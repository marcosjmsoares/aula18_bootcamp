import requests
from pydantic import BaseModel 

class PokemonSchame(BaseModel):
    name: str
    type: str

    class Config:
        from_attibutes = True

def pegar_pokemon(id: int) -> PokemonSchame:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    data_types = data['types']
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchame(name=data['name'], type=types)

if __name__ == "__main__":
    print(pegar_pokemon(10))
    print(pegar_pokemon(20))
    print(pegar_pokemon(30))
    print(pegar_pokemon(40))