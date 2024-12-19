import os
import logging
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import JSONResponse

from backend.src.dbs.init_postgres import instance_postgres
from backend.src.routes.main import main_router
from backend.src.lib.auth import oauth

load_dotenv()
logging.basicConfig(level=logging.INFO, force=True)

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware, secret_key=os.getenv("AUTH_SESSION_SECRET_KEY"))

app.include_router(main_router)
instance_postgres()


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred"},
    )
