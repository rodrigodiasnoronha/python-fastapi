from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from models import Usuario
from services import auth_service
from functions import auth_functions

router = APIRouter(prefix="/auth", tags=["Autenticação"], dependencies=[])

@router.post('/login')
async def post_login(form_data: OAuth2PasswordRequestForm = Depends() ):
    return await auth_service.login(form_data)

@router.post('/token')
async def get_usuario_by_token(usuarioLogado: Usuario = Depends(auth_functions.get_current_user)):
    return usuarioLogado
