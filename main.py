"""
Created on Mon Feb 8
A Pokemon clone for the terminal.
@author: Andrew Alagna
"""
import random
from rich import print
from dataclasses import dataclass, field, asdict


@dataclass
class Pokemon:
    name: str = 'PokeMon'
    gender: str = random.choice(['Male', 'Female'])
    type_of_pokemon: str = "Rando"
    nature: str = 'normal'
    moves: dict[str:int] = field(default_factory=dict)
    health: int = 100


def generate_rand_pokemon():
    fuego = Pokemon('fuego', 'female', "Charzard", 'Fire', {'Flamethrower': 20, 'Claw': 15})
    rocky = Pokemon('rocky', 'male', 'Geodude', 'Rock', {'Rock-throw': 20, 'head-butt': 15})
    mew = Pokemon('mew', 'neutral', 'Mew', 'Psychic', {'Mind-beam': 20, 'Psychic-slam': 25})
    snore = Pokemon('snore', 'male', 'Snorlax', 'Normal', {'Body-slam': 20, 'Slap': 15})
    rocky = Pokemon('rocky', 'female', 'Onyx', 'Normal', {'Body-slam': 20, 'Slap': 15})
    return random.choice([fuego, rocky, mew, snore])


@dataclass
class Player:
    name: str = "Player"
    gender: str = random.choice(['Male', 'Female'])
    nature: str = 'Fun'
    pokemon_list: list[Pokemon] = field(default_factory=list)
    bag: dict[str:int] = field(default_factory=dict)
    money: int = 10000

    def print_poke_list(self):
        names = []
        for poke in enumerate(self.pokemon_list):
            names.append(poke[1].name)
        print(names)

    def __repr__(self):
        return "\U0001FAE1"


class GridSquare:
    def __init__(self):
        possible_options = [0, 1, 2, 3, 4]  # 0 = cant access, 1 =  empty land, 2 = pokemon, 3 = pokeball, 4 = CPU
        distribution = [.02, .60, .13, .05, .10]
        self.terrain = random.choice(['grass', 'water', 'concrete'])
        self.occupied_with = random.choices(possible_options, distribution)[0]

    def __repr__(self):  # 0 = cant access, 1 =  empty land, 2 = pokemon, 3 = pokeball, 4 = CPU, -1 = visited
        if self.occupied_with == 0:
            return "\U0001F6B7"
        if self.occupied_with == 1:
            return random.choice(["\U0001F334"])
        if self.occupied_with == 2:
            return '\U0001F994'
        if self.occupied_with == 3:
            return "\U000026D4"
        if self.occupied_with == 4:
            return "\U0001F94A"
        if self.occupied_with == Player:
            return "\U0001FAE1"
        if self.occupied_with == -1:
            return "\U00002705"


class Grid:
    def __init__(self):
        self.grid = [[GridSquare() for i in range(8)] for i in range(8)]
        self.grid[0][
            0] = GridSquare.occupied_with = player1  # The starting player is represented as 9, and visited squares will be marked as -1.
        self.row_pos, self.col_pos = 0, 0

    def print_grid(self):
        print(self.grid)


# Dont need to keep track of visited cells, but could be good practice to use the grid teq mentioned by professor.
def traverse_grid(grid):
    grid.print_grid()
    dir_row, dir_col = [-1, 0, 1, 0], [0, 1, 0, -1]  # North[0], east[1], south[2], west[3]
    made_move = False
    while made_move is False:
        direction = input("Do you want to go W (up), A (left), S (down), or D (right)? ")
        if direction.upper() == 'W':  # north
            rr = grid.row_pos + dir_row[0]
            cc = grid.col_pos + dir_col[0]
        if direction.upper() == 'D':
            rr = grid.row_pos + dir_row[1]
            cc = grid.col_pos + dir_col[1]
        if direction.upper() == 'S':
            rr = grid.row_pos + dir_row[2]
            cc = grid.col_pos + dir_col[2]
        if direction.upper() == 'A':
            rr = grid.row_pos + dir_row[3]
            cc = grid.col_pos + dir_col[3]
        if rr < 0 or cc < 0 or rr >= 8 or cc >= 8 or grid.grid[rr][cc].occupied_with == 0:  # 8 is size of rows and cols or edge of grid
            direction = input(
                "You cannot move there or were already there. Try again, Enter W/A/S/D to move in a different direction: ")
        else:
            if grid.grid[rr][cc].occupied_with == 4:
                battle(player1)
            if grid.grid[rr][cc].occupied_with == 3:
                player1.bag['pokeball'] += 1
                print("Sweet, you found a pokeball!! [blue]")
            if grid.grid[rr][cc].occupied_with == 2:
                wild_pokemon(player1)
            grid.grid[grid.row_pos][grid.col_pos] = GridSquare()
            grid.grid[grid.row_pos][grid.col_pos].occupied_with = -1
            grid.grid[rr][cc] = player1
            grid.row_pos, grid.col_pos = rr, cc
            made_move = True


@dataclass
class CpuPlayer:
    name: str = random.choice(['Jenny', 'James', 'Jamal', 'Drizzy', 'Sam', 'Rachel'])
    pokemon: Pokemon = generate_rand_pokemon()
    cash_award: int = random.randint(10000, 100000)
    poke_gift: Pokemon = pokemon
    fact: str = f"My name is {name}, get ready to battle me!"


