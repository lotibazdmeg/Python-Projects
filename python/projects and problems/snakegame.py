import pygame
import random

# initialize Pygame
pygame.init()

# game settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 7

# create the game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# set the game window title
pygame.display.set_caption('Snake Game')

# set the game clock
clock = pygame.time.Clock()

# define the Snake class
class Snake:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.dx = CELL_SIZE
        self.dy = 0
        self.body = []
        self.length = 1

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x < 0:
            self.x = WINDOW_WIDTH - CELL_SIZE
        elif self.x >= WINDOW_WIDTH:
            self.x = 0

        if self.y < 0:
            self.y = WINDOW_HEIGHT - CELL_SIZE
        elif self.y >= WINDOW_HEIGHT:
            self.y = 0

        # check for collisions with the Snake's body
        for segment in self.body[1:]:
            if self.x == segment[0] and self.y == segment[1]:
                pygame.quit()
                quit()

        self.body.insert(0, (self.x, self.y))

        if len(self.body) > self.length:
            self.body.pop()


    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(game_window, SNAKE_COLOR, (x, y, CELL_SIZE, CELL_SIZE))

    def handle_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.dx == 0:
                self.dx = -CELL_SIZE
                self.dy = 0
            elif event.key == pygame.K_RIGHT and self.dx == 0:
                self.dx = CELL_SIZE
                self.dy = 0
            elif event.key == pygame.K_UP and self.dy == 0:
                self.dx = 0
                self.dy = -CELL_SIZE
            elif event.key == pygame.K_DOWN and self.dy == 0:
                self.dx = 0
                self.dy = CELL_SIZE

    def eat_food(self, food_x, food_y):
        if self.x == food_x and self.y == food_y:
            self.length += 1
            return True

        return False

# define the Food class
class Food:
    def __init__(self):
        self.x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1) * CELL_SIZE
        self.y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1) * CELL_SIZE

    def draw(self):
        pygame.draw.rect(game_window, FOOD_COLOR, (self.x, self.y, CELL_SIZE, CELL_SIZE))

    def respawn(self):
        self.x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1) * CELL_SIZE
        self.y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1) * CELL_SIZE

# create the Snake and Food objects
snake = Snake()
food = Food()

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            snake.handle_keys(event)

    # move the Snake
    snake.move()

    # check if the Snake eats the Food
    if snake.eat_food(food.x, food.y):
      food.respawn()

    game_window.fill(BACKGROUND_COLOR)

    snake.draw()
    food.draw()


    pygame.display.update()

    clock.tick(FPS)

pygame.quit()