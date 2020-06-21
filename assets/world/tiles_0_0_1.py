"""Stores the tile sprites for version: 0.0.1
"""
import pathlib

import arcade


class Basic(arcade.Sprite):
    """Creates a bass tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    :param zone: zone coordinates
    :type zone: str
    """

    def __init__(
            self,
            path: pathlib.Path,
            center_x: int,
            center_y: int,
            zone: str
    ) -> None:
        """Constructor method
        """
        super().__init__(
            path,
            center_x=center_x,
            center_y=center_y
        )

        self.player_collides = False

        self.zone = zone


class Unknown(Basic):
    """Creates a unknown tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int, zone: str) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/unknown.png"),
            center_x,
            center_y,
            zone
        )

        self.player_collides = True


class Void(Basic):
    """Creates a void tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int, zone: str) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/void.png"),
            center_x,
            center_y,
            zone
        )

        self.player_collides = True


class Grass(Basic):
    """Creates a grass tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int, zone: str) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/grass.png"),
            center_x,
            center_y,
            zone
        )


class Stone(Basic):
    """Creates a stone tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int, zone: str) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/stone.png"),
            center_x,
            center_y,
            zone
        )


class Tree(Basic):
    """Creates a tree tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int, zone: str) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/tree.png"),
            center_x,
            center_y,
            zone
        )


class Wall(Basic):
    """Creates a wall tile sprite

    :param center_x: x position
    :type center_x: int
    :param center_y: y position
    :type center_y: int
    """

    def __init__(self, center_x: int, center_y: int, zone: str) -> None:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/tiles/wall.png"),
            center_x,
            center_y,
            zone
        )

        self.player_collides = True
