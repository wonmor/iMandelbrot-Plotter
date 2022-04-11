#-----------------------------------------------------------------------------
# Name:        iMandelbrot: An Interactive Module
# Purpose:     iMandelbrot is a tool made out of PyGame that visualizes the nature of a Mandelbrot fractal!
#
# Author:      John Seong
# Created:     April 6, 2022
# Updated:     April 11, 2022
#---------------------------------------------------------------------------------------#
#   I think this project deserves a level 4+ because...
#
#   Features Added:
#
#   1. For the sake of optimization,
#       iMandelbrot only generates the coordinates above the x-axis,
#       basically duplicating to the corresponding coordinates below the horizontal line.
#
#   2. The user interface is very intuitive that even a kindergardener can immediately tell which is which;
#       the program additionally displays what is going on behind the scenes
#       to validate that the Mandelbrot set equation indeed works perfectly in real life.
#---------------------------------------------------------------------------------------#

'''

██╗███╗░░░███╗░█████╗░███╗░░██╗██████╗░███████╗██╗░░░░░██████╗░██████╗░░█████╗░████████╗
██║████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝██║░░░░░██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██║██╔████╔██║███████║██╔██╗██║██║░░██║█████╗░░██║░░░░░██████╦╝██████╔╝██║░░██║░░░██║░░░
██║██║╚██╔╝██║██╔══██║██║╚████║██║░░██║██╔══╝░░██║░░░░░██╔══██╗██╔══██╗██║░░██║░░░██║░░░
██║██║░╚═╝░██║██║░░██║██║░╚███║██████╔╝███████╗███████╗██████╦╝██║░░██║╚█████╔╝░░░██║░░░
╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░

█▀▄ █▀▀ █░█ █▀▀ █░░ █▀█ █▀█ █▀▀ █▀▄   █▄▄ █▄█   ░░█ █▀█ █░█ █▄░█   █▀ █▀▀ █▀█ █▄░█ █▀▀
█▄▀ ██▄ ▀▄▀ ██▄ █▄▄ █▄█ █▀▀ ██▄ █▄▀   █▄█ ░█░   █▄█ █▄█ █▀█ █░▀█   ▄█ ██▄ █▄█ █░▀█ █▄█


---------------------------------------------------------------------------------------

Python 3.10 and above required to run this program!

'''

import pygame as pg

import os

import platform

