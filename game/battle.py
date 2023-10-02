from game.pokemon import Pokemon
from utils.ascii_art import (
    set_console_color,
    set_console_background,
    reset_console_ansi_escapes,
)


class Battle:
    def __init__(self, pokemon_1: Pokemon, pokemon_2: Pokemon):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.winner = None

    def get_battle_state(self):
        battle_state = "\n".join(
            [
                row[0]
                + (' ')*15
                + row[1]
                for row in zip(
                    self.pokemon_1.get_visual_stats_sprite().split("\n"),
                    self.pokemon_2.get_visual_stats_sprite().split("\n"),
                )
            ]
        )
        
        return battle_state
