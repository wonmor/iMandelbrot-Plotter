import pygame as pg

# Pygame has built-in collider detection for rect type objects


class ScreenManager(object):
    def __init__(self, display_x, display_y):
        self.display_x = display_x
        self.display_y = display_y

    def update_screen_resolution(self):
        self.screen = pg.display.set_mode([self.display_x, self.display_y])

    def update(self):
        self.screen.fill((255, 255, 255))


class GameManager(object):
    def __init__(self):
        self.game_running = True
        self.main_loop()

    def update(self):
        pass

    def main_loop(self):
        '''
        This is the main loop of the program, where most of the commands are executed!
        '''
        screen_m = ScreenManager(1280, 720)
        while self.game_running == True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_running = False
            screen_m.update()
            self.update()
            pg.display.update()

# Run the code
game_m = GameManager()
                
