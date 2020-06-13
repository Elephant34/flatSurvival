"""Stores the tile sprites for version: 0.0.1
"""
import pathlib

import arcade


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

        self.player_collides = True


class Void(arcade.Sprite):
    """Creates a void tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/void.png"),
            center_x=center_x,
            center_y=center_y
        )

        self.player_collides = True


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

        self.player_collides = False


class Stone(arcade.Sprite):
    """Creates a stone tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/stone.png"),
            center_x=center_x,
            center_y=center_y
        )

        self.player_collides = False


class Tree(arcade.Sprite):
    """Creates a tree tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/tree.png"),
            center_x=center_x,
            center_y=center_y
        )

        self.player_collides = False


class Wall(arcade.Sprite):
    """Creates a wall tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/wall.png"),
            center_x=center_x,
            center_y=center_y
        )

        self.player_collides = True
