from models import Ingrediente, Usuario

async def criar_ingrediente(ingrediente: Ingrediente, usuario: Usuario):
    ingrediente.usuario_id = usuario.id
    return await ingrediente.save()

async def get_ingredientes():
    return await Ingrediente.objects.select_related('usuario_id').all()
    