import math
import pygame as pg
import pygame_gui

GUI = pygame_gui.elements
WIDTH = 500
HEIGHT = 500


# Pygame has built-in collider detection for rect type objects


class ScreenManager(object):

    def __init__(self, display_x, display_y, game_m):
        self.display_x = display_x
        self.display_y = display_y
        self.ui_manager = pygame_gui.UIManager((800, 600))
        pg.display.set_caption('iMandelbrot')
        self.update_screen_resolution(self.display_x, self.display_y)
        self.game_m = game_m

    @staticmethod
    def update_screen_resolution(display_x, display_y):
        global screen
        screen = pg.display.set_mode([display_x, display_y])

    def update(self):
        screen.fill((255, 255, 255))
        self.ui_manager.update(self.game_m.time_delta)
        self.ui_manager.draw_ui(screen)


class FunctionPlotter(object):

    def __init__(self):
        self.max_iter = 100
        self.plot_fractal()

    @staticmethod
    def normalize(values, actual_bounds, desired_bounds):
        return [desired_bounds[0] + (x - actual_bounds[0]) * (desired_bounds[1] - desired_bounds[0]) / (actual_bounds[1] - actual_bounds[0]) for x in values]

    def plot_fractal(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                self.a = self.normalize([x], (0, WIDTH), (-2, 2))[0]
                self.b = self.normalize([y], (0, HEIGHT), (-2, 2))[0]

                self.n = 0
                self.z = 0

                self.ca = self.a
                self.cb = self.b

                while self.n < 100:
                    self.aa = self.a ** 2 - self.b ** 2
                    self.bb = 2 * self.a * self.b

                    self.a = self.aa + self.ca
                    self.b = self.bb + self.ca

                    if abs(self.a + self.b) > 16:
                        break

                    self.n += 1

                    self.hue = self.normalize(
                        [self.n], (0, self.max_iter), (0, 1))[0]

                    self.hue = self.normalize(
                        [math.sqrt(self.hue)], (0, 1), (0, 255))[0]

                    if self.n == self.max_iter:
                        self.hue = 0

                    screen.set_at((x, y), (self.hue, self.hue, self.hue))


class GameManager(object):

    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.frame_rate = 60
        self.game_running = True
        self.screen_m = ScreenManager(WIDTH, HEIGHT, self)
        self.main_loop()

    def update(self):
        fp = FunctionPlotter()

    def main_loop(self):
        '''
        This is the main loop of the program, where most of the commands are executed!
        '''
        while self.game_running == True:
            self.time_delta = self.clock.tick(self.frame_rate) / 1000.0
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_running = False
                self.screen_m.ui_manager.process_events(event)
            self.screen_m.update()
            self.update()
            pg.display.update()
        pg.quit()


# Run the code
game_m = GameManager()
