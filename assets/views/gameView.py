"""Loads and controls the main game
"""
import logging

from assets.world.loadWorldData import load_data

import arcade


class GameView(arcade.View):
    """The main game screen with all game elements

        :param window: The main window used to switch views
        :type window: arcade.Window
    """

    def __init__(self, window: arcade.Window) -> None:
        """Constructer method
        """

        super().__init__()

        logging.info("On game screen")

        self.winodw = window

        self.world_data = load_data()

    def on_draw(self) -> None:
        """Draws all game objects to the screen
        """
        arcade.start_render()
