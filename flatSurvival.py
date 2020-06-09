"""
The entry point to start the game
"""
from datetime import datetime
import logging
import pathlib

from assets.views.menuView import MenuView

import arcade


def run() -> None:
    """Loads a new game window
    """

    log_path = pathlib.Path("assets/data/logs/")

    if not log_path.exists():
        log_path.mkdir()

    log_list = list(log_path.rglob("*.log"))
    if len(log_list) > 10:
        pathlib.Path(log_list[0]).unlink()

    logging.basicConfig(
        filename="assets/data/logs/{}.log".format(
            str(datetime.now())[:-7].replace(":", ".")
        ),
        level=logging.INFO
    )
    logging.info("Game Started")

    window = arcade.Window(
        800,
        600,
        "Flat Survival"
    )
    menu_view = MenuView(window)
    window.show_view(menu_view)
    try:
        arcade.run()
    except OSError:
        pass


if __name__ == "__main__":
    run()
