"""Generates the world tilemap
Different loader called depending on the game version
This ensures saves are backwards compatable
"""
import json
import logging
import pathlib
import time
from collections import Counter

import arcade

from assets.world import tiles_0_0_1
from assets.world.loadWorldData import add_zone


class Save_0_0_1:
    """Class to handle the world tilemap

    :param save_version: The version of the save for back compatability
    :type save_version: str
    :param tiledata: Dict with paths of the tile zones
    :type tiledata: dict
    """

    def __init__(self, save_version: str, tiledata: dict) -> None:
        """Constructor method
        """

        self.save_version = save_version
        self.tiledata = tiledata

        self.zone_size = tiledata["size"]
        self.zone_length = self.zone_size * 64

        self.tile_lookup = {
            "unknown": tiles_0_0_1.Unknown,
            "0": tiles_0_0_1.Void,
            "1": tiles_0_0_1.Grass,
            "2": tiles_0_0_1.Stone,
            "3": tiles_0_0_1.Tree,
            "4": tiles_0_0_1.Wall,
        }

        self.loaded_zones = []

        logging.info("Tilemap instance created")

    def load_tilemap(self, player_pos: tuple) -> arcade.SpriteList:
        """Loads all the rendered tilemap zones

        :param player_pos: Gets the player current postition to load local
        :type player_pos: tuple
        :return: Returns two lists: all tiles and collision tiles
        :rtype: arcade.SpriteList
        """

        logging.info("Tilemap loading")

        self.player_pos = player_pos

        if not self.loaded_zones:
            self.loaded_zones = self.get_player_zones()
            zones_to_load = self.loaded_zones

            self.tilemap = arcade.SpriteList(
                use_spatial_hash=True,
                is_static=True
            )
            self.collision_map = arcade.SpriteList(
                use_spatial_hash=True,
                is_static=True
            )
        else:
            set(map(self.remove_zones, self.tilemap))

            zones_to_load = (
                set(self.get_player_zones()) ^ set(self.loaded_zones)
            )

        start = time.time()
        set(map(self.load_zone, zones_to_load))
        print(time.time()-start)

        self.loaded_zones = self.get_player_zones()

        logging.info("Tilemap loaded")

        return self.tilemap, self.collision_map

    def remove_zones(self, tile: tiles_0_0_1.Basic) -> None:
        """Used when updating zones to clear old zones

        :param tile: Tile to test
        :type tile: tiles_0_0_1.Basic
        """
        if tile.zone not in self.loaded_zones:
            self.tilemap.remove(tile)

    def load_zone(self, zone: str) -> None:
        """Loads a given zone and adds it to tilemap

        :param zone: The zone to load
        :type zone: str
        """
        self.zone_x = int(zone.split("_")[0])
        self.zone_y = int(zone.split("_")[1])

        self.zone = zone

        try:
            zone_path = pathlib.Path(self.tiledata[zone])
        except KeyError:
            self.tiledata[zone] = str(add_zone(
                self.zone_x,
                self.zone_y,
                self.zone_size
            ))
            zone_path = pathlib.Path(self.tiledata[zone])

        with zone_path.open() as save:
            data = json.load(save)

        set(map(self.load_row, enumerate(data)))

    def load_row(self, row_data: enumerate) -> None:
        """Loads the sprites in a row

        :param row_data: position and value of the row
        :type row: enumerate
        """

        self.row_index = row_data[0]
        self.row = row_data[1]

        set(map(self.load_column, enumerate(self.row)))

    def load_column(self, column_data: enumerate) -> None:
        """Loads the sprites in a column

        :param column_data: The position and value of a column
        :type column_data: enumerate
        """

        cell_index = column_data[0]
        cell = column_data[1]

        cell_x = ((((cell_index+1)*64)-128) +
                  (self.zone_x*self.zone_length))
        cell_y = ((((self.row_index+1)*64)-128) +
                  (self.zone_y*self.zone_length))

        if list(cell.keys())[0] in self.tile_lookup:
            tile = self.tile_lookup[list(cell.keys())[0]](
                center_x=cell_x,
                center_y=cell_y,
                zone=self.zone
            )
        else:
            tile = self.tile_lookup["unknown"](
                center_x=cell_x,
                center_y=cell_y,
                zone=self.zone
            )

        self.tilemap.append(
            tile
        )
        if tile.player_collides:
            self.collision_map.append(
                tile
            )

    def validate_zones(self, player_pos: tuple) -> bool:
        """Checks if the the next zone should be loaded

        :param player_pos: Current player position
        :type player_pos: tuple
        :return: true if the loaded tiles are correct false otherwise
        :rtype: bool
        """

        self.player_pos = player_pos
        self.player_zones = self.get_player_zones()

        return Counter(self.player_zones) == Counter(self.loaded_zones)

    def get_player_zones(self) -> list:
        """Gets the zone(s) the player is in

        :return: list of zone string codes
        :rtype: list
        """

        zone_list = []

        x_zone = int((self.player_pos[0]+128) // self.zone_length)
        y_zone = int((self.player_pos[1]+128) // self.zone_length)

        zone_list.append("{}_{}".format(x_zone, y_zone))

        zone_list.append("{}_{}".format(x_zone+1, y_zone))
        zone_list.append("{}_{}".format(x_zone, y_zone+1))
        zone_list.append("{}_{}".format(x_zone+1, y_zone+1))

        clear_left = False
        clear_down = False

        if x_zone-1 >= 0:
            clear_left = True

        if y_zone-1 >= 0:
            clear_down = True

        if clear_down:
            zone_list.append("{}_{}".format(x_zone, y_zone-1))
            zone_list.append("{}_{}".format(x_zone+1, y_zone-1))
        if clear_left:
            zone_list.append("{}_{}".format(x_zone-1, y_zone))
            zone_list.append("{}_{}".format(x_zone-1, y_zone+1))
        if clear_left and clear_down:
            zone_list.append("{}_{}".format(x_zone-1, y_zone-1))

        return zone_list


def get_tilemap(save_version: str, tiledata: dict) -> type:
    """Selects the correct tilemap for the save version

    :param save_version: The save files generated version
    :type save_version: str
    :param tiledata: The tiledata from the worldsave
    :type tiledata: dict
    :return: A class which can load the tilemap
    :rtype: type
    """

    if save_version == "0.0.1":
        return Save_0_0_1(save_version, tiledata)
