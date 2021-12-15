from fastapi import APIRouter
from fastapi.param_functions import Depends
from services import ingrediente_service
from models import Ingrediente, Usuario
from functions import auth_functions

router = APIRouter(prefix="/ingredientes", dependencies=[], tags=["Ingredientes"])

@router.post('/')
async def post_criar_ingrediente(ingrediente: Ingrediente, usuarioLogado: Usuario = Depends(auth_functions.get_current_user)):
    return await ingrediente_service.criar_ingrediente(ingrediente, usuarioLogado)

@router.get('/')
async def get_ingredientes():
    return await ingrediente_service.get_ingredientes()