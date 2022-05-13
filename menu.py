import pygame
import webbrowser

class Menu():
    """
    Class used to display the Menu
    """
    def __init__(self, game):
        """
        Method used to define basic parameters throughout the project
        """
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        """
        Method used to create cursor used in main menu screen
        """
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        """
        Method used to reset and update screen
        """
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    """
    Class used to define the main menu/start screen
    """
    def __init__(self, game):
        """
        Method used to define basic parameters
        """
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        """
        Method used to display what people will see in the main menu
        """
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Morse Code Interpreter', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Input Data", 20, self.startx, self.starty)
            self.game.draw_text("Dictionary", 20, self.optionsx, self.optionsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        """
        Method used to move cursor and select options
        """
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

    def check_input(self):
        """
        Method used to switch screens for whichever screen is selected
        """
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
                self.run_display = False
            elif self.state == 'Options':
                 webbrowser.open(r"https://www.merriam-webster.com/dictionary/Morse%20code")
