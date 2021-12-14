from pydantic import BaseModel

from typing import Optional

class ProdutoSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float

class UsuarioSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    senha: str

class LoginSchema(BaseModel):
    email: str
    senha: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class TokenDataSchema(BaseModel):
    usuario: UsuarioSchema