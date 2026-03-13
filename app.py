import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input
"""
def poke():
    lang = input("what language (english, japanese, french, or chinese) ")
    for i, item in enumerate(data):
        print(index, ":", item["name"][lang])
poke()
"""
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

def type():
    type = input("what type you want? (Grass, Fire, Water, Normal, Flying, Poison, Bug, Electric) ")
    lang = input("what language (english, japanese, french, or chinese) ")
    for i in data:
        if type in i["type"]:
            print(i["name"][lang])
    if type != "Grass" or "Fire" or "Water" or "Normal" or "Flying" or "Poison" or "Bug" or "Electric":
        print("nothing found kid")
type()
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type
