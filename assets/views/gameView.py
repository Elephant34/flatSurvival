"""Loads and controls the main game
"""
import logging

from assets.world.loadWorldData import load_data
from assets.world.generateTilemap import load_tilemap
from assets.player.player import Player
from assets.views.pauseView import PauseView

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

        self.window = window

        self.width = window.width
        self.height = window.height

        self.world_data = load_data()

        self.tilemap, self.collision_list = load_tilemap(
            self.world_data["version"],
            self.world_data["tilemap"]
        )

        self.player = Player(self.world_data["player"])

        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                         self.collision_list)

    def on_draw(self) -> None:
        """Draws all game objects to the screen
        """
        arcade.start_render()

        self.tilemap.draw()
        self.player.draw()

    def on_update(self, dt: float) -> None:
        """Run whenever the game screen is updated

        :param dt: Delta time between frames
        :type dt: float
        """

        self.physics_engine.update()

        self.player.on_update(dt)

        self.world_data["player"]["pos"] = list(self.player.position)

    def on_key_press(self, key: int, modifiers: int) -> None:
        """handels key presses

        :param key: arcade key index
        :type key: int
        :param modifiers: given if shift or control keys are pressed
        :type modifiers: int
        """

        if key == arcade.key.ESCAPE or key == arcade.key.P:
            pause_view = PauseView(self.window, self)
            self.window.show_view(pause_view)

        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key: int, modifiers: int) -> None:
        """handles key releases

        :param key: arcade key index
        :type key: int
        :param modifiers: gives if modifer keys are also pressed
        :type modifiers: int
        """

        self.player.on_key_release(key, modifiers)
