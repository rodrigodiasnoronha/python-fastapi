from fastapi import APIRouter, status, Response
from fastapi.param_functions import Depends
from services import produto_service
from models import Usuario, Produto
from schemas import ProdutoSchema
from functions import auth_functions


router = APIRouter(prefix="/produtos", dependencies=[], tags=["Produtos"])

@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_criar_produto(response: Response, produto: Produto, usuario: Usuario = Depends(auth_functions.get_current_user)):
    return await produto_service.criar_produto(produto, usuario)

@router.get('/')
async def get_produtos():
    return await produto_service.get_produtos()

@router.delete('/{produto_id}')
async def delete_produto(produto_id: int):
    return await produto_service.delete_produto(produto_id=produto_id)

@router.get('/produtos-by-user-id/{id}')
async def get_produtos_by_user(id: int):
    return await produto_service.get_produtos_by_user(id)

@router.put('/')
async def atualizar_produto(produto: ProdutoSchema):
    return await produto_service.atualizar_produto(produto)

@router.delete('/{produto_id}')
async def del_produto(produto_id: int):
    return await produto_service.delete_produto(produto_id)

@router.put('/')
async def atualizar_produto(produto: Produto):
    return await produto_service.atualizar_produto(produto)