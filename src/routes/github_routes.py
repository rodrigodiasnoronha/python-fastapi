from fastapi import APIRouter
from services import github_service

router = APIRouter(prefix="/github", dependencies=[], tags=["Github"])

@router.get('/{username}')
async def get_usuario_github(username: str):
    return await github_service.get_usuario_github_by_username(username)