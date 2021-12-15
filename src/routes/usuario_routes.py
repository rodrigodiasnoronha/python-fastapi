from fastapi import APIRouter, Response, status
from fastapi.param_functions import Depends
from services import usuario_service, auth_service
from schemas import UsuarioSchema
from models import Usuario
from functions import auth_functions

router = APIRouter(prefix="/usuarios",
    tags=["Usuários"],
    dependencies=[], # array de middlewares Depends(middleware)
)

@router.post('/', status_code= status.HTTP_201_CREATED)
async def post_criar_usuario(usuario: UsuarioSchema, response: Response):
    return await usuario_service.criar_usuario(usuario, response)

@router.get('/')
async def get_usuarios():
    return await usuario_service.get_usuarios()

@router.get('/usuario-logado')
async def get_usuario_logado(usuarioLogado: Usuario = Depends(auth_functions.get_current_user)):
    return await auth_service.get_usuario_logado(usuarioLogado)
