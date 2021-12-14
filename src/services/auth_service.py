from fastapi import status
from datetime import timedelta
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from passlib.context import CryptContext
from models import Usuario
from functions import auth_functions
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 # 1 dia

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    usuario = await auth_functions.authenticate_user(form_data.username, form_data.password)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos",        
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_functions.create_access_token(
        data={"usuario": dict(usuario)}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

    
async def get_usuario_logado(usuarioLogado: Usuario):
    return usuarioLogado