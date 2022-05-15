import os, sys
import time

import pygame as pg
from BoardClass import Board
from MediaManagerClass import MediaManager
from GameLogicClass import GameLogic
from GameLogicClass import PlayerType

SECTOR_SIZE = 100
class GameManager():
    def __init__(self, columns, rows, inarow, player1, player2):
        self.board = Board(columns, rows, inarow)
        self.game_logic = GameLogic(self.board, player1, player2)
        screen_size_w = SECTOR_SIZE * columns
        screen_size_h = SECTOR_SIZE * rows
        self.media_manager = MediaManager(screen_size_w, screen_size_h, self.board, SECTOR_SIZE)
        self.clock = pg.time.Clock()

    def run(self):
        going = True
        game_over = False

        while going:
            self.clock.tick(60)
            # если текущий игрок бот - делаем ход и немного отдыхаем
            if not game_over and self.game_logic.if_current_player_is_bot():
                self.game_logic.MakeTurn()
                time.sleep(1)

            if self.game_logic.player_wins != 0:
                self.media_manager.set_winnner(self.game_logic.player_wins)
                game_over = True

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    going = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    going = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if not self.game_logic.if_current_player_is_bot() and not game_over:
                        pos = pg.mouse.get_pos()
                        self.game_logic.MakeTurn(int(pos[0] / SECTOR_SIZE))


            self.media_manager.update_graphics()

    def run_trainnig(self, epochs):
        player_1_wins = 0
        player_2_wins = 0
        draws = 0
        for i in range(epochs):
            going = True
            game_over = False
            self.game_logic.reset()
            print(str(self.game_logic.players[0]['type']) + " vs " + str(self.game_logic.players[1]['type']))
            while not game_over:
                if not game_over:
                    self.game_logic.MakeTurn()
                if self.game_logic.is_draw:
                    print("Draw " + str(i + 1) + "epoch of " + str(epochs))
                    draws += 1
                    game_over = True
                if self.game_logic.player_wins != 0:
                    game_over = True
                    print(str(self.game_logic.players[self.game_logic.player_wins - 1]['type']) + " WIN!" + str(
                        i + 1) + "epoch of " + str(epochs))
                    if self.game_logic.player_wins == 1:
                        player_1_wins += 1
                    else:
                        player_2_wins += 1
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        return
                    elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        return
        print(str(self.game_logic.players[0]['type']) + " wins: " + str(player_1_wins) + ", " + str(self.game_logic.players[1]['type']) + " wins: " + str(player_2_wins))
        print("draws:" + str(draws))



game_manager_class = GameManager(7, 6, 4, PlayerType.AGENT_ONE_STEP_AHEAD, PlayerType.AGENT_N_STEP_AHEAD)
#game_manager_class.run()
game_manager_class.run_trainnig(6)