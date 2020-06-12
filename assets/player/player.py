"""The user controled player character
"""
import pathlib

import arcade


class Player(arcade.Sprite):
    """Generates a player sprite to be drawn

    :param player_data: Player data from world save
    :type player_data: dict
    :return: Returns a sprite to draw on the screen
    :rtype: arcade.Sprite
    """

    def __init__(self, player_data: dict) -> arcade.Sprite:
        """Constructor method
        """
        super().__init__(
            pathlib.Path("assets/data/player/player.png")
        )

        self.player_data = player_data

        self.set_position(
            self.player_data["pos"][0],
            self.player_data["pos"][1]
        )

        self.movement_keys = {
            "up": [
                arcade.key.UP,
                arcade.key.W
            ],
            "down": [
                arcade.key.DOWN,
                arcade.key.S
            ],
            "left": [
                arcade.key.LEFT,
                arcade.key.A
            ],
            "right": [
                arcade.key.RIGHT,
                arcade.key.D
            ],
        }

        self.movement_speed = self.player_data["multipliers"]["speed"] * 5

        self.down_pressed = False
        self.up_pressed = False

    def on_key_press(self, key: int, modifiers: int) -> None:
        """handels key presses

        :param key: arcade key index
        :type key: int
        :param modifiers: given if shift or control keys are pressed
        :type modifiers: int
        """

        if key in self.movement_keys["up"]:
            self.change_y += self.movement_speed
            self.up_pressed = True
        elif key in self.movement_keys["down"]:
            self.change_y -= self.movement_speed
            self.down_pressed = True
        elif key in self.movement_keys["left"]:
            self.change_x -= self.movement_speed
        elif key in self.movement_keys["right"]:
            self.change_x += self.movement_speed

    def on_key_release(self, key: int, modifiers: int) -> None:
        """handles key releases

        :param key: arcade key index
        :type key: int
        :param modifiers: gives if modifer keys are also pressed
        :type modifiers: int
        """

        if key in self.movement_keys["up"]:
            self.change_y -= self.movement_speed
            self.up_pressed = False
        elif key in self.movement_keys["down"]:
            self.change_y += self.movement_speed
            self.down_pressed = False
        elif key in self.movement_keys["left"]:
            self.change_x += self.movement_speed
        elif key in self.movement_keys["right"]:
            self.change_x -= self.movement_speed

    def on_update(self, dt: float) -> None:
        """Updates the player

        :param dt: delta time since last frame
        :type dt: float
        """

        # Workaround for weird collision issue
        if self.down_pressed and not self.up_pressed:
            self.change_y = -self.movement_speed
        if self.up_pressed and not self.down_pressed:
            self.change_y = self.movement_speed
