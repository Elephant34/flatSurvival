"""Methods for the loading and generation of the game data
"""
import logging
import pathlib
import json

from assets.data import version


save_path = pathlib.Path("assets/data/worldSave.json")


def load_data() -> dict:
    """Will read the world save or create a new one

    :return: A dictionary of the world save
    :rtype: dict
    """

    global save_path

    if not save_path.exists():
        generate_new_world()

    logging.info("Reading world save")

    with save_path.open() as save:
        data = json.load(save)

    return data


def generate_new_world() -> None:
    """Makes a new worldSave.json file and populates it with defaults
    """

    logging.info("Generating new world save")

    global save_path

    data = {
        "version": version.version,
        "time": 0,
        "player": generate_player(),
        "tilemap": generate_tilemap(),
        "mobs": {
            "passive": generate_passive(),
            "hostile": []
        }
    }

    with save_path.open("w") as save:
        json.dump(data, save, indent=4)


def generate_player() -> dict:
    """Generates new player data

    :return: Returns a dict of player data
    :rtype: dict
    """

    player_data = {
        "pos": [100, 100],
        "health": 100,
        "hunger": 100,
        "multipliers": {
            "speed": 1,
            "mineing": 1,
            "damage": 1
        },
        "inventory": {
            "hand": None,
            "slots": []
        }
    }

    return player_data


def generate_tilemap() -> list:
    """Generates the world terrain tilemap
    WIP so only returns grass for now

    :return: returns a 2d list of tile id's
    :rtype: list
    """

    tilemap = [
        [0 for i in range(30)] for i in range(30)
    ]

    return tilemap


def generate_passive() -> list:
    """Generates some passive mobs around the players spawn

    :return: list of the mob data
    :rtype: list
    """

    return []
