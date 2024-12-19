import os
import logging
from dotenv import load_dotenv
from authlib.integrations.starlette_client import OAuth
from fastapi.security import OAuth2PasswordBearer

load_dotenv()
logger = logging.getLogger(__name__)

oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.getenv("AUTH_GG_CLIENT_ID"),
    client_secret=os.getenv("AUTH_GG_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile",
        "redirect_url": "http://localhost:8000/api/v1/auth/google",
    },
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
