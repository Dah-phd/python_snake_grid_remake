import pygame as pg
import snake_logic
import time
import subprocess
from sys import platform
if platform == 'linux':
    from os import setpgrp


class GUI:
    def __init__(self):
        self.game = snake_logic.snake()
        self.klok = pg.time.Clock()
        self.font = pg.font.SysFont('Courier New', 33, 'Bold')

    def main(self):
        self.game.setup()
        self.grid = pg.display.set_mode((800, 440))
        step = 6
        self.start = time.time()
        while True:
            if not self.game.alive:
                self.end()
                break
            self.klok.tick(60)
            self.grid.fill((0, 0, 0))
            if step == 0:
                step = 6
                self.game.run()
            else:
                step += -1
            self.controls()
            self.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
            pg.display.update()

    def controls(self):
        if pg.key.get_pressed()[pg.K_UP]:
            self.game.up()
        if pg.key.get_pressed()[pg.K_DOWN]:
            self.game.down()
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.game.left()
        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.game.right()

    def draw(self):
        for vert in self.game.snake:
            pg.draw.rect(self.grid, (20, 220, 20),
                         (vert[1]*20, vert[0]*20, 20, 20))
        pg.draw.rect(self.grid, (200, 20, 20),
                     (self.game.food[1]*20, self.game.food[0]*20, 20, 20))
        pg.draw.rect(self.grid, (20, 220, 20), (0, 400, 800, 40))
        self.grid.blit(self.font.render(
            'SCORE:', False, (0, 0, 0)), (500, 400))
        self.grid.blit(self.font.render(
            str(self.game.score), False, (0, 0, 0)), (700, 400))
        self.grid.blit(self.font.render(
            self.timer(), False, (0, 0, 0)), (40, 400))

    def end(self):
        if platform[:3] == 'win':
            subprocess.Popen(f'res\\terminal.py {self.game.score}', stdin=None, stdout=None, stderr=None, close_fds=True,
                             shell=True, creationflags=subprocess.DETACHED_PROCESS)
        else:
            subprocess.Popen(f'./res/terminal.py {self.game.score}', stdin=None, stdout=None, stderr=None, close_fds=True,
                             shell=True, preexec_fn=setpgrp)

    def timer(self):
        moment = time.time() - self.start
        sec = int(moment % 60)
        sec = ('0' + str(sec)) if sec < 10 else str(sec)
        mins = str(int(moment//60))
        return mins+':'+sec


if __name__ == '__main__':
    pg.init()
    start = GUI()
    start.main()
    pg.quit()
