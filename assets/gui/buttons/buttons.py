"""
Contains all button classes
"""
import arcade


class TextButton(arcade.gui.TextButton):
    """A simple text box

    :param x: x position of button
    :type x: int
    :param y: y position of button
    :type y: int
    :param width: button width
    :type width: int
    :param height: button height
    :type height: int
    :param text: text to display on button
    :type text: str
    :param function: function to call when button is pressed
    :type function: callable
    :param theme: button images in an arcade theme
    :type theme: arcade.Theme
    """

    def __init__(
                self,
                x: int,
                y: int,
                width: int,
                height: int,
                text: str,
                function: callable,
                theme: arcade.Theme
            ) -> None:
        """Constructor method
        """

        super().__init__(
            x,
            y,
            width,
            height,
            text=text,
            theme=theme
        )
        self.font_size = 30

        self.function = function

        self.locked = False

    def on_press(self) -> None:
        """Called when the button is pressed
        """
        if not self.locked:
            self.pressed = True

    def on_release(self) -> None:
        """Called when the button is realeased"""
        if self.pressed:
            self.function()
            self.pressed = False

    def draw_texture_theme(self) -> None:
        """Draws the theme items to the button
        """
        if self.locked:
            arcade.draw_texture_rectangle(self.center_x, self.center_y,
                                          self.width, self.height,
                                          self.locked_texture
                                          )
        elif self.pressed:
            arcade.draw_texture_rectangle(self.center_x, self.center_y,
                                          self.width, self.height,
                                          self.clicked_texture
                                          )
        else:
            arcade.draw_texture_rectangle(self.center_x, self.center_y,
                                          self.width, self.height,
                                          self.normal_texture
                                          )