'''
CONSTANTS
These include button sizes, screen sizes, the size of the graph, colour values, etc.
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
ASIAN_YELLOW = (252, 194, 1)  # Just a joke (I am Asian by the way, so please do not cancel me out)
TRUDEAU_GREEN = (19, 135, 21)  # Yes
JET_BLACK = (0, 0, 0)
SMOKEY_GRAY = (70, 70, 70)
BARELY_GRAY = (211, 211, 211)
BLEACHED_WHITE = (255, 255, 255)

EQUATION_LABEL = 'EQUATION_LABEL'
EQUATION_CONTENT = 'EQUATION_CONTENT'
START_BUTTON = 'START_BUTTON'


# Pygame has built-in collider detection for rect type objects


'''
ScreenManager class dictates the behaviour of all on-screen UI elements on the program,
which include buttons, images, and texts.
'''

class ScreenManager(object):

    def __init__(self, game_m):
        '''
        This function is an intializer that defines the paths for the fonts and defines the screen resolution
        
        Parameters
        ----------
        game_m: Instance of a class
            GameManager object

        Returns
        -------
        None

        '''
        self.display_x = SCREEN_WIDTH
        self.display_y = SCREEN_HEIGHT

        pg.display.set_caption('iMandelbrot')

        self.update_screen_resolution(self.display_x, self.display_y)

        self.game_m = game_m

        self.font = pg.font.Font(
            GameManager.get_path('src/fonts/LeagueSpartan-ExtraLight.ttf'), 21)
        self.font_bold = pg.font.Font(
            GameManager.get_path('src/fonts/LeagueSpartan-SemiBold.ttf'), 18)

        self.mono_font_bold = pg.font.Font(
            GameManager.get_path('src/fonts/RobotoMono-Medium.ttf'), 18)
        self.mono_font_sm = pg.font.Font(
            GameManager.get_path('src/fonts/RobotoMono-Regular.ttf'), 14)


    @staticmethod
    def update_screen_resolution(display_x, display_y):
        '''
        A static method that updates the resolution of a screen
        
        Parameters
        ----------
        display_x: Integer
            The width of the screen
        display_y: Integer
            The height of the screen

        Returns
        -------
        None

        '''
        global screen
        screen = pg.display.set_mode([display_x, display_y], pg.DOUBLEBUF)

    def update(self):
        '''
        This method runs every frame and updates the display
        
        Parameters
        ----------
        None

        Returns
        -------
        None

        '''
        pg.display.update()


    def show_onscreen_label(self, text):
        '''
        This is a method that displays an on-screen label on the program, specifically on the centre portion of the display
        
        Parameters
        ----------
        text: String
            A user-defined text that can be displayed on the centre portion of the display

        Returns
        -------
        None
        '''
        self.onscreen_label = self.font.render(
            text, True, JET_BLACK, BARELY_GRAY)

        self.onscreen_rect = self.onscreen_label.get_rect()

        # This will set the relative position of the label to the centre of the display despite the potential resolution changes that can be made...
        self.onscreen_rect.center = (
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70)

        screen.blit(self.onscreen_label, self.onscreen_rect)

    def display_console(self):
        '''
        This is a method that displays an on-screen label on the program, specifically on the centre portion of the display
        
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
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
        '''
        ONLY IN PYTHON 3.10 AND OVER: MATCH-CASE STATEMENT
        A generic state-finite machine that dictates the behaviour of each text on the console depending on the state of the program.
        When the plotting process has not yet started, the texts on the console will display a static information that indicates that
        e.g. the domain and the range of the function will be all points, scale, equation, etc.
        
        Parameters
        ----------
        state: String
            Current state of the state-finite machine
        equation: String
            Equation that will be displayed on the in-game console window
        coordinates: String
            Coordinates that will show up on the in-game console window
        whether_final: Boolean
            A boolean variable that definees whether the program is in its final stage after all the graph plotting has completed
        whether_hover: Boolean
            A boolean variable that defines whether the mouse is hovering over the button or not (Collision detection)

        Returns
        -------
        None
        '''
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
        '''
        Set up initial values such as the max iteration count or the scale of the Mandelbrot fractal
        
        Parameters
        ----------
        game_m: Instance of a class
            GameManager object
        screen_m: Instance of a class
            ScreenManager object

        Returns
        -------
        None
        '''
        self.y_axis = HEIGHT // 2
        self.x_axis = WIDTH // 1.5 + 30

        self.scale = 150
        self.max_iter = 50

        self.game_m = game_m
        self.screen_m = screen_m

    def plot_fractal(self):
        '''
        A method that plots the Mandelbrot set based upon the x and y coordinates of the display
        
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        # Print out a message to debug console to indicate that the plotting function process is running....
        print("Plotting the fractal...")

        # This is a boolean value that determines whether the plotting function process is running or not...
        self.game_m.fractal_gen_in_progress = True

        # For all x-values in the x-axis of the display and y-values in the y-axis of the display...
        for x in range(WIDTH + 1):
            for y in range(HEIGHT // 2 + 1):

                # To let the OS know that the game isn't crashing but in an idle state...
                pg.event.pump()

                # Save the current coordinates to print them out on the in-game console...
                self.coordinates = f'x: {x} | y: {y}'

                '''
                Normalize pixel coordinates to a complex number,
                thanks to a built-in python function complex(),
                which contains two variables: real and imaginary numbers.

                The reason we convert the y-axis of the plane to imaginary numbers and x-axis to the real numbers is pretty obvious:
                because that's what the complex plane should look like.

                MORE EXPLANATION ABOUT COMPLEX PLANES: 
                https://en.wikipedia.org/wiki/Complex_plane

                The complex() function in Python basically works in the same way the real life complex numbers work.
                In a nutshell, i (in this case, j) = sqrt(-1) 
                and the Mandelbrot fractal is generated upon a complex plane
                where the y-axis is the imaginary number axis
                and the x-axis is the real number axis.
                '''

                self.c = complex(float(x - self.x_axis) / self.scale,
                                 float(y - self.y_axis) / self.scale)

                self.rounded_c = round(float(
                    x - self.x_axis) / self.scale, 2) + round(float(y - self.y_axis) / self.scale, 2) * 1j

                self.m = self.mandelbrot_eqt(
                    self.c, self.rounded_c, self.max_iter)

                # Set the color in correlation with the number of iterations; 255 is the max. value in the grayscale spectrum...
                self.color = 255 - int(self.m[0] * 255 / self.max_iter)

                # Equation is the second value in the list that is returned by the mandelbrot_eqt function...
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

                # Show the percentage label and update it every iteration...
                self.screen_m.show_onscreen_label(self.percent)

                pg.display.update()

                # Draw a rectangle on the portion of the screen where the text has to be continously updated to prevent text overlapping...
                pg.draw.rect(screen, BARELY_GRAY, self.screen_m.onscreen_rect)

                pg.draw.rect(screen, JET_BLACK, self.screen_m.equation_rect)

                pg.draw.rect(screen, JET_BLACK, self.screen_m.coordinate_rect)

        print("Plotting successfuly completed!")

        self.game_m.fractal_plotted = True
        self.game_m.show_finished = True

    '''
    EQUATION LINK AND FURTHER EXPLANATION: https://simple.wikipedia.org/wiki/Mandelbrot_set

    Basically the way Mandelbrot fractal works is that
    n, which is the index (should be a positive integer) of the complex number Z will start from 0.
    Then, it will intercept with another complex number which is C, and together, both added, will be defined as the new Z. 
    This Z, will again go through the same equation with this time a different n, which will increase by an increment of 1.
    This iteration process will continue until it reaches the count of the max iteration, which was determined previously in the __init__ function.
    The Z values that will "blow up," a layman term indicating that it approaches either negative or positive infinity will NOT be plotted on the graph,
    which we set as a numerical value in this case because computer science does not accept any "conceptual values."
    The colours are defined on the grayscale based upon the size of the complex number Z.

    In this case though, to maximize the performance and speed of plotting the set,
    and considering that the fully graphed version of a Mandelbrot set is symmetrical across the x-axis,
    we are just literally copying the top part of the Mandelbrot set onto the bottom part, to save the resources since Python is not optimized for heavy computation.
    (To perform full-on computation with superior speed, a total revamp of the code is needed as it needs to implement modules such as NumPy or Cython: a combination of Python and C language).
    '''

    @staticmethod
    def mandelbrot_eqt(c, rounded_c, max_iter):
        '''
        Set up initial values such as the max iteration count or the scale of the Mandelbrot fractal
        
        Parameters
        ----------
        c:
            A complex number that contains both the real and imaginary axes, converted from display coordinates
        rounded_c:
            The same as the C value but is rounded up to two signicant digits

        Returns
        -------
        List
            Contains n, which represents the number of iteration, as well as the equation, which is a String value that contains the full decrypted information
                of all variables that the program is plugging in
        '''
        z = 0
        n = 0

        while abs(z) <= 2 and n < max_iter:
            z = z ** 2 + c

            rounded_z = complex(round(z.real, 2), round(z.imag, 2))
            equation = f'{rounded_z} = {rounded_z}^2 + {rounded_c}'.replace(
                'j', 'i')

            n += 1

        return [n, equation]

'''
EventManager is a clss that dictates the behaviour of all major events that happen in the program.
such as the key bindings and the animations that will happen when e.g. a mouse cursor is hovering over a button.
'''

class EventManager(object):

    def __init__(self, game_m, screen_m):
        '''
        An initializer method that receives the GameManager and ScreenManager objects as well as setting up the boundaries for the start button
        
        Parameters
        ----------
        game_m: Instance of a class
            GameManager object

        screen_m: Instance of a class
            ScreenManager object

        Returns
        -------
        None
        '''
        self.game_m = game_m
        self.screen_m = screen_m

        self.whether_endgame = False

        self.startbutton_container_rect = pg.Rect(
            (SCREEN_WIDTH // 2) - 100, (SCREEN_HEIGHT // 8) * 6.8, 200, 50)

    def key_bindings(self):
        '''
        A method that defines the button on-click behaviours
        
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.mouse_pos = pg.mouse.get_pos()

        # Determine whether the mouse pointer is within the boundary of the start button or not... self.mouse_pos[0] => mouse's x position / self.mouse_pos[1] => mouse's y position
        self.whether_mouse_bound_x = self.startbutton_container_rect.x <= self.mouse_pos[
            0] <= self.startbutton_container_rect.x + self.startbutton_container_rect.width
        self.whether_mouse_bound_y = self.startbutton_container_rect.y <= self.mouse_pos[
            1] <= self.startbutton_container_rect.y + self.startbutton_container_rect.height

        for self.event in pg.event.get():
            if self.event.type == pg.QUIT:
                self.game_m.game_running = False

            if not self.whether_endgame and self.event.type == pg.MOUSEBUTTONDOWN:

                # If the start button is pressed...
                if self.whether_mouse_bound_x and self.whether_mouse_bound_y:
                    self.game_m.whether_default_show = False

                    pg.draw.rect(screen, JET_BLACK,
                                 self.screen_m.equation_rect)
                    pg.draw.rect(screen, JET_BLACK,
                                 self.screen_m.coordinate_rect)

                    # Play the background music...
                    pg.mixer.music.load(
                        GameManager.get_path('src/music/guitar.mp3'))
                    pg.mixer.music.play(-1)

                    # Start plotting the fractal...
                    fp.plot_fractal()

    def button_animations(self):
        '''
        A method that sets up the button animations; when the mouse pointer is hovering above the button, it swaps the sprites
        
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.whether_mouse_bound_x and self.whether_mouse_bound_y:
            # Highlight the button when mouse pointer is hovering above...
            self.screen_m.display_console_content(
                START_BUTTON, '', '', False, True)

        else:
            # Un-highlight the button when mouse pointer is outside of the boundary...
            self.screen_m.display_console_content(
                START_BUTTON, '', '', False, False)

'''
GameManager is the first class that is instantiated when the program runs.
which includes the update method that runs every frame, plotting the function only when it is supposed to do so.
It also sets the route of different elements in the game such as the logo or the icon image.
'''

class GameManager(object):

    def __init__(self):
        '''
        An initializer that runs at the start of the game. Defines the boolean values that will be used to represent each state of the game,
        as well as the clock that will run throughout the game to get the delta time.
        
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        pg.init()

        self.clock = pg.time.Clock()
        self.screen_m = ScreenManager(self)

        self.frame_rate = 60

        self.game_running = True
        self.fractal_plotted = False
        self.show_finished = False
        self.fractal_gen_in_progress = False
        self.whether_default_show = True

        self.logo_img = pg.image.load(GameManager.get_path('src/logo.png'))
        self.icon_img = pg.image.load(GameManager.get_path('src/icon.png'))

        self.logo_img = pg.transform.scale(
            self.logo_img, (self.logo_img.get_width() // 3.5, self.logo_img.get_height() // 3.5))

        pg.display.set_icon(self.icon_img)

        screen.fill(BLEACHED_WHITE)

        self.event_m = EventManager(self, self.screen_m)

        self.main_loop()

    def update(self):
        '''
        A method that runs every frame. Instantiates the FunctionPlotter class, as well as setting up the default behaviour
        of both the console window and the area where the fractal will be graphed (displaying a logo)
        
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
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

            self.credit_label = self.screen_m.font.render(
                'Developed and Maintained by John Seong', True, JET_BLACK, BARELY_GRAY)

            self.credit_rect = self.credit_label.get_rect()

            self.credit_rect.center = (
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

            screen.blit(self.credit_label, self.credit_rect)

            if self.whether_default_show:
                self.screen_m.display_console_content(
                    EQUATION_CONTENT, 'Zn+1 = (Zn)^2 + C', 'x: ALL POINTS | y: ALL POINTS', True)

        # Show the label indicating that the plotting process has ended...
        elif self.fractal_plotted and self.show_finished:

            self.screen_m.show_onscreen_label('The Mandelbrot Set')

            self.screen_m.display_console_content(EQUATION_LABEL)

            self.screen_m.display_console_content(
                EQUATION_CONTENT, 'Zn+1 = (Zn)^2 + C', 'x: ALL POINTS | y: ALL POINTS', True)

            # To cover up the start button container that was created at the beginning of the loop...
            pg.draw.rect(screen, JET_BLACK,
                         self.screen_m.startbutton_container_rect)

            self.screen_m.update()

            self.show_finished = False

    # Resolve Py2App Crashing Error in Finder but not when opening it using Terminal: https://stackoverflow.com/questions/63611190/python-macos-builds-run-from-terminal-but-crash-on-finder-launch

    @staticmethod
    def get_path(filename):
        '''
        A static method that returns the corresponding relative path of the file name that is entered depending on the operating system.
        Specifically designed for macOS, as it uses a different kind of path system in comparison to Windows.
        
        Parameters
        ----------
        filename: String
            Gets the path of a specific file that the program is looking for

        Returns
        -------
        String
            Returns a string of a path that is converted depending on the user's operating system
        '''
        name = os.path.splitext(filename)[0]
        ext = os.path.splitext(filename)[1]

        # For macOS only...
        if platform.system() == "Darwin":
            from AppKit import NSBundle
            file = NSBundle.mainBundle().pathForResource_ofType_(name, ext)
            return file or os.path.realpath(filename)
        elif platform.system() == "win32":
            return filename.replace("/", "\\")
        else:
            return os.path.realpath(filename)

    def main_loop(self):
        '''
        This is the main loop of the program, where most of the commands are executed!
        It invovles the calculation of a delta time, deciding whether to enable the button animations or not,
        and running the update method in each class.
        
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        while self.game_running == True:
            # To let the OS know that the game isn't crashing but in an idle state...
            pg.event.pump()

            self.time_delta = self.clock.tick(self.frame_rate) / 1000.0

            self.event_m.key_bindings()

            if not self.fractal_plotted and not self.fractal_gen_in_progress:
                self.event_m.whether_endgame = False
                self.event_m.button_animations()

            else:
                self.event_m.whether_endgame = True

            self.screen_m.update()

            self.update()

        # pg.quit()


# Run the code
game_m = GameManager()

# IF THE LOADNG CURSOR IS KEEP SHOWING UP: https://stackoverflow.com/questions/20165492/pygame-window-not-responding-after-a-few-seconds
