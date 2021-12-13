from models import Produto
from schemas import ProdutoSchema

async def criar_produto(produto: Produto):
    return await produto.save()


async def get_produtos():
    return await Produto.objects.all()

async def delete_produto(produto_id: int):
    return await Produto.objects.delete(id = produto_id)

async def atualizar_produto(produto: ProdutoSchema):
    p =  await Produto.objects.get(id = produto.id)
    p.nome = produto.nome
    p.preco = produto.preco
    await p.update()
    return p
    
