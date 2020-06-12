"""Shown when the game is paused
"""

import arcade


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

    def on_draw(self) -> None:
        """Draw everything to the screen
        """

        arcade.start_render()

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
            300,
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
            self.window.show_view(self.game_view)
