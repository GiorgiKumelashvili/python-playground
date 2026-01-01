from __future__ import annotations

import sys
from enum import Enum
from types import DynamicClassAttribute
from typing import Dict

import pyfiglet

WINING_POSITION_INDEXES = [
    # horizontals
    "123",
    "456",
    "789",
    # verticals
    "147",
    "258",
    "369",
    # diagonals
    "159",
    "357",
]


class Player(Enum):
    EMPTY = 0
    FIRST = 1
    SECOND = 2

    @DynamicClassAttribute
    def display(self):
        if self == Player.FIRST:
            return "X"
        elif self == Player.SECOND:
            return "O"
        else:
            return ""

    @DynamicClassAttribute
    def inverted(self):
        return Player.FIRST if self == Player.SECOND else Player.SECOND


class Board:
    display: str
    isNumberedBoard: bool

    def __init__(self):
        self.isNumberedBoard = False

        if self.isNumberedBoard:
            self.display = (
                "| 1 | | 2 | | 3 |\n\n| 4 | | 5 | | 6 |\n\n| 7 | | 8 | | 9 |\n\n"
            )
        else:
            self.display = (
                "|   | |   | |   |\n\n|   | |   | |   |\n\n|   | |   | |   |\n\n"
            )

    def __str__(self):
        return self.display

    def rebuild(self, values: Dict[str, Player]):
        final_board = ""

        for index, (key, value) in enumerate(values.items()):
            if index % 3 == 0:
                final_board += "\n\n"

            additional_space = "" if int(key) % 3 == 1 else " "

            if value != Player.EMPTY:
                display_input_type = "X" if value == Player.FIRST else "O"
                final_board += f"{additional_space}| {display_input_type} |"
            else:
                if self.isNumberedBoard:
                    final_board += f"{additional_space}| {key} |"
                else:
                    final_board += f"{additional_space}|   |"

        self.display = final_board


class Game:
    state: Dict[str, Player]
    player_active: Player
    board: Board
    is_game_finished: bool

    def __init__(self) -> None:
        self.state = {str(x): Player.EMPTY for x in range(1, 10)}
        self.is_game_finished = False
        self.player_active = Player.FIRST
        self.board = Board()

    def _update_position(self, position) -> None:
        self.state[position] = self.player_active

    def _validate(self, position) -> str | None:
        if position not in self.state.keys():
            available_values = ", ".join([x for x in self.state.keys()])
            return f"Incorrect value given, should be between {available_values}"

        if self.state[position] != Player.EMPTY:
            return f"Already places value there, choose another place"

        return None

    def _is_game_finished(self) -> str | None:
        active_player_positions = [
            key for (key, value) in self.state.items() if value == self.player_active
        ]

        all_available_position = [
            key
            for (key, value) in self.state.items()
            if value == Player.FIRST or value == Player.SECOND
        ]

        for pos in WINING_POSITION_INDEXES:
            wining_combination = "".join(active_player_positions)

            if all(c in iter(wining_combination) for c in pos):
                self.is_game_finished = True
                return f"{self.player_active.display} has Won"

        if len(all_available_position) == 9:
            self.is_game_finished = True
            return "It is a draw"

        return None

    def start(self) -> None:
        print(
            "\n\n" + pyfiglet.figlet_format(text="Welcome to tic tac toe", font="slant")
        )
        print(f"\n{self.board}")

        while self.is_game_finished != True:
            sys.stdout.flush()

            position = input(
                f"\nWhich position you want to input {self.player_active.display}: "
            )

            validate_message = self._validate(position)

            if isinstance(validate_message, str):
                print(validate_message)
                continue

            self._update_position(position)
            self.board.rebuild(self.state)

            print(self.board)

            finish_message = self._is_game_finished()

            if isinstance(finish_message, str):
                print(
                    "\n"
                    + pyfiglet.figlet_format(text=finish_message, font="slant")
                    + "\n"
                )
                break

            self.player_active = self.player_active.inverted


game = Game()
game.start()
