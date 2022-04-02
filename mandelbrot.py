import pygame as pg

'''
CONSTANTS
'''

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

WIDTH = 400
HEIGHT = 400
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

WINDOW_BAR_BUTTON_SIZE = 15
WINDOW_BAR_BUTTON_GAP = 20
WINDOW_BAR_TITLE_SIZE = 45

PERSIAN_RED = (202, 48, 47)
ASIAN_YELLOW = (252, 194, 1)  # Just a joke (I am Asian btw)
TRUDEAU_GREEN = (19, 135, 21)  # Yes
JET_BLACK = (0, 0, 0)
SMOKEY_GRAY = (70, 70, 70)
BARELY_GRAY = (211, 211, 211)
BLEACHED_WHITE = (255, 255, 255)

EQUATION_LABEL = 'EQUATION_LABEL'
EQUATION_CONTENT = 'EQUATION_CONTENT'
START_BUTTON = 'START_BUTTON'


# Pygame has built-in collider detection for rect type objects


class ScreenManager(object):

    def __init__(self, game_m):
        self.display_x = SCREEN_WIDTH
        self.display_y = SCREEN_HEIGHT

        pg.display.set_caption('iMandelbrot')

        self.update_screen_resolution(self.display_x, self.display_y)

        self.game_m = game_m

        self.font = pg.font.Font('fonts/LeagueSpartan-ExtraLight.ttf', 21)
        self.font_bold = pg.font.Font('fonts/LeagueSpartan-SemiBold.ttf', 18)

        self.mono_font_bold = pg.font.Font('fonts/RobotoMono-Medium.ttf', 18)
        self.mono_font_sm = pg.font.Font('fonts/RobotoMono-Regular.ttf', 14)

    @staticmethod
    def update_screen_resolution(display_x, display_y):
        global screen
        screen = pg.display.set_mode([display_x, display_y], pg.DOUBLEBUF)

    def update(self):
        # screen.fill((255, 255, 255))
        pg.display.update()

    def show_onscreen_label(self, text):

        self.onscreen_label = self.font.render(
            text, True, JET_BLACK, BARELY_GRAY)

        self.onscreen_rect = self.onscreen_label.get_rect()

        self.onscreen_rect.center = (
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70)

        screen.blit(self.onscreen_label, self.onscreen_rect)

    def display_console(self):

        self.windowbox_rect = pg.Rect(
            ((SCREEN_WIDTH // 2) - (WIDTH // 2)), (SCREEN_HEIGHT // 8) * 5.5, 400, 200)

        self.windowbar_rect = pg.Rect(
            ((SCREEN_WIDTH // 2) - (WIDTH // 2)), (SCREEN_HEIGHT // 8) * 5.5, 400, 25)

        self.button_y = self.windowbar_rect.y + WINDOW_BAR_BUTTON_SIZE // 2

        self.redbutton_rect = pg.Rect(self.windowbar_rect.x + WINDOW_BAR_BUTTON_SIZE //
                                      2, self.button_y, WINDOW_BAR_BUTTON_SIZE, WINDOW_BAR_BUTTON_SIZE)

        self.yellowbutton_rect = pg.Rect(self.windowbar_rect.x + WINDOW_BAR_BUTTON_SIZE // 2 +
                                         WINDOW_BAR_BUTTON_GAP, self.button_y - 0.25, WINDOW_BAR_BUTTON_SIZE, WINDOW_BAR_BUTTON_SIZE)

        self.greenbutton_rect = pg.Rect(self.windowbar_rect.x + WINDOW_BAR_BUTTON_SIZE // 2 +
                                        WINDOW_BAR_BUTTON_GAP * 2, self.button_y - 1.25, WINDOW_BAR_BUTTON_SIZE, WINDOW_BAR_BUTTON_SIZE)

        self.windowbar_title_rect = pg.Rect(self.windowbar_rect.x + WINDOW_BAR_BUTTON_SIZE // 2 +
                                            WINDOW_BAR_BUTTON_GAP * 3.25, self.button_y - 1.25, WINDOW_BAR_TITLE_SIZE, WINDOW_BAR_BUTTON_SIZE)

        # Console window box
        pg.draw.rect(screen, JET_BLACK, self.windowbox_rect)

        # Console window bar
        pg.draw.rect(screen, SMOKEY_GRAY, self.windowbar_rect)

        # Red button
        pg.draw.rect(screen, PERSIAN_RED, self.redbutton_rect)

        # Yellow button
        pg.draw.rect(screen, ASIAN_YELLOW, self.yellowbutton_rect)

        # Green button
        pg.draw.rect(screen, TRUDEAU_GREEN, self.greenbutton_rect)

        # Window bar title
        self.windowbar_title = self.font.render(
            'CONSOLE', True, BLEACHED_WHITE)

        screen.blit(self.windowbar_title, self.windowbar_title_rect)

    # Handles the individual behaviour of buttons and different UI elements
    def display_console_content(self, state, equation='', coordinates='', whether_final=False, whether_hover=False):
        match state:
            case 'EQUATION_LABEL':

                self.equationtitle_label = self.mono_font_bold.render(
                    'EQUATION', True, BLEACHED_WHITE)

                self.coordinatetitle_label = self.mono_font_bold.render(
                    'COORDINATES', True, BLEACHED_WHITE)

                self.equationtitle_rect = self.equationtitle_label.get_rect()

                self.coordinatetitle_rect = self.coordinatetitle_label.get_rect()

                self.equationtitle_rect.center = (
                    self.windowbox_rect.x + 60, self.windowbar_rect.y + 50)

                self.coordinatetitle_rect.center = (
                    self.windowbox_rect.x + 75, self.windowbar_rect.y + 100)

                screen.blit(self.equationtitle_label, self.equationtitle_rect)

                screen.blit(self.coordinatetitle_label,
                            self.coordinatetitle_rect)

            case 'EQUATION_CONTENT':

                self.equation_label = self.mono_font_sm.render(
                    equation, True, BLEACHED_WHITE, JET_BLACK)

                self.coordinate_label = self.mono_font_sm.render(
                    coordinates, True, BLEACHED_WHITE, JET_BLACK)

                self.equation_rect = self.equation_label.get_rect()

                self.coordinate_rect = self.coordinate_label.get_rect()

                if not whether_final:
                    self.equation_rect.center = (
                        self.windowbox_rect.x + 200, self.windowbar_rect.y + 70)
                    self.coordinate_rect.center = (
                        self.windowbox_rect.x + 200, self.windowbar_rect.y + 100)
                else:
                    self.equation_rect.center = (
                        self.windowbox_rect.x + 180, self.windowbar_rect.y + 50)
                    self.coordinate_rect.center = (
                        self.windowbox_rect.x + 260, self.windowbar_rect.y + 100)

                screen.blit(self.equation_label, self.equation_rect)
                screen.blit(self.coordinate_label, self.coordinate_rect)

            case 'START_BUTTON':

                self.startbutton_container_rect = pg.Rect(
                    (SCREEN_WIDTH // 2) - 100, (SCREEN_HEIGHT // 8) * 6.8, 200, 50)
                self.startbutton_nested_container_rect = pg.Rect(
                    (SCREEN_WIDTH // 2) - 95, (SCREEN_HEIGHT // 8) * 6.85, 190, 40)

                if whether_hover == False:

                    pg.draw.rect(screen, BLEACHED_WHITE,
                                 self.startbutton_container_rect)
                    pg.draw.rect(screen, JET_BLACK,
                                 self.startbutton_nested_container_rect)

                    self.startbutton_label = self.mono_font_bold.render(
                        'START PLOTTING', True, BLEACHED_WHITE)
                    self.startbutton_rect = self.startbutton_label.get_rect()

                    self.startbutton_rect.center = (
                        SCREEN_WIDTH // 2, self.startbutton_nested_container_rect.centery)

                    screen.blit(self.startbutton_label, self.startbutton_rect)

                else:
                    pg.draw.rect(screen, BLEACHED_WHITE, pg.Rect(
                        self.startbutton_container_rect), self.startbutton_nested_container_rect.y)

                    self.startbutton_label = self.mono_font_bold.render(
                        'START PLOTTING', True, JET_BLACK)
                    self.startbutton_rect = self.startbutton_label.get_rect()

                    self.startbutton_rect.center = (
                        SCREEN_WIDTH // 2, self.startbutton_nested_container_rect.centery)

                    screen.blit(self.startbutton_label, self.startbutton_rect)


class FunctionPlotter(object):

    def __init__(self, game_m, screen_m):
        self.y_axis = HEIGHT // 2
        self.x_axis = WIDTH // 1.5 + 30

        self.scale = 150
        self.max_iter = 50

        self.game_m = game_m
        self.screen_m = screen_m

    def plot_fractal(self):
        print("Plotting the fractal...")
        self.game_m.fractal_gen_in_progress = True

        for x in range(WIDTH + 1):
            for y in range(HEIGHT // 2 + 1):
                self.coordinates = f'x: {x} | y: {y}'

                # Map pixel coordinates to a complex number, thanks to a built-in python function complex()
                self.c = complex(float(x - self.x_axis) / self.scale,
                                 float(y - self.y_axis) / self.scale)

                self.rounded_c = round(float(
                    x - self.x_axis) / self.scale, 2) + round(float(y - self.y_axis) / self.scale, 2) * 1j

                self.m = self.mandelbrot_eqt(
                    self.c, self.rounded_c, self.max_iter)

                # Set the color in correlation with the number of iterations; 255 is the max. value in the grayscale spectrum...
                self.color = 255 - int(self.m[0] * 255 / self.max_iter)

                self.equation = self.m[1]

                self.percent = f'{round((x / WIDTH) * 100, 2)} %' if x != 400 and y != 200 else '100.0 %'

                self.screen_m.display_console_content(
                    EQUATION_CONTENT, self.equation, self.coordinates)

                # Only plot the top portion of the fractal for performance reasons
                screen.set_at((x + ((SCREEN_WIDTH // 2) - (WIDTH // 2)), y +
                              (SCREEN_HEIGHT // 8)), (self.color, self.color, self.color))

                # Mirror the top part of the fractal on the bottom
                screen.set_at((x + ((SCREEN_WIDTH // 2) - (WIDTH // 2)), HEIGHT -
                              y + (SCREEN_HEIGHT // 8)), (self.color, self.color, self.color))

                self.screen_m.show_onscreen_label(self.percent)

                pg.display.update()

                # Draw a rectangle on the portion of the screen where the text has to be continously updated to prevent text overlapping...
                pg.draw.rect(screen, BARELY_GRAY, self.screen_m.onscreen_rect)

                pg.draw.rect(screen, JET_BLACK, self.screen_m.equation_rect)

                pg.draw.rect(screen, JET_BLACK, self.screen_m.coordinate_rect)

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
            equation = f'{rounded_z} = {rounded_z}^2 + {rounded_c}'.replace(
                'j', 'i')

            n += 1

        return [n, equation]


class EventManager(object):

    def __init__(self, game_m, screen_m):
        self.game_m = game_m
        self.screen_m = screen_m

        self.startbutton_container_rect = pg.Rect(
            (SCREEN_WIDTH // 2) - 100, (SCREEN_HEIGHT // 8) * 6.8, 200, 50)

    def key_bindings(self):
        self.mouse_pos = pg.mouse.get_pos()

        # Determine whether the mouse pointer is within the boundary of the start button or not... self.mouse_pos[0] => mouse's x position / self.mouse_pos[1] => mouse's y position
        self.whether_mouse_bound_x = self.startbutton_container_rect.x <= self.mouse_pos[
            0] <= self.startbutton_container_rect.x + self.startbutton_container_rect.width
        self.whether_mouse_bound_y = self.startbutton_container_rect.y <= self.mouse_pos[
            1] <= self.startbutton_container_rect.y + self.startbutton_container_rect.height

        for self.event in pg.event.get():
            if self.event.type == pg.QUIT:
                self.game_m.game_running = False

            if self.event.type == pg.MOUSEBUTTONDOWN:

                # If the start button is pressed...
                if self.whether_mouse_bound_x and self.whether_mouse_bound_y:
                    self.game_m.whether_default_show = False

                    pg.draw.rect(screen, JET_BLACK,
                                 self.screen_m.equation_rect)
                    pg.draw.rect(screen, JET_BLACK,
                                 self.screen_m.coordinate_rect)

                    # Play the background music...
                    pg.mixer.music.load('music/guitar.mp3')
                    pg.mixer.music.play(-1)

                    # Start plotting the fractal...
                    fp.plot_fractal()

    def button_animations(self):

        if self.whether_mouse_bound_x and self.whether_mouse_bound_y:
            # Highlight the button when mouse pointer is hovering above...
            self.screen_m.display_console_content(
                START_BUTTON, '', '', False, True)

        else:
            # Un-highlight the button when mouse pointer is outside of the boundary...
            self.screen_m.display_console_content(
                START_BUTTON, '', '', False, False)


class GameManager(object):

    def __init__(self):
        pg.init()

        self.clock = pg.time.Clock()
        self.screen_m = ScreenManager(self)

        self.frame_rate = 60

        self.game_running = True
        self.fractal_plotted = False
        self.show_finished = False
        self.fractal_gen_in_progress = False

        self.logo_img = pg.image.load('logo.png')
        self.font = pg.font.Font('fonts/LeagueSpartan-ExtraLight.ttf', 21)

        self.logo_img = pg.transform.scale(
            self.logo_img, (self.logo_img.get_width() // 3.5, self.logo_img.get_height() // 3.5))

        screen.fill(BLEACHED_WHITE)

        self.event_m = EventManager(self, self.screen_m)

        self.whether_default_show = True

        self.main_loop()

    def update(self):
        global fp
        fp = FunctionPlotter(self, self.screen_m)

        # If the fractal is not formed yet...
        if not self.fractal_plotted:
            # Placeholder rectangle to cover the area where the fractal will be generated
            pg.draw.rect(screen, BARELY_GRAY, pg.Rect(
                ((SCREEN_WIDTH // 2) - (WIDTH // 2)), SCREEN_HEIGHT // 8, 400, 400))

            # Display the top bar
            pg.draw.rect(screen, BARELY_GRAY, pg.Rect(0, 0, SCREEN_WIDTH, 30))

            self.top_bar_label = self.screen_m.font_bold.render(
                'iMandelbrot', True, JET_BLACK)

            self.top_bar_rect = self.top_bar_label.get_rect()

            self.top_bar_rect.center = (
                SCREEN_WIDTH // 2, 15)

            screen.blit(self.top_bar_label, self.top_bar_rect)

            self.screen_m.display_console()
            self.screen_m.display_console_content(EQUATION_LABEL)

            # Display the logo
            screen.blit(self.logo_img, ((SCREEN_WIDTH // 2) - (self.logo_img.get_width() // 2),
                        (SCREEN_HEIGHT // 8 + HEIGHT // 2) - (self.logo_img.get_height() // 2)))

            # Display the credit text

            self.credit_label = self.font.render(
                'Developed and Maintained by John Seong', True, JET_BLACK, BARELY_GRAY)

            self.credit_rect = self.credit_label.get_rect()

            self.credit_rect.center = (
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

            screen.blit(self.credit_label, self.credit_rect)

            if self.whether_default_show:
                self.screen_m.display_console_content(
                    EQUATION_CONTENT, 'Zn+1 = (Zn)^2 + C', 'x: ALL POINTS | y: ALL POINTS', True)

            # fp.plot_fractal()

            self.show_finished = True

        # Show the label indicating that the plotting process has ended...
        elif self.fractal_plotted and self.show_finished:

            self.screen_m.show_onscreen_label('The Mandelbrot Set')

            self.screen_m.display_console_content(EQUATION_LABEL)

            self.screen_m.display_console_content(
                EQUATION_CONTENT, 'Zn+1 = (Zn)^2 + C', 'x: ALL POINTS | y: ALL POINTS', True)

            pg.display.update()

            self.show_finished = False

    def main_loop(self):
        '''
        This is the main loop of the program, where most of the commands are executed!
        '''
        while self.game_running == True:
            self.time_delta = self.clock.tick(self.frame_rate) / 1000.0
            
            if not self.fractal_plotted and not self.fractal_gen_in_progress:
                self.event_m.key_bindings()
                self.event_m.button_animations()

            self.screen_m.update()

            self.update()

        # pg.quit()


# Run the code
game_m = GameManager()
