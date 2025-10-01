from pydantic import BaseModel 

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        from_attibutes = True