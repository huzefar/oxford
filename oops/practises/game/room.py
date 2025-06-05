from __future__ import annotations
from typing import Self

class Room:
    """
    The Room class consists of a name and a descrtiption
    """

    __name: str
    __description: str
    __exists: dict

    def __new__(cls, name: str, description: str) -> Self:

        # This creates a new instance of the class
        self = super().__new__(cls)

        self.__name = name
        self.__description = description
        self.__exists = {}

        # return the pointer created by the constructor
        return self

    def connect_exit(self, direction: str, room: Room) -> None:
        """
        Connects the current room to another room in a given direction.
        """
        self.__exists[direction] = room

    def get_exit(self, direction: str) -> Room | None:
        """
        Returns the room in a given direction if it exists, otherwise returns None.
        """
        return self.__exists.get(direction)

    @property
    def name(self) -> str:
        """
        Returns the name of the room.
        """
        return self.__name

    @property
    def description(self) -> str:
        """
        Returns the description of the room.
        """
        return self.__description
