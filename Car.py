import arcade
import os

SPRITE_SCALING = 0.1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


MOVEMENT_SPEED = 5


class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Initializer
        """

        super().__init__(width, height)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)


        self.player1_list = None
        self.player1_sprite = None

        self.player2_list = None
        self.player2_sprite = None
        
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """


        self.player1_list = arcade.SpriteList()
        self.player2_list = arcade.SpriteList()

        self.player1_sprite = Player("images/motorbike.png", SPRITE_SCALING)
        self.player1_sprite.center_x = 50
        self.player1_sprite.center_y = 50
        self.player1_list.append(self.player1_sprite)

        self.player2_sprite = Player("images/motorbike.png", SPRITE_SCALING)
        self.player2_sprite.center_x = 500
        self.player2_sprite.center_y = 50
        self.player2_list.append(self.player2_sprite)


    def on_draw(self):
        """
        Render the screen.
        """


        arcade.start_render()

        self.player1_list.draw()
        self.player2_list.draw()
    def update(self, delta_time):
        """ Movement and game logic """

        self.player1_list.update()
        self.player2_list.update()
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player1_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player1_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player1_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player1_sprite.change_x = MOVEMENT_SPEED


        
        if key == arcade.key.W:
            self.player2_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player2_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player2_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player2_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player1_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player1_sprite.change_x = 0

        if key == arcade.key.W or key == arcade.key.S:
            self.player2_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player2_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()