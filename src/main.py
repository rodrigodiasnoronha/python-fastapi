from fastapi import FastAPI, status, Response
from ormar import models
from starlette.status import HTTP_400_BAD_REQUEST

from models import Produto
from services import produto_service, github_service
from schemas import ProdutoSchema



app  = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
def root():
    return {  "Olá": "Mundo" }


@app.post('/produtos', status_code=status.HTTP_201_CREATED)
async def post_criar_produto(response: Response, produto: Produto):
    return await produto_service.criar_produto(produto)

@app.get('/produtos')
async def get_produtos():
    return await produto_service.get_produtos()

@app.delete('/produtos/{produto_id}')
async def delete_produto(produto_id: int):
    return await produto_service.delete_produto(produto_id=produto_id)

@app.put('/produtos')
async def atualizar_produto(produto: ProdutoSchema):
    return await produto_service.atualizar_produto(produto)

@app.get('/github/{username}')
async def get_usuario_github(username: str):
    return await github_service.get_usuario_github_by_username(username)