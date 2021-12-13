import databases
import sqlalchemy

import ormar

dbURL = "sqlite:///database.sqlite"

database = databases.Database(dbURL)
metadata = sqlalchemy.MetaData()

class Produto(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key = True, autoincrement=True)
    nome: str= ormar.String(max_length=255)
    preco: int = ormar.Float(default = 0)

engine = sqlalchemy.create_engine(dbURL)
metadata.create_all(engine)