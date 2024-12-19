import os
import logging
from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.responses import RedirectResponse
import jwt
from datetime import datetime, timedelta
import jwt.exceptions
from starlette.requests import Request

from backend.src.lib.auth import oauth, oauth2_scheme

logger = logging.getLogger(__name__)


class AuthService:
    def __init__(self):
        logger.info("AuthService initialized")

    async def login_via_google(self, request: Request):
        redirect_uri = request.url_for("auth_via_google")
        return await oauth.google.authorize_redirect(request, redirect_uri)

    async def auth_via_google(self, request: Request):
        token = await oauth.google.authorize_access_token(request)
        user = token["userinfo"]

        access_token = self.create_access_token(data={"sub": user["email"]})
        response = RedirectResponse(url="http://localhost:5173/chatbot")
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            samesite="Strict",
            # secure=True,
        )

        return response

    def create_access_token(
        self, data: dict, expires_delta: timedelta = timedelta(hours=1)
    ):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            os.getenv("AUTH_SECRET_KEY"),
            algorithm=os.getenv("AUTH_ALGORITHM"),
        )
        return encoded_jwt.decode("utf-8")

    def verify_jwt_token(self, request: Request):
        try:
            token = request.cookies.get("access_token")

            if not token:
                raise HTTPException(status_code=401, detail="Token is missing")

            payload = jwt.decode(
                token,
                os.getenv("AUTH_SECRET_KEY"),
                algorithms=os.getenv("AUTH_ALGORITHM"),
            )

            logger.info(payload)
            return payload
        # except jwt.ExpiredSignatureError:
        #     raise HTTPException(status_code=401, detail="Token has expired")
        # except jwt.PyJWTError:
        #     raise HTTPException(status_code=401, detail="Invalid token")
        except Exception as e:
            logger.error(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
