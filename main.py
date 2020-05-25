import pygame
import pygame_menu
from snake import *
from game import *
from linked_list import *
from pygame.locals import *
import sys
font = None
name_input = None
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
def update_render(game, window):

    window.fill((0,0,0))
    # pygame.draw.line(window, blue, (0, 404), (400, 404), 10)
    pygame.draw.rect(window, blue, (0, 400, 400, 100))

    it = game.snake.pos.first
    while it != None:
        pygame.draw.rect(window, white, (it.item[0] * 10, it.item[1] * 10, 10, 10))
        it = it.next
    for food in game.foods:
        pygame.draw.circle(window, (255, 0, 0), (food[0]*10+5, food[1]*10+5), 5)
    score_disp = font.render("Score " + str(game.snake.score), False, black)
    high_score = max(Score.score.get_highest(), game.snake.score)
    high_score_disp = font.render("High Score " + str(high_score), False, black)
    window.blit(high_score_disp, (10, 450))
    window.blit(score_disp, (10, 410))
    pygame.display.flip()


def gameloop(window):
    name = name_input.get_value()
    game = Game()
    clock = pygame.time.Clock()
    eat_sound = pygame.mixer.Sound("resources/eat_apple.wav")
    running = True
    next_food = pygame.time.get_ticks() + 5000
    while running:
        dir_change = False
        for event in pygame.event.get():
            if event.type == QUIT:
                Score.score.add_score(name, game.snake.score)
                exit()
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
            Score.score.add_score(name, game.snake.score)
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
    global name_input
    menu = pygame_menu.Menu(500, 400, 'Menu', onclose=exit ,theme=pygame_menu.themes.THEME_DARK)
    name_input = menu.add_text_input('Name: ', maxchar=10)
    menu.add_button('Play', gameloop, window)
    menu.add_button('Quit', exit)
    menu.mainloop(window)


def exit():
    Score.score.save_score()
    pygame_menu.events.EXIT
    pygame.quit()
    sys.exit()


def main():
    Score.init_score()
    pygame.init()
    global font
    font = pygame.font.Font('resources/INVASION2000.TTF', 30)
    pygame.display.set_caption("Snake")
    window = pygame.display.set_mode((400, 500))
    menu(window)

if __name__ == '__main__':
    main()
