from typing import List, Optional
import databases
import sqlalchemy

import ormar

dbURL = "sqlite:///database.sqlite"

database = databases.Database(dbURL)
metadata = sqlalchemy.MetaData()


class Usuario(ormar.Model):
    class Meta():
        metadata = metadata
        database = database
        tablename = "tb_usuarios"

    id: int = ormar.Integer(primary_key=True, autoincrement = True)
    nome: str = ormar.String(nullable = False, max_length=255)
    email: str = ormar.String(nullable= False, unique = True, max_length =255)
    senha: str = ormar.String(nullable = False, min_length= 8, max_length = 255)
class Ingrediente(ormar.Model):

    class Meta():
        metadata = metadata
        database = database
        tablename = "tb_ingredientes"

    id: int = ormar.Integer(primary_key = True, autoincrement = True)
    nome: str = ormar.String(nullable = False, max_length = 255)
    usuario_id: Optional[Usuario] = ormar.ForeignKey(Usuario)


class Produto(ormar.Model):
    class Meta():
        metadata = metadata
        database = database
        tablename = "tb_produtos"

    id: int = ormar.Integer(primary_key = True, autoincrement=True)
    nome: str= ormar.String(max_length=255)
    preco: int = ormar.Float(default = 0)
    usuario_id: Optional[Usuario] = ormar.ForeignKey(Usuario)
    ingredientes: Optional[List[Ingrediente]] = ormar.ManyToMany(Ingrediente)



engine = sqlalchemy.create_engine(dbURL)
metadata.create_all(engine)