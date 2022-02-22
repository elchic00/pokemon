from dataclasses import dataclass, field, asdict
import random


@dataclass
class Player:
    name: str = "Player"
    gender: str = random.choice(['Male', 'Female'])
    nature: str = 'Fun'
    pokemon_list: list[Pokemon] = field(default_factory=list)
    bag: dict[str:int] = field(default_factory=dict)
    money: int = 10000
