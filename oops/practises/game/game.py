
from __future__ import annotations
from .room import Room
from .player import Player
from typing import Self

class Game:
    """
    A class to represent a game.
    """
    rooms : dict[str, Room] = {}

    def __new__(cls) -> Self:
        """
        Creates a new instance of the Game class.
        This method initializes the game with an empty list of players,
        a current player index set to 0, and a game_over flag set to False.
        """
        # This creates a new instance of the class
        self = super().__new__(cls)
        self.players = []
        self.current_player_index = 0
        self.game_over = False
        return self

    def add_player(self, player):
        """
        Adds a player to the game.

        :param player: The player to add.
        """
        self.players.append(player) 