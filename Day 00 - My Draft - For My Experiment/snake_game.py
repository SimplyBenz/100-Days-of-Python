import curses
import random
import time

class Snake:
    def __init__(self, window):
        self.window = window
        self.snake = [(10, 10), (10, 9), (10, 8)]
        self.direction = curses.KEY_RIGHT
        self.food = self.generate_food()
        self.score = 0

    def generate_food(self):
        while True:
            food = (random.randint(1, curses.LINES-2), random.randint(1, curses.COLS-2))
            if food not in self.snake:
                return food

    def draw(self):
        self.window.clear()
        self.window.border(0)
        self.window.addch(self.food[0], self.food[1], curses.ACS_PI)
        for y, x in self.snake:
            self.window.addch(y, x, curses.ACS_CKBOARD)
        self.window.addstr(0, 2, f'Score: {self.score}')
        self.window.refresh()

    def move(self):
        head = self.snake[0]
        y, x = head
        if self.direction == curses.KEY_UP:
            y -= 1
        elif self.direction == curses.KEY_DOWN:
            y += 1
        elif self.direction == curses.KEY_LEFT:
            x -= 1
        elif self.direction == curses.KEY_RIGHT:
            x += 1

        new_head = (y, x)

        if (y, x) == self.food:
            self.snake.insert(0, new_head)
            self.food = self.generate_food()
            self.score += 1
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()

    def check_collision(self):
        head = self.snake[0]
        y, x = head

        if y == 0 or y == curses.LINES - 1 or x == 0 or x == curses.COLS - 1:
            return True

        if head in self.snake[1:]:
            return True

        return False

    def run(self):
        self.window.timeout(100)
        while True:
            self.draw()
            key = self.window.getch()
            if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
                self.direction = key
            self.move()
            if self.check_collision():
                break
            time.sleep(0.1)

        self.window.addstr(curses.LINES // 2, curses.COLS // 2 - 5, 'GAME OVER')
        self.window.refresh()
        time.sleep(2)

def main(stdscr):
    curses.curs_set(0)
    snake_game = Snake(stdscr)
    snake_game.run()

if __name__ == '__main__':
    curses.wrapper(main)