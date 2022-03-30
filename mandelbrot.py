import pygame as pg
import pygame_gui

GUI = pygame_gui.elements


# Pygame has built-in collider detection for rect type objects


class ScreenManager(object):
    
    def __init__(self, display_x, display_y, game_m):
        self.display_x = display_x
        self.display_y = display_y
        self.ui_manager = pygame_gui.UIManager((800, 600))
        self.button_layout_rect = pg.Rect(30, 20, 100, 20)
        pg.display.set_caption('iMandelbrot Plotter')
        self.update_screen_resolution()
        self.game_m = game_m

    def update_screen_resolution(self):
        self.screen = pg.display.set_mode([self.display_x, self.display_y])

    def update(self):
        self.screen.fill((255, 255, 255))
        self.ui_manager.update(self.game_m.time_delta)
        self.ui_manager.draw_ui(self.screen)
        GUI.UIButton(relative_rect=self.button_layout_rect,
                     text='Hello',
                     manager=self.ui_manager,
                     container=self.screen)


class EventManager(object):

    def __init__(self):
        pass


class GameManager(object):

    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.frame_rate = 60
        self.game_running = True
        self.screen_m = ScreenManager(1280, 720, self)
        self.main_loop()

    def update(self):
        pass

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
