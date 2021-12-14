from models import Produto
from schemas import ProdutoSchema
from models import Usuario

async def criar_produto(produto: Produto, usuario: Usuario):
    produto.usuario_id = usuario.id
    return await produto.save()

async def get_produtos():
    return await Produto.objects.select_related('usuario_id').all()

async def delete_produto(produto_id: int):
    return await Produto.objects.delete(id = produto_id)

async def atualizar_produto(produto: ProdutoSchema):
    p =  await Produto.objects.get(id = produto.id)
    p.nome = produto.nome
    p.preco = produto.preco
    await p.update()
    return p
    
async def get_produtos_by_user(user_id: int):
    user = await Usuario.objects.filter(id = user_id).select_related('produtos').get()
    return user