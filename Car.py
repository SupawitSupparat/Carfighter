import arcade
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
class CarWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.GRAY)
        
        self.car_sprite = arcade.Sprite('images/motorbike.png', 0.1)
        self.car_sprite.set_position(300,300)
      
 
    def on_draw(self):
        arcade.start_render()
        self.car_sprite.draw()

def main():
    window = CarWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()