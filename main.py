#Para rodar nosso código, executar no terminal: python -m uvicorn main:app --reload
from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv() # carrega as variaveis de ambientes do .env
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACESS_TOKEN_EXPIRE_MINUTES"))

bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

from auth_routes import auth_router
from order_routes import order_router

app =  FastAPI()


app.include_router(auth_router)
app.include_router(order_router)
