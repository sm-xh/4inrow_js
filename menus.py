import sys

import numpy as np
import pygame
from gameLogic import *
from constans import *


class userInterface:
    """Klasa bazowa definujaca interfejs uzytkownika"""

    def __init__(self):
        """konstruktor inicjalizujący ustawienia gry"""
        self.game = Game()
        self.run = True
        self.click = False

        self.clock = pygame.time.Clock()
        self.gameDisplay = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Connect Four")
        pygame.init()
        pygame.font.init()
        # kolory
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.green = (0, 100, 30)
        self.white = (255, 255, 255)
        # kofiguracja czcionek
        self.bigFont = pygame.font.SysFont(None, 80)
        self.mediumFont = pygame.font.SysFont(None, 50)
        self.smallFont = pygame.font.SysFont(None, 30)

    def startScreen(self):
        """funkcja definiująca ekran startowy"""
        skip = False
        self.gameDisplay.fill((88, 111, 200))

        # przyciski menu
        button_start = pygame.Rect(200, 150, 400, 80)
        button_help = pygame.Rect(200, 300, 400, 80)
        button_quit = pygame.Rect(200, 450, 400, 80)

        pygame.draw.rect(self.gameDisplay, (255, 0, 0), button_start)
        pygame.draw.rect(self.gameDisplay, (255, 0, 0), button_help)
        pygame.draw.rect(self.gameDisplay, (255, 0, 0), button_quit)

        play = self.bigFont.render("Start Game", True, (0, 0, 0))
        rules = self.bigFont.render("Rules", True, (0, 0, 0))
        quit = self.bigFont.render("Quit", True, (0, 0, 0))

        self.gameDisplay.blit(play, (250, 160))
        self.gameDisplay.blit(rules, (320, 315))
        self.gameDisplay.blit(quit, (330, 460))

        while not skip:
            self.clock.tick(30)
            # lokalizacja kursora myszki
            mx, my = pygame.mouse.get_pos()

            if button_start.collidepoint((mx, my)):
                if self.click == True:
                    self.game.twoPlayer = True
                    self.playgame()
            if button_help.collidepoint(((mx, my))):
                if self.click == True:
                    self.about()
            if button_quit.collidepoint((mx, my)):
                if self.click == True:
                    skip = True
                    self.run = False

            self.click = False
            # detekcja wyjścia z gry
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                pygame.display.update()

    def about(self):

        instructions_txt = 'Gra rozgrywana jest na pionowym, pustym, drewnianym urządzeniu, w którym gracze na \n \
        przemian upuszczają swoje kafelki na wierzch. Pole gry składa się z 7 pionowych kolumn i 6 poziomych linii. \n \
        Obaj gracze mają po 21 identycznych kolorowych płytek. Kiedy gracz upuszcza element do kolumny, zajmuje \n \
        najniższą dostępną przestrzeń w kolumnie. Każdy gracz jest reprezentowany przez jego kolor \n \
         (na przykład brązowy dla pierwszego gracza i żółty dla drugiego). \n \
          Jest odtwarzany naprzemiennie. Celem gry jest posiadanie czterech kawałków koloru z rzędu. \n \
          Ten wiersz może być pionowy, poziomy lub ukośny. Możesz to zrobić, umieszczając kamienie jeden \n \
          po drugim w siedmiu możliwych kolumnach. Kamienie spadają na najniższą możliwą wolną przestrzeń \n \
           albo na ziemię, albo na inny kamień.'.split('\n')

        self.gameDisplay.fill((66, 111, 155))

        button_return = pygame.Rect(200, 500, 600, 80)
        pygame.draw.rect(self.gameDisplay, (255, 0, 0), button_return)
        return_to = self.bigFont.render("Powrót do menu", True, (0, 0, 0))
        self.gameDisplay.blit(return_to, (250, 520))

        aboutscreen = []
        for i in range(len(instructions_txt)):
            aboutscreen.append(self.smallFont.render(instructions_txt[i], True, (0, 0, 0)))
            self.gameDisplay.blit(aboutscreen[i], (80, 20 * i + 250))

        skip = False
        while not skip:
            self.clock.tick(30)  # This limits the while loop to a max of 10 times per second.

            mx, my = pygame.mouse.get_pos()
            if button_return.collidepoint((mx, my)):
                if self.click == True:
                    skip = True
                    self.startScreen()
            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                pygame.display.update()

    def playgame(self):
        self.gameDisplay.fill(self.green)

        """petla rysujaca plansze"""
        for row in range(1, ROW_COUNT + 1):
            for column in range(1, COLUMN_COUNT + 1):
                pygame.draw.circle(self.gameDisplay, self.white, (column * 100, row * 100 + 130), 30)

        """petla rysujaca przyciski"""
        for row in range(1, COLUMN_COUNT + 1):
            pygame.draw.rect(self.gameDisplay, (240,30,200), [row*100-25, 100, 50, 50])
            pygame.draw.rect(self.gameDisplay, (220,20,190), [row*100-20, 105, 40, 40])

        pygame.draw.rect(self.gameDisplay, (70,20,40), [290,20,200,40])
        help_text = self.mediumFont.render('POMOC', 1, (40, 20, 30))
        self.gameDisplay.blit(help_text, (320, 24))

        """glowna petla gry"""
        while self.run:
            self.clock.tick(30)
            player1 = self.mediumFont.render('Czerwony', 1, self.red if self.game.turn == 1 else (self.green))
            player2 = self.mediumFont.render('Żółty', 1, self.yellow if self.game.turn == 2 else (self.green))
            self.gameDisplay.blit(player1, (50, 24))
            self.gameDisplay.blit(player2, (650, 24))



            if not self.game.game_over:
                if self.game.twoPlayer or (self.game.turn == 1):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.run = False

                        if event.type == pygame.MOUSEBUTTONUP:
                            pos = pygame.mouse.get_pos()
                            row, column = self.game.player_move(pos)
                            if (row == -1 or column == -1): continue
                            pygame.draw.circle(self.gameDisplay, self.red if self.game.turn == 1 else self.yellow,
                                               ((column + 1) * 100, (row + 1) * 100 + 130), 30)
                            self.game.isGameOver()
            else:
                self.endOfGame()
            pygame.display.update()

    def playAgain(self):

        self.game = Game()
        self.welcomeScreen()

    def endOfGame(self):

        pygame.draw.rect(self.gameDisplay, (200, 0, 0) if self.game.turn == 1 else (255, 255, 0), (0, 0, 800, 52))
        pygame.draw.rect(self.gameDisplay, (102, 204, 0), (0, 640, 800, 30))
        pygame.draw.rect(self.gameDisplay, (204, 0, 0), (0, 670, 800, 30))
        if self.game.winner == 'Draw':
            congrats = self.mediumFont.render('Draw!', 1, (0, 0, 0))
        elif self.game.winner == 'Player1':
            congrats = self.mediumFont.render(self.game.getTurn() + ' wins ! Congrats!', 1, (0, 0, 0))

        else:
            congrats = self.mediumFont.render(
                self.game.getTurn() + ' wins ! Congrats!' if self.game.twoPlayer == True else self.game.getTurn() + ' wins !',
                1, (0, 0, 0))
        quit = self.smallFont.render('Quit', 1, (0, 0, 0))
        playAgain = self.smallFont.render('Play again', 1, (0, 0, 0))
        self.gameDisplay.blit(congrats, (280, 15))
        self.gameDisplay.blit(quit, (375, 680))
        self.gameDisplay.blit(playAgain, (350, 650))

        skip = False
        while not skip:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    skip = True
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[1] > 640:
                        if pos[1] < 670:
                            self.playAgain()
                        else:
                            skip = True
                            self.run = False

            pygame.display.update()
