from select import select
from bson.son import SON
from src.db.database import Database

db = Database()

#Pokémons com mais de um tipo
pokemons = db.collection.find({ "type": {"$size": 2}},{"name": 1, 'type': 1, "_id": 0})
pokelist = []
for pokemon in pokemons:
    pokelist.append(pokemon)
print(pokelist)

#Pokémons com mais de uma evolução
pokemons = db.collection.find({ "next_evolution": {"$size": 2} },{"_id": 0, "name": 1})
pokelist = []
for pokemon in pokemons:
    pokelist.append(pokemon)
print(pokelist)

#Pokémons sem Evolução
pokemons = db.collection.find({ "next_evolution": { "$exists": False }},{"_id": 0, "name": 1})
pokelist = []
for pokemon in pokemons:
    pokelist.append(pokemon)
print(pokelist)

#Pokémons sem ovo
pokemons = db.collection.find({ "egg": {"$eq": "Not in Eggs"} },{"_id": 0, "name": 1})
pokelist.clear()
for pokemon in pokemons:
    pokelist.append(pokemon)
print(pokelist)

#Pokémons raros
pokemons = db.collection.find({ "spawn_chance": {"$lt": 0.001} },{"_id": 0, "name": 1})
pokelist.clear()
for pokemon in pokemons:
    pokelist.append(pokemon)
print(pokelist)