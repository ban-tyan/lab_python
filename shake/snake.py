import pygame
from random import randrange

# Custom exceptions
class GameOverException(Exception):
    pass

class Game:
    RES = 800
    SIZE = 40
    FPS = 6

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode([self.RES, self.RES])
        self.clock = pygame.time.Clock()
        self.font_score = pygame.font.SysFont('Arial', 26, bold=True)
        self.font_end = pygame.font.SysFont('Arial', 66, bold=True)
        self.score = 0
        self.snake_speed = 10
        self.snake = Snake(self.SIZE, self.RES)
        self.apple = Apple(self.SIZE, self.RES)

    def draw_elements(self):
        self.surface.fill(pygame.Color('black'))
        for segment in self.snake.body:
            pygame.draw.rect(self.surface, pygame.Color('green'), (segment[0], segment[1], self.SIZE - 1, self.SIZE - 1))
        pygame.draw.rect(self.surface, pygame.Color('red'), (self.apple.position[0], self.apple.position[1], self.SIZE, self.SIZE))
        render_score = self.font_score.render(f'SCORE: {self.score}', 1, pygame.Color('orange'))
        self.surface.blit(render_score, (5, 5))

    def check_collision(self):
        if self.snake.head == self.apple.position:
            self.apple.respawn(self.snake.body)
            self.snake.grow()
            self.score += 1
            self.snake_speed = max(self.snake_speed - 1, 4)
        if self.snake.is_collision():
            raise GameOverException

    def game_over(self):
        render_end = self.font_end.render('GAME OVER', 1, pygame.Color('orange'))
        self.surface.blit(render_end, (self.RES // 2 - 200, self.RES // 3))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        exit()

    def run(self):
        while True:
            try:
                self.handle_events()
                self.snake.move()
                self.check_collision()
                self.draw_elements()
                pygame.display.flip()
                self.clock.tick(self.FPS)
            except GameOverException:
                self.game_over()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        self.snake.update_direction(keys)

class Snake:
    def __init__(self, size, res):
        self.size = size
        self.res = res
        self.length = 1
        self.body = [(randrange(size, res - size, size), randrange(size, res - size, size))]
        self.dx, self.dy = 0, 0
        self.dirs = {'W': True, 'S': True, 'A': True, 'D': True}

    @property
    def head(self):
        return self.body[-1]

    def move(self):
        x, y = self.head
        x += self.dx * self.size
        y += self.dy * self.size
        self.body.append((x, y))
        self.body = self.body[-self.length:]

    def grow(self):
        self.length += 1

    def update_direction(self, keys):
        if keys[pygame.K_w] and self.dirs['W']:
            self.dx, self.dy = 0, -1
            self.dirs = {'W': True, 'S': False, 'A': True, 'D': True}
        elif keys[pygame.K_s] and self.dirs['S']:
            self.dx, self.dy = 0, 1
            self.dirs = {'W': False, 'S': True, 'A': True, 'D': True}
        elif keys[pygame.K_a] and self.dirs['A']:
            self.dx, self.dy = -1, 0
            self.dirs = {'W': True, 'S': True, 'A': True, 'D': False}
        elif keys[pygame.K_d] and self.dirs['D']:
            self.dx, self.dy = 1, 0
            self.dirs = {'W': True, 'S': True, 'A': False, 'D': True}

    def is_collision(self):
        x, y = self.head
        return (x < 0 or x >= self.res or y < 0 or y >= self.res or len(self.body) != len(set(self.body)))

class Apple:
    def __init__(self, size, res):
        self.size = size
        self.res = res
        self.position = self.random_position()

    def random_position(self):
        return randrange(self.size, self.res - self.size, self.size), randrange(self.size, self.res - self.size, self.size)

    def respawn(self, snake_body):
        while True:
            new_position = self.random_position()
            if new_position not in snake_body:
                self.position = new_position
                break

if __name__ == "__main__":
    game = Game()
    game.run()
