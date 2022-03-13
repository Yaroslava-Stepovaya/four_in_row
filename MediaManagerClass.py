import os, sys
import pygame as pg

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255,255,255)

class MediaManager():
    def __init__(self,screen_size_w, screen_size_h, board, sector_size):
        pg.init()
        self.screen = pg.display.set_mode((screen_size_w, screen_size_h))
        self.board = board
        self.sector_size = sector_size

        pg.display.set_caption("Four in a row")

        #background
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        #data_graphics
        self.sector_image = self.load_image("cell.png")
        self.disc1_image = self.load_image("disc1.png")
        self.disc2_image = self.load_image("disc2.png")

        # fonts
        self.font = pg.font.SysFont('arial.ttf', 72)
        self.font_img = None
        self.show_draw_win_text = False
        self.winner = ''

    def set_winnner(self, player_index):
        self.winner = str(player_index)

    def draw_board(self):
        for i in range(len(self.board.grid)):
            for j in range(len(self.board.grid[i])):
                self.draw_tile(j, i, self.board.grid[i][j])

    def draw_tile(self,x, y, value):
        image = None
        if value == 0:
            image = self.sector_image
        elif value == 1:
            image = self.disc1_image
        elif value == 2:
            image = self.disc2_image

        rect = self.sector_image.get_rect()
        rect.topleft = (x * self.sector_size, y * self.sector_size)
        self.screen.blit(image, rect)

    def draw_win_text(self):
        self.font_img = self.font.render('Player ' + self.winner + ' wins!', True, WHITE)
        self.screen.blit(self.font_img, (40, 120))


    def update_graphics(self): #Выполняем апдейт всей графики
        self.screen.blit(self.background,(0, 0))
        self.draw_board()
        if self.winner != '':
            self.draw_win_text()
        pg.display.flip()

    # functions to create our resources
    def load_image(self,name):
        fullname = os.path.join('data', name)
        try:
            image = pg.image.load(fullname)
        except Exception as e:
            print("Cannot load  image",name,e)
            return None
        if image.get_alpha() is not None:
            image = image.convert_alpha()
        else:
            image = image.convert()
        return image

