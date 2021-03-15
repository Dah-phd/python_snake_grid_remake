import random


class snake:
    '''
    dims should be tuple with (rows, squares in row). Based on that will be made the filed
    for the snake. If the values are too small there may not be enough space for the 
    snake.
    '''

    def __init__(self, dims=(20, 40), init_lenght=3, set_food=False):
        self.dims = dims
        self.init_lenght = init_lenght
        self.set_food = set_food
        # self.field = [[0 for _ in range(self.dims[1])]
        #               for _ in range(self.dims[0])]

    def setup(self):
        '''
        Prepares the board for the snake
        '''
        self.alive = True
        self.snake = []
        for vert in range(self.init_lenght):
            self.snake.append((
                int(self.dims[0]/2+vert),
                int(self.dims[1]/2)
            ))
        self.face = 'up'
        self.score = 0
        self._make_food()

    def run(self):
        '''
        Should be called in the loop, triggering the motion of the snake 
        adn doing internal checks.
        '''
        self._colision()
        if self.alive:
            if self.humgry:
                self._move(False)
                self._make_food()
            else:
                self._move()
        self.turned = False

    def up(self):
        if self.face != 'down':
            self.face = 'up'
            self.turned = True

    def left(self):
        if self.face != 'right':
            self.face = 'left'
            self.turned = True

    def right(self):
        if self.face != 'left':
            self.face = 'right'
            self. turned = True

    def down(self):
        if self.face != 'up':
            self.face = 'down'
            self.turned = True

    def _make_food(self):
        position = random.randint(
            1,
            (self.dims[0]*self.dims[1]) - len(self.snake)
        )
        for row in range(self.dims[0]):
            for sq in range(self.dims[1]):
                if (row, sq) not in self.snake:
                    if position == 0:
                        self.food = (row, sq)
                        self.humgry = False
                        return
                    else:
                        position -= 1

    def _colision(self):
        if self.snake[0][0] >= self.dims[0] or self.snake[0][0] < 0 or self.snake[0][1] >= self.dims[1] or self.snake[0][1] < 0:
            self.alive = False
            return
        if self.snake[0] in self.snake[1:-1]:
            self.alive = False
            return
        if self.snake[0] == self.food:
            self.humgry = True
            self.score += 10

    def _move(self, remove=True):
        self.snake.insert(0, (
            self.snake[0][0]-1 if self.face == 'up' else
            self.snake[0][0] + 1 if self.face == 'down' else
            self.snake[0][0],
            self.snake[0][1]-1 if self.face == 'left' else
            self.snake[0][1] + 1 if self.face == 'right' else
            self.snake[0][1]
        ))
        if remove:
            self.snake.pop()
