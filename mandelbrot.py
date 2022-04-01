import math
import pygame as pg
import pygame_gui

GUI = pygame_gui.elements
WIDTH = 500
HEIGHT = 500
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1


# Pygame has built-in collider detection for rect type objects


class ScreenManager(object):

    def __init__(self, display_x, display_y, game_m):
        self.display_x = display_x
        self.display_y = display_y
        self.ui_manager = pygame_gui.UIManager((WIDTH, HEIGHT))
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

    def plot_fractal(self):
        global max_iter
        max_iter = 20
        print("Plotting the fractal...")
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                print(f'x: {x} | y: {y}')
                # Map pixel coordinates to a complex number, thanks to a built-in python function complex()
                self.c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                                 IM_START + (y / HEIGHT) * (IM_END - IM_START))

                self.m = self.mandelbrot_eqt(self.c)

                # Set the color in correlation with the number of iterations; 255 is the max. value in the grayscale spectrum...
                self.color = 255 - int(self.m * 255 / max_iter)

                screen.set_at((x, y), (self.color, self.color, self.color))

                pg.display.update()

    # EQUATION LINK: https://simple.wikipedia.org/wiki/Mandelbrot_set
    @staticmethod
    def mandelbrot_eqt(c):
        z = 0
        n = 0
        while abs(z) <= 2 and n < max_iter:
            z = z ** 2 + c
            n += 1
        return n


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
        fp.plot_fractal()

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
        pg.quit()


# Run the code
game_m = GameManager()
