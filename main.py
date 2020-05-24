import pygame
import pygame_menu
from snake import *
from game import *
from linked_list import *
from pygame.locals import *
import sys
def update_render(game, window):
    window.fill((0,0,0))
    it = game.snake.pos.first
    while it != None:
        pygame.draw.rect(window, (255, 255, 255), (it.item[0] * 10, it.item[1] * 10, 10, 10))
        it = it.next
    for food in game.foods:
        pygame.draw.circle(window, (255, 0, 0), (food[0]*10+5, food[1]*10+5), 5)
    pygame.display.flip()

def gameloop(window):
    game = Game()
    clock = pygame.time.Clock()
    eat_sound = pygame.mixer.Sound("resources/eat_apple.wav")
    running = True
    next_food = pygame.time.get_ticks() + 5000
    while running:
        dir_change = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and not dir_change:
                if event.key == K_UP:
                    dir_change = game.snake.turn(Direction.N)
                elif event.key == K_RIGHT:
                    dir_change = game.snake.turn(Direction.E)
                elif event.key == K_DOWN:
                    dir_change = game.snake.turn(Direction.S)
                elif event.key == K_LEFT:
                    dir_change = game.snake.turn(Direction.W)
        i = game.snake.update()
        if i == 0:
            running = False
        else :
            if i == 2:
                game.foods.remove(game.snake.pos.first.item)
                eat_sound.play()
            actual = pygame.time.get_ticks()
            if actual >= next_food or len(game.foods) == 0:
                game.add_food()
                if actual >=next_food:
                    next_food = pygame.time.get_ticks() + 5000
            update_render(game, window)
            clock.tick(game.snake.speed)
def menu(window):
    menu = pygame_menu.Menu(400, 400, 'Menu', onclose=pygame_menu.events.EXIT ,theme=pygame_menu.themes.THEME_DARK)
    menu.add_button('Play', gameloop, window)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(window)
def main():
    pygame.init()
    pygame.display.set_caption("Snake")
    window = pygame.display.set_mode((400, 400))
    menu(window)

if __name__ == '__main__':
    main()
