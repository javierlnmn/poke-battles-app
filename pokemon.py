from utils import (
    set_console_color,
    set_console_style,
    reset_console_ansi_escapes,
    read_ascii_art,
    reset_console_style,
)
from config import POKEMON_ASCII_ART_PATH


class Pokemon:
    
    def __init__(self, id, name, visible_name, type, color, stats, abilities):
        self.id = id
        self.name = name
        self.visible_name = visible_name
        self.type = type
        self.color = color
        self.stats = stats
        self.current_hp = int(stats["hp"] / 2)
        self.abilities = abilities

    def __repr__(self) -> str:
        return (
            "["
            + str(self.id)
            + "] "
            + str(self.name)
            + "\n"
            + str(self.type)
            + "\n"
            + str(self.abilities)
            + "\n"
            + str(self.stats)
        )

    def __str__(self) -> str:
        return (
            set_console_style("bright")
            + set_console_color(self.color)
            + self.visible_name
            + reset_console_ansi_escapes()
        )

    def get_ascii_art(self) -> str:
        return (
            set_console_color(self.color)
            + read_ascii_art(POKEMON_ASCII_ART_PATH, self.name)
            + reset_console_ansi_escapes()
        )

    def visual_stats_sprite(self) -> str:
        max_hp = self.stats["hp"]
        current_hp = self.current_hp
        health_percentage = (current_hp / max_hp) * 100
        bar_length = int(health_percentage / 2)

        health_indicator = (
            "HP: "
            + set_console_style("bright")
            + str(current_hp)
            + reset_console_style()
            + " / "
            + str(max_hp)
        )

        health_bar = "[" + "#" * bar_length + "-" * (50 - bar_length) + "]"

        ascii_art = self.get_ascii_art()

        combined_sprite = (
            ascii_art
            + "\n"
            + set_console_color(self.color)
            + health_indicator
            + "\n"
            + health_bar
            + reset_console_ansi_escapes()
        )

        return combined_sprite
