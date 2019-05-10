import arcade
import os


SPRITE_SCALING = 0.1

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SPRITE_SCALING_LASER = 0.8
centerx = 0
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
        self.frame_count = 0
        self.player1_wall = None
        self.player1_list = None
        self.player1_sprite = None
        self.bullet1_list = None
        self.player1_check = True
        self.player1_currentkey = None


        self.player2_list = None
        self.player2_sprite = None
        self.plater2_wall = None
        self.bullet2_list = None
        self.player2_check = True
        self.player2_currentkey =None

        self.instruct = True
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """


        self.player1_list = arcade.SpriteList()
        self.player2_list = arcade.SpriteList()
        self.bullet1_list = arcade.SpriteList()
        self.bullet2_list = arcade.SpriteList()
        

        self.player1_sprite = Player("images/player1_block.png")
        self.player1_sprite.center_x = 50
        self.player1_sprite.center_y = 400
        self.player1_list.append(self.player1_sprite)
        self.player2_sprite = Player("images/player2_block.png")
        self.player2_sprite.center_x = 1150
        self.player2_sprite.center_y = 400
        self.player2_list.append(self.player2_sprite)



    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        if self.instruct == True :
            page_texture = arcade.load_texture("images/instruction.png")
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)    

        elif self.instruct == False:
            self.player1_list.draw()
            self.player2_list.draw()
            self.bullet1_list.draw()
            self.bullet2_list.draw()  
            if self.player1_check == False :
                arcade.draw_text("Player 2 Win", 400, 400, arcade.color.WHITE, 50)
            elif self.player2_check == False : 
                arcade.draw_text("Player 1 Win", 400, 400, arcade.color.WHITE, 50)

    def update(self, delta_time):
        """ Movement and game logic """
        self.frame_count += 1
        
        if self.player1_check == True and self.player2_check ==True :
            if self.frame_count % 2 == 0:
                    bullet1 = arcade.Sprite("images/player1_block.png")
                    bullet1.center_x = self.player1_sprite.center_x 
                    bullet1.angle = -90
                    bullet1.top = self.player1_sprite.top
                    self.bullet1_list.append(bullet1)


                    bullet2 = arcade.Sprite("images/player2_block.png")
                    bullet2.center_x = self.player2_sprite.center_x
                    bullet2.angle = -90
                    bullet2.top = self.player2_sprite.top
                    self.bullet2_list.append(bullet2)

                    self.player1_list.update()
                    self.player2_list.update()
                    self.bullet1_list.update()
                    self.bullet2_list.update()
            
        Player1_hit_Player2 = arcade.check_for_collision_with_list(self.player1_sprite, self.bullet2_list)

        Player2_hit_Player1 = arcade.check_for_collision_with_list(self.player2_sprite, self.bullet1_list)
  

        if len(Player1_hit_Player2) > 0 :
            self.player1_check = False                 
        elif len(Player2_hit_Player1) > 0 :
            self.player2_check = False
        

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.W and self.player1_currentkey != "S":
            self.player1_currentkey = "W"
            self.player1_sprite.change_x = 0
            self.player1_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S and self.player1_currentkey != "W":
            self.player1_currentkey = "S"
            self.player1_sprite.change_x = 0
            self.player1_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A and self.player1_currentkey != "D":
            self.player1_currentkey = "A"
            self.player1_sprite.change_y = 0
            self.player1_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D and self.player1_currentkey != "A":
            self.player1_currentkey = "D"
            self.player1_sprite.change_y = 0
            self.player1_sprite.change_x = MOVEMENT_SPEED
        
        if key == arcade.key.UP and self.player2_currentkey != "DOWN"  :
            self.player2_currentkey = "UP"
            self.player2_sprite.change_x = 0
            self.player2_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN and self.player2_currentkey != "UP":
            self.player2_currentkey = "DOWN"
            self.player2_sprite.change_x = 0
            self.player2_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT and self.player2_currentkey != "RIGHT":
            self.player2_currentkey = "LEFT"
            self.player2_sprite.change_y = 0
            self.player2_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT and self.player2_currentkey != "LEFT":
            self.player2_currentkey = "RIGHT"
            self.player2_sprite.change_y = 0
            self.player2_sprite.change_x = MOVEMENT_SPEED

        if key == arcade.key.SPACE:
            self.setup()
            self.instruct = False
            self.player1_check = True
            self.player2_check = True
            self.player1_currentkey = None
            self.player2_currentkey = None


    # def on_key_release(self, key, modifiers):
    #     """Called when the user releases a key. """

    #     if key == arcade.key.UP or key == arcade.key.DOWN:
    #         self.player2_sprite.change_y = 0
    #     elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
    #         self.player2_sprite.change_x = 0

    #     if key == arcade.key.W or key == arcade.key.S:
    #         self.player1_sprite.change_y = 0
    #     elif key == arcade.key.A or key == arcade.key.D:
    #         self.player1_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()