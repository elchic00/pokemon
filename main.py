"""
Created on Mon Feb 8
@author: Andrew Alagna
"""
import random
from rich import print
from dataclasses import dataclass, field


@dataclass
class Player:
    def __init__(self, name, gender, nature, pokemon_list, bag, money):
        self.name = name
        self.gender = gender
        self.nature = nature
        self.pokemon_list = pokemon_list
        self.bag = bag
        self.money = money

    def print_poke_list(self):
        for i in range(len(self.pokemon_list)):
            print(self.pokemon_list[i].name)


@dataclass
class Pokemon:
    name: str = 'PokeMon'
    gender: str = random.choice(['Male', 'Female'])
    type_of_pokemon: str = "Rando"
    nature: str = 'normal'
    moves: dict[str:int] = field(default_factory=dict)
    health: int = 100


class Grid:
    def __init__(self):
        self.grid = [[GridSquare() for i in range(8)] for i in range(8)]
        self.curr_pos = [0][0]
        self.grid[0][0].occupied_with = 9  # The starting player is represented as 9

    def print_grid(self):
        print(self.grid)


class GridSquare:
    def __init__(self):
        possible_options = [0, 1, 2, 3, 4]  # 0 = cant access, 1 =  empty land, 2 = pokemon, 3 = pokeball, 4 = CPU
        distribution = [.02, .60, .13, .05, .10]
        self.terrain = random.choices(['grass', 'water', 'concrete'], [.4, .2, .4])[0]
        self.occupied_with = random.choices(possible_options, distribution)[0]

    def __repr__(self):
        return f'{self.occupied_with}'

    def __str__(self):
        return f'{self.occupied_with}'


class CpuPlayer:
    def __init__(self, pokemon_list=[], poke_gift={}, fact="Im a CPU, ready to battle!!"):
        self.name = random.choice(['Jenny', 'James', 'Jamal', 'Drew', 'Sam', 'Rachel'])
        self.pokemon_list = pokemon_list
        self.cash_award = random.randint(10000, 100000)
        self.poke_gift = poke_gift
        self.fact = fact

    def __str__(self):
        return f'Hello, I"m {self.name}. Are you ready to battle?'


# class PokeBalls:
#     def __init__(self):


# class PokeMoves:
#     def __init__():

def traverse(grid):
    direction = input("Which direction do you want to move, up (W), left (A), down (S), or right (D)?")
    while direction.upper() != 'W' and direction.upper() != 'A' and direction.upper() != 'S' and direction.upper() != 'D':
        direction = input("Please use A/W/S/D and enter to choose which direction to move.")


def throw_pokeball(player, pokemon):
    if pokemon.health > 75:
        if random.random() < .35:
            print(f'Congrats, you captured {pokemon.type_of_pokemon}!')
            return player.pokemon_list.append(pokemon)
        else:
            return print(f'You did not capture {pokemon.type_of_pokemon}!')
    elif pokemon.health < 40:
        if random.random() <= .75:
            return player.pokemon_list.append(pokemon)
        else:
            return print(f'You did not capture {pokemon.type_of_pokemon}!')


def use_potion(player, pokemon):
    if player.bag is not None:
        player.bag['potion'] -= 1
        pokemon.health += 20


def battle(player1, player2):  # player2 will always be a CPU for now
    print(f"Get ready to fight {player2.name} !!")


def starting_player_info():
    player_name = input("Hello there! What is your name?: ")
    gender = input("What is your gender?: ")
    nature = input("How would you describe your nature?: ")
    starter_pokemon = input("Which pokemon do you want to start with? P - Pikachu, C - Charmander, or S - Squirtle?: ")
    starter_pokemon = choose_starter_pokemon(starter_pokemon)
    return Player(player_name, gender, nature, [starter_pokemon], {'potion': 2}, 10000)


def choose_starter_pokemon(pokemon):
    while pokemon[0].upper() != 'P' and pokemon[0].upper() != 'C' and pokemon[0].upper() != 'S':
        pokemon = input("Please enter the first letter P (Pikachu) , C (Charmander), or S (Squirtle) to choose "
                        "your starter pokemon")
    name = input('What do you want to name your pokemon?: ')
    if pokemon == 'P' or pokemon[0].upper() == 'P':
        return Pokemon(name, random.choice(["Male", "Female"]), "Pikachu", 'Electric', {'Shock': 35, 'Tail Whip': 20},
                       100)
    elif pokemon == 'C' or pokemon[0].upper() == 'C':
        return Pokemon(name, random.choice(["Male", "Female"]), "Charmander", 'Fire', {'Flamethrower': 40, 'Claw': 20},
                       100)
    elif pokemon == 'S' or pokemon[0].upper() == 'S':
        return Pokemon(name, random.choice(["Male", "Female"]), "Squirtle", 'Water', {'Hydropump': 40, 'Tackle': 20},
                       100)


# def game_start():
#     player1 = starting_player_info()
#     grid = Grid()
#     print(grid.grid[0][0])
#     # fuego = Pokemon('Fuego', 'female', "Charzard", 'Fire', {'Fire blast': 75, 'Flamethrower': 50, 'Claw': 35}, 150)
#     player1.print_poke_list()
#     throw_pokeball(player1, player1.pokemon_list[0])
#     player1.print_poke_list()
#     grid.print_grid()
#     print("Hello [bold blue]" + player1.name + " and Rich python[/bold blue]!", ":thumbs_up:")


# 0 = cant access, 1 =  empty land, 2 = pokemon, 3 = pokeball, 4 = CPU
if __name__ == "__main__":
    p = Pokemon()
    print(p)
    player1 = starting_player_info()
    print(player1)
    grid = Grid()
    # fuego = Pokemon('Fuego', 'female', "Charzard", 'Fire', {'Fire blast': 75, 'Flamethrower': 50, 'Claw': 35}, 150)
    player1.print_poke_list()
    throw_pokeball(player1, player1.pokemon_list[0])
    player1.print_poke_list()
    grid.print_grid()
    print("Hello [bold blue]" + player1.name + " and Rich python[/bold blue]!", ":thumbs_up:")
