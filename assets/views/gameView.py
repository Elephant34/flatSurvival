"""Loads and controls the main game
"""
import json
import logging
import pathlib

import arcade

from assets.player.player import Player
from assets.views.pauseView import PauseView
from assets.world.generateTilemap import get_tilemap
from assets.world.loadWorldData import load_data


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

        self.player = Player(self.world_data["player"])

        self.tilemap = get_tilemap(
            self.world_data["version"],
            self.world_data["tilemap"]
        )

        self.rendered_zones, self.collision_list = self.tilemap.load_tilemap(
            self.player.position
        )

        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                         self.collision_list)

        arcade.set_viewport(
            self.player.left - 400,
            self.player.right + 400,
            self.player.bottom - 300,
            self.player.top + 300
        )

        self.save_path = pathlib.Path("assets/data/worldSave.json")
        arcade.schedule(
            lambda e: self.save,
            10
        )

    def on_draw(self) -> None:
        """Draws all game objects to the screen
        """
        arcade.start_render()

        self.rendered_zones.draw()
        self.player.draw()

    def on_update(self, dt: float) -> None:
        """Run whenever the game screen is updated

        :param dt: Delta time between frames
        :type dt: float
        """

        self.physics_engine.update()

        self.player.on_update(dt)

        if not self.tilemap.validate_zones(self.player.position):
            self.rendered_zones, self.collision_list = self.tilemap.load_tilemap(  # noqa E501
                self.player.position
            )
            self.physics_engine.walls = self.collision_list

        self.world_data["player"]["pos"] = list(self.player.position)

        current_viewport = arcade.get_viewport()

        view_x, view_y = 0, 0

        if self.player.left < current_viewport[0] + 100:
            view_x = self.player.change_x
        if self.player.right > current_viewport[1] - 100:
            view_x = self.player.change_x
        if self.player.bottom < current_viewport[2] + 100:
            view_y = self.player.change_y
        if self.player.top > current_viewport[3] - 100:
            view_y = self.player.change_y

        arcade.set_viewport(
                current_viewport[0] + view_x,
                current_viewport[1] + view_x,
                current_viewport[2] + view_y,
                current_viewport[3] + view_y
            )

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

    def save(self) -> None:
        """Writes the current world_data to the save file
        """

        save_data = self.world_data

        with self.save_path.open("w") as save:
            json.dump(save_data, save, indent=4)
