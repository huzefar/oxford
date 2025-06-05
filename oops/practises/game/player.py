from __future__ import annotations
from .room import Room
from typing import Self


class Player:
    """
    The Player class consists starting room where the player starts his journey
    """
    __current_room: Room

    def __new__(cls, starting_room: Room) -> Self:
        
        self = super().__new__(cls)
        
        self.__current_room = starting_room

        return self
    
    def move_to(self, direction: str) -> None:
        """
        Moves the player to the room in the given direction if it exists.
        """
        next_room = self.__current_room.get_exit(direction)

        if next_room:
            self.__current_room = next_room
        else:
            print(f"Cannot move {direction}, no exit in that direction.")
    

    @property
    def currentroom(self) -> Room:
        """
        Returns the current room of the player.
        """
        return self.__current_room