def throw_pokeball(player, pokemon):
    player.bag['pokeball'] -= 1
    if pokemon.health > 75:
        if random.random() < .35:
            print(f'Congrats, you captured {pokemon.type_of_pokemon}!')
            return player.pokemon_list.append(pokemon)
        else:
            return print(f'You did not capture {pokemon.type_of_pokemon}!')
    elif pokemon.health < 40:
        if random.random() <= .75:
            print(f'Congrats, you captured {pokemon.type_of_pokemon}!')
            return player.pokemon_list.append(pokemon)
        else:
            return print(f'You did not capture {pokemon.type_of_pokemon}!')


def use_potion(player, pokemon):
    if player.bag['potion'] > 0:
        player.bag['potion'] -= 1
        pokemon.health += 40
        print(f'Your pokemon now has {pokemon.health} health!')
    else:
        print("You do not have any more potions!")


def battle(player):  # player2 will always be a CPU for now
    cpu = CpuPlayer()
    print(cpu.fact)
    print(f'You will be starting the battle with {player.pokemon_list[0].name} (a {player.pokemon_list[0].type_of_pokemon}), and battling {cpu.pokemon.name} (a {cpu.pokemon.type_of_pokemon})')
    print("You have the first move!")
    while player.pokemon_list is not None and cpu.pokemon.health > 0:
        pokemon = player.pokemon_list[0]  # We will always battle with your pokemon in order of your list.
        move = input(
            f"Do you want to use move 1 ({next(iter(pokemon.moves))}), move 2 ({list(pokemon.moves.keys())[1]}), or use a potion (P)? ")
        if move == '1':
            cpu.pokemon.health -= list(pokemon.moves.values())[0]
            print(f"Their pokemon has {cpu.pokemon.health} health left")
        elif move == '2':
            cpu.pokemon.health -= list(pokemon.moves.values())[1]
            print(f"Their pokemon has {cpu.pokemon.health} health left")
        elif move.upper() == 'P':
            use_potion(player, pokemon)
        if pokemon.health <= 0 and player.bag['potion'] != 0:
            use = input("Your pokemon is about to faint, do you want to use a potion? (Y or N)")
            if use == 'Y': use_potion(player, pokemon)
            else:
                rip = player.pokemon_list.pop(0)
                print(f"{rip.name} has fainted!")
                if player.pokemon_list is not None: print(f'You will now fight with {player.pokemon_list[0].name}!')
        cpu_move = random.choice(list(cpu.pokemon.moves.keys()))
        pokemon.health -= cpu.pokemon.moves[cpu_move]
        print(f"You were hit with {cpu_move} for {cpu.pokemon.moves[cpu_move]} health points! You have {pokemon.health} health left.")
    print(f"Good job, you defeated {cpu.name}!")
    cpu.pokemon.health = 100
    player.pokemon_list.append(cpu.pokemon)
    print(f"You won a {pokemon.type_of_pokemon}! Congrats!")


def starting_player_info():
    player_name = input("Hello there! What is your name?: ")
    gender = input("What is your gender?: ")
    nature = input("How would you describe your nature?: ")
    starter_pokemon = input("Which pokemon do you want to start with? P - Pikachu, C - Charmander, or S - Squirtle?: ")
    starter_pokemon = choose_starter_pokemon(starter_pokemon)
    return Player(player_name, gender, nature, [starter_pokemon], {'potion': 2, 'pokeball': 1}, 10000)


def choose_starter_pokemon(starter_pokemon):
    while starter_pokemon is None and starter_pokemon[0].upper() != 'P' and starter_pokemon[0].upper() != 'C' and \
            starter_pokemon[0].upper() != 'S':
        starter_pokemon = input("Please enter the first letter P (Pikachu) , C (Charmander), or S (Squirtle) to choose "
                                "your starter pokemon")
    name = input('What do you want to name your pokemon?: ')
    if starter_pokemon == 'P' or starter_pokemon[0].upper() == 'P':
        return Pokemon(name, random.choice(["Male", "Female"]), "Pikachu", 'Electric', {'Shock': 40, 'Tail Whip': 25})
    elif starter_pokemon == 'C' or starter_pokemon[0].upper() == 'C':
        return Pokemon(name, random.choice(["Male", "Female"]), "Charmander", 'Fire', {'Flamethrower': 40, 'Claw': 25})
    elif starter_pokemon == 'S' or starter_pokemon[0].upper() == 'S':
        return Pokemon(name, random.choice(["Male", "Female"]), "Squirtle", 'Water', {'Hydropump': 40, 'Tackle': 25})


def wild_pokemon(player):
    pokemon = generate_rand_pokemon()
    print(f"Get ready to fight {pokemon.name}!")


def playing_game(player):
    grid = Grid()
    while player.pokemon_list is not None and len(player.pokemon_list) < 4:
        traverse_grid(grid)
    print("Game over! You have 4 pokemon, or all of yours have lost. Thanks for playing", ":smile:")
    player.print_poke_list()


# 0 = cant access, 1 =  empty land, 2 = pokemon, 3 = pokeball, 4 = CPU
if __name__ == "__main__":
    player1 = starting_player_info()
    print("Hello [bold blue]" + player1.name + " and Rich python[/bold blue]!", )
    playing_game(player1)
