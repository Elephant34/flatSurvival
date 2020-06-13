"""Shown when the game is paused
"""

import logging
import pathlib

import arcade

from assets.gui.buttons.buttons import TextButton


class PauseView(arcade.View):
    """A pause screen stopping the game from running

    :param game_view: The top level game window
    :type game_view: arcade.Window
    :param game_view: The main game view to return to it when unpaused
    :type game_view: arcade.View
    """

    def __init__(self, window: arcade.Window, game_view: arcade.View) -> None:
        """Construcotr method
        """

        super().__init__()

        self.window = window

        self.game_view = game_view

        self.width = self.window.width
        self.height = self.window.height

        self.menu_theme = arcade.gui.Theme()

        normal = pathlib.Path("assets/data/buttons/Normal.png")
        hover = pathlib.Path("assets/data/buttons/Hover.png")
        clicked = pathlib.Path("assets/data/buttons/Clicked.png")
        locked = pathlib.Path("assets/data/buttons/Locked.png")

        self.menu_theme.add_button_textures(normal, hover, clicked, locked)

        self.button_list += [
            TextButton(
                self.width / 2,
                350,
                270,
                50,
                "Save and Quit",
                self.exit_game,
                self.menu_theme
            )
        ]

    def on_draw(self) -> None:
        """Draw everything to the screen
        """

        arcade.start_render()

        for button in self.button_list:
            if button.active:
                button.draw()

        arcade.draw_text(
            "Paused",
            self.window.width / 2,
            500,
            arcade.color.WHITE,
            70,
            anchor_x="center",
            anchor_y="center"
        )
        arcade.draw_text(
            "Press ESC or P to resume",
            self.window.width / 2,
            400,
            arcade.color.WHITE,
            30,
            anchor_x="center",
            anchor_y="center"
        )

    def on_key_press(self, key: int, modifiers: int) -> None:
        """handels key presses

        :param key: arcade key index
        :type key: int
        :param modifiers: given if shift or control keys are pressed
        :type modifiers: int
        """

        if key == arcade.key.ESCAPE or key == arcade.key.P:
            logging.info("Resuming game")
            self.window.show_view(self.game_view)

    def exit_game(self) -> None:
        """Saves and quits the game
        """
        logging.info("Exiting game")

        self.game_view.save()

        self.window.close()
