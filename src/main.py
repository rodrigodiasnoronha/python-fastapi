from fastapi import FastAPI, status, Response
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from models import Produto, Usuario
from services import produto_service, github_service, usuario_service, auth_service
from schemas import ProdutoSchema, UsuarioSchema, LoginSchema

from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from functions import auth_functions

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app  = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
def root():
    return {  "Olá": "Mundo" }

@app.post('/produtos', status_code=status.HTTP_201_CREATED)
async def post_criar_produto(response: Response, produto: Produto, usuario: Usuario = Depends(auth_functions.get_current_user)):
    return await produto_service.criar_produto(produto, usuario)

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

@app.post('/usuarios', status_code= status.HTTP_201_CREATED)
async def post_criar_usuario(usuario: UsuarioSchema, response: Response):
    return await usuario_service.criar_usuario(usuario, response)

@app.get('/usuarios')
async def get_usuarios():
    return await usuario_service.get_usuarios()

@app.post('/login')
async def post_login(form_data: OAuth2PasswordRequestForm = Depends() ):
    return await auth_service.login(form_data)

@app.post('/token')
async def get_usuario_by_token(usuarioLogado: Usuario = Depends(auth_functions.get_current_user)):
    return usuarioLogado

@app.get('/usuario-logado')
async def get_usuario_logado(usuarioLogado: Usuario = Depends(auth_functions.get_current_user)):
    return await auth_service.get_usuario_logado(usuarioLogado)

@app.get('/produtos-by-user-id/{id}')
async def get_produtos_by_user(id: int):
    return await produto_service.get_produtos_by_user(id)