import requests

async def get_usuario_github_by_username(username: str):
    r = requests.get('https://api.github.com/users/' + username)
    return r.json()