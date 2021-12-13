from pydantic import BaseModel

from typing import Optional

class ProdutoSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float