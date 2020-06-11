"""Stores the tile sprites for version: 0.0.1
"""
import pathlib

import arcade


class Grass(arcade.Sprite):
    """Creates a grass tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/grass.png"),
            center_x=center_x,
            center_y=center_y
        )


class Unknown(arcade.Sprite):
    """Creates a unknown tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/unknown.png"),
            center_x=center_x,
            center_y=center_y
        )
