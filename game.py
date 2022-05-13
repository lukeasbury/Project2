import pygame
from sys import exit
from menu import *
import time
from playsound import playsound


class Game():
    """
    Class used to define the Game
    """
    def __init__(self):
        """
        Method used to set basic parameters and prep window
        """
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 480, 270
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE, self.YELLOW = (0, 0, 0), (255, 255, 255), (255, 255, 0)
        self.main_menu = MainMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        """
        Method used to play the game/program
        -This is the actual program and project base
        """
        translate_dict = {'A': '.-', 'B': '-...',
                          'C': '-.-.', 'D': '-..', 'E': '.',
                          'F': '..-.', 'G': '--.', 'H': '....',
                          'I': '..', 'J': '.---', 'K': '-.-',
                          'L': '.-..', 'M': '--', 'N': '-.',
                          'O': '---', 'P': '.--.', 'Q': '--.-',
                          'R': '.-.', 'S': '...', 'T': '-',
                          'U': '..-', 'V': '...-', 'W': '.--',
                          'X': '-..-', 'Y': '-.--', 'Z': '--..',
                          '1': '.----', '2': '..---', '3': '...--',
                          '4': '....-', '5': '.....', '6': '-....',
                          '7': '--...', '8': '---..', '9': '----.',
                          '0': '-----', " ": "/"}

        reverse_dict = {v: k for k, v in translate_dict.items()}

        clock = pygame.time.Clock()

        screen = self.window

        base_font = pygame.font.Font(None, 32)
        user_text = ''

        input_rect = pygame.Rect((self.DISPLAY_W/2)/2, self.DISPLAY_H/2 - 30, 140, 32)

        color_active = pygame.Color(self.WHITE)

        color_passive = pygame.Color(self.YELLOW)
        color = color_passive

        active = False

        message = user_text

        reverse_message = ''


        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False

                if event.type == pygame.KEYDOWN:
                    if color == color_passive and event.key == pygame.K_BACKSPACE:
                        self.playing = False
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key != pygame.K_RETURN:
                        user_text += event.unicode

                    if event.key == pygame.K_RETURN:
                        try:
                            message = user_text
                            if "?!()=+\"'$#%@&^:;{}[]<>,_" in message:
                                raise(KeyError)
                            if message[0] == '.' or message[0] == '-' or message[0] == '/':
                                reverse_message = "".join(reverse_dict[c] for c in message.split(" "))
                                message = reverse_message

                            sound = " ".join(translate_dict[c] for c in message.upper())

                            self.play_morse_code(sound)
                        except KeyError:
                            message = ''
                            user_text = 'Invalid Input, Try Again!'

            if active:
                color = color_active
            else:
                color = color_passive
            self.display.fill(self.BLACK)

            self.font_name = '8-BIT WONDER.TTF'
            self.draw_text('Input Message or Morse Code', 15, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 50)
            self.font_name = pygame.font.get_default_font()
            if message == reverse_message:
                self.draw_text(message, 30, self.DISPLAY_W / 2, self.DISPLAY_H / 2 + 50)
            else:
                self.draw_text(sound, 30, self.DISPLAY_W / 2, self.DISPLAY_H / 2 + 50)
            self.font_name = '8-BIT WONDER.TTF'
            pygame.draw.rect(screen, color, input_rect)

            text_surface = base_font.render(user_text, True, self.BLACK)
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(240, text_surface.get_width() + 10)

            pygame.display.flip()

            clock.tick(60)

            screen.blit(self.display, (0, 0))
            self.reset_keys()

    def check_events(self):
        """
        Used to help with input keys and make sure they are working as intended
        -Also used to close the program
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        """
        Method used to reset all the keys that players press
        """
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        """
        Method used to display text without creating a visible rectangle around it
        """
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def play_morse_code(self, message):
        """
        Method used to play the sounds whenever a message is created used in game_loop
        """
        for c in message:
            if c == ".":
                playsound("short.mp3")
                time.sleep(0.3)
            elif c == "-":
                playsound("long.mp3")
                time.sleep(0.3)
            elif c == "/" or c == " ":
                time.sleep(0.5)
