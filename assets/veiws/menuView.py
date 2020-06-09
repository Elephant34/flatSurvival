"""
The main menu screen loaded when the game is started
"""
import logging
import pathlib

import arcade

from assets.gui.buttons.buttons import TextButton


class MenuView(arcade.View):
    """The main menu screen

    :param window: The main game window to access width and height
    :type window: arcade.Window
    """

    def __init__(self, window: arcade.Window) -> None:
        """Constructor method
        """
        super().__init__()

        logging.info("Menu loaded")

        self.width = window.width
        self.height = window.height

        self.window = window

        self.menu_theme = arcade.gui.Theme()

        normal = pathlib.Path("assets/data/buttons/Normal.png")
        hover = pathlib.Path("assets/data/buttons/Hover.png")
        clicked = pathlib.Path("assets/data/buttons/Clicked.png")
        locked = pathlib.Path("assets/data/buttons/Locked.png")

        self.menu_theme.add_button_textures(normal, hover, clicked, locked)

    def on_show(self) -> None:
        """Loads all the text and buttons
        """

        # Adds all of the buttons to the menu
        self.button_list += [
            TextButton(
                self.width / 2,
                350,
                200,
                50,
                "Play",
                self.start_game,
                self.menu_theme
            ),
            TextButton(
                self.width / 2,
                285,
                200,
                50,
                "Credits",
                self.load_credits,
                self.menu_theme
            ),
            TextButton(
                self.width / 2,
                170,
                200,
                50,
                "Exit",
                self.exit_game,
                self.menu_theme
            )
        ]

    def on_draw(self) -> None:
        """Draws all menu objects to the screen
        """
        super().on_draw()

        for button in self.button_list:
            if button.active:
                button.draw()

    def start_game(self) -> None:
        """Switchs to the game veiw called by button press
        """
        logging.info("Switching to game veiw")

    def exit_game(self) -> None:
        """Quits the game and closes the window
        """
        logging.info("Exiting game")
        self.window.close()

    def load_credits(self) -> None:
        """Loads the games credits
        WIP
        """
        # TODO
        logging.info("Load credits")
