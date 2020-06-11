"""Generates the world tilemap
Different loader called depending on the game version
This ensures saves are backwards compatable
"""
import arcade

from assets.world import tiles_0_0_1


def load_tilemap(save_version: str, tiledata: list) -> arcade.SpriteList:
    """Will return a sprite list of all tilemap entities

    :param save_version: The version the save was made for compatability
    :type save_version: str
    :param tiledata: The tile list from the world save
    :type tiledata: list
    :return: An arcade sprite list which can be draw to the screen
    :rtype: arcade.SpriteList
    """

    if save_version == "0.0.1":
        return load_0_0_1(tiledata)


def load_0_0_1(tiledata) -> arcade.SpriteList:
    """Generator for dev version 0.0.1

    :param tiledata: The tile list from the world save
    :type tiledata: list
    :return: List of sprites for easy drawing
    :rtype: arcade.SpriteList
    """

    tile_lookup = {
        "0": tiles_0_0_1.Grass,
        "unknown": tiles_0_0_1.Unknown
    }

    tilemap = arcade.SpriteList(
        use_spatial_hash=True,
        is_static=True
    )

    for row_index, row in enumerate(tiledata):
        for cell_index, cell in enumerate(row):
            if list(cell.keys())[0] in tile_lookup:
                tile = tile_lookup[list(cell.keys())[0]](
                    center_x=((cell_index+1)*64)-32,
                    center_y=((row_index+1)*64)-32
                )
            else:
                tile = tile_lookup["unknown"](
                    center_x=((cell_index+1)*64)-32,
                    center_y=((row_index+1)*64)-32
                )

            tilemap.append(
                tile
            )

    return tilemap
