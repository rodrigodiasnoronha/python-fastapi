from models import Usuario
from fastapi import Response, status
import bcrypt

from schemas import UsuarioSchema
from models import Usuario
from functions import auth_functions


async def criar_usuario(usuario: UsuarioSchema, response: Response):
    usuarioExiste = await Usuario.objects.get_or_none(email = usuario.email)

    if (usuarioExiste is not None):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { "erro": "Email já em uso", "status_code": status.HTTP_400_BAD_REQUEST }

    hashSenha = auth_functions.get_password_hash(usuario.senha)

    return await Usuario.objects.create(email = usuario.email, senha = hashSenha, nome = usuario.nome)

async def get_usuarios():
    return await Usuario.objects.all()