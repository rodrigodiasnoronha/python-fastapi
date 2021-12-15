from fastapi import FastAPI, status

from fastapi.security import OAuth2PasswordBearer 
from routes import github_routes, ingrediente_routes, produto_routes, usuario_routes, auth_routes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app  = FastAPI()

app.include_router(auth_routes.router)
app.include_router(github_routes.router)
app.include_router(usuario_routes.router)
app.include_router(ingrediente_routes.router)
app.include_router(produto_routes.router)
