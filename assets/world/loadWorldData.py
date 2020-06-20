"""Methods for the loading and generation of the game data
"""
import json
import logging
import pathlib

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
        "mobs": {
            "passive": generate_passive(),
            "hostile": []
        },
        "tilemap": generate_tilemap(),
    }

    with save_path.open("w") as save:
        json.dump(data, save, indent=4)


def generate_player() -> dict:
    """Generates new player data

    :return: Returns a dict of player data
    :rtype: dict
    """

    logging.info("Generating player")

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

    logging.info("Generating tilemap")

    zone_path = pathlib.Path("assets/data/zones/")

    if not zone_path.exists():
        zone_path.mkdir()

    zone_size = 20

    # Generates the first few zones
    tile_zones = {
        "size": zone_size,
        "0_0": str(generate_zone(0, 0, zone_size)),
        "1_0": str(generate_zone(1, 0, zone_size)),
        "0_1": str(generate_zone(0, 1, zone_size)),
        "1_1": str(generate_zone(1, 1, zone_size)),
    }

    return tile_zones


def generate_zone(x: int, y: int, size: int) -> pathlib.Path:
    """Generates a zone of the tilemap

    :param x: X grid number
    :type x: int
    :param y: y grid number
    :type y: int
    :param size: how many tiles is the zone length
    :type size: int
    :return: Path to the zone save file
    :rtype: pathlib.Path
    """

    zone_path = pathlib.Path(
        "assets/data/zones/{}_{}.json".format(
            x,
            y
        )
    )

    zone_tilemap = []

    if y == 0:
        zone_tilemap = [[{0: 0} for i in range(size)]]

    for i in range(size):

        row = [{1: 0} for i in range(size)]
        if x == 0:
            row[0] = {0: 0}

        zone_tilemap.insert(
            i+1,
            row
        )

    with zone_path.open("w") as save:
        json.dump(zone_tilemap, save, indent=4)

    return zone_path


def generate_passive() -> list:
    """Generates some passive mobs around the players spawn

    :return: list of the mob data
    :rtype: list
    """

    logging.info("Generating passive")

    return []


def add_zone(x: int, y: int, size: int) -> pathlib.Path:
    """Creates a new zone file, adds it to save and return the path directly

    :param x: X position of zone
    :type x: int
    :param y: Y position of zone
    :type y: int
    :param size: How many cells across the zone is
    :type size: int
    :return: The path object to the zone save
    :rtype: pathlib.Path
    """

    logging.info("Adding zone to world")

    global save_path

    zone_path = generate_zone(x, y, size)

    zone_name = "{}_{}".format(x, y)

    with save_path.open() as save:
        data = json.load(save)

    data["tilemap"][zone_name] = str(zone_path)

    with save_path.open("w") as save:
        json.dump(data, save, indent=4)

    return zone_path
