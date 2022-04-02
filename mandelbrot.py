import math
import pygame as pg
import pygame_gui

GUI = pygame_gui.elements
# FONT = pg.font.Font('fonts/LeagueSpartan-SemiBold.ttf', 32)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

WIDTH = 400
HEIGHT = 400
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1


# Pygame has built-in collider detection for rect type objects


class ScreenManager(object):

    def __init__(self, game_m):
        self.display_x = SCREEN_WIDTH
        self.display_y = SCREEN_HEIGHT
        self.ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.label_layout_rect = pg.Rect(30, 20, 100, 20)
        pg.display.set_caption('iMandelbrot')
        self.update_screen_resolution(self.display_x, self.display_y)
        self.game_m = game_m

    @staticmethod
    def update_screen_resolution(display_x, display_y):
        global screen
        screen = pg.display.set_mode([display_x, display_y], pg.DOUBLEBUF)

    def update(self):
        screen.fill((255, 255, 255))
        self.ui_manager.update(self.game_m.time_delta)
        self.ui_manager.draw_ui(screen)

    def show_labels(self):
        pass


class FunctionPlotter(object):

    def __init__(self, game_m):
        self.y_axis = HEIGHT // 2
        self.x_axis = WIDTH // 1.5 + 30
        self.scale = 150
        self.max_iter = 50
        self.game_m = game_m

    def plot_fractal(self):
        print("Plotting the fractal...")
        for x in range(WIDTH):
            for y in range(HEIGHT // 2 + 1):
                print(f'x: {x} | y: {y}')
                # Map pixel coordinates to a complex number, thanks to a built-in python function complex()
                self.c = complex(float(x - self.x_axis) / self.scale,
                                 float(y - self.y_axis) / self.scale)

                self.rounded_c = round(float(
                    x - self.x_axis) / self.scale, 2) + round(float(y - self.y_axis) / self.scale, 2) * 1j

                self.m = self.mandelbrot_eqt(
                    self.c, self.rounded_c, self.max_iter)

                # Set the color in correlation with the number of iterations; 255 is the max. value in the grayscale spectrum...
                self.color = 255 - int(self.m * 255 / self.max_iter)

                self.percent = f'{round((x / WIDTH) * 100, 2)} %' if x != 399 and y != 200 else '100.0 %'

                print(self.percent)

                # Only plot the top portion of the fractal for performance reasons
                screen.set_at((x + ((SCREEN_WIDTH // 2) - (WIDTH // 2)), y +
                              (SCREEN_HEIGHT // 8)), (self.color, self.color, self.color))

                # Mirror the top part of the fractal on the bottom
                screen.set_at((x + ((SCREEN_WIDTH // 2) - (WIDTH // 2)), HEIGHT -
                              y + (SCREEN_HEIGHT // 8)), (self.color, self.color, self.color))

                pg.display.update()

        print("Plotting successfuly completed!")
        self.game_m.fractal_plotted = True

    # EQUATION LINK: https://simple.wikipedia.org/wiki/Mandelbrot_set
    @staticmethod
    def mandelbrot_eqt(c, rounded_c, max_iter):
        z = 0
        n = 0

        while abs(z) <= 2 and n < max_iter:
            z = z ** 2 + c
            rounded_z = complex(round(z.real, 2), round(z.imag, 2))
            print(f'{rounded_z} = {rounded_z}^2 + {rounded_c}'.replace('j', 'i'))

            n += 1

        return n


class GameManager(object):

    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.frame_rate = 60
        self.game_running = True
        self.screen_m = ScreenManager(self)
        self.fractal_plotted = False
        self.logo_img = pg.image.load('logo.png')
        self.logo_img = pg.transform.scale(self.logo_img, (self.logo_img.get_width() // 3.5, self.logo_img.get_height() // 3.5))
        self.main_loop()

    def update(self):
        fp = FunctionPlotter(self)
        # If the fractal is not formed yet...
        if not self.fractal_plotted:
            # Placeholder rectangle to cover the area where the fractal will be generated
            pg.draw.rect(screen, (211, 211, 211), pg.Rect(
                ((SCREEN_WIDTH // 2) - (WIDTH // 2)), SCREEN_HEIGHT // 8, 400, 400))

            # Display the logo
            screen.blit(self.logo_img, ((SCREEN_WIDTH // 2) - (self.logo_img.get_width() // 2), (SCREEN_HEIGHT // 8 + HEIGHT // 2) - (self.logo_img.get_height() // 2)))

            self.screen_m.show_labels()
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
