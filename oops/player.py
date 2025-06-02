from __future__ import annotations
from .room import Room
from typing import Self

"""
The Player class represent a player in the game.
"""

class Player:
    """
    The Player class consists starting room where the player starts his journey
    """
    __current_room: Room

    def __new__(cls, starting_room: Room) -> Self:
        
        self = super().__new__(cls)
        
        self.__room = starting_room

        return self
    
    def move_to(self, direction: str) -> None:
        """
        Moves the player to the room in the given direction if it exists.
        """
        next_room = self.__room.get_exit(direction)
        if next_room:
            self.__room = next_room
        else:
            print(f"Cannot move {direction}, no exit in that direction.")
    
"""
    __name: str
    __description: str

    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description
"""