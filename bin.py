import pygame as pg
from res import snake_logic, scoring, pg_inputbox


class GUI:
    def __init__(self):
        self.game = snake_logic.snake()
        self.klok = pg.time.Clock()

    def main(self):
        pg.init()
        self.run = True
        self.game.setup()
        self.grid = pg.display.set_mode((800, 400))
        step = 6
        while self.run:
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
            pg.draw.rect(self.grid, (200, 200, 200),
                         (vert[1]*20, vert[0]*20, 20, 20))
        pg.draw.rect(self.grid, (0, 200, 200),
                     (self.game.food[1]*20, self.game.food[0]*20, 20, 20))


if __name__ == '__main__':
    start = GUI()
    start.main()
