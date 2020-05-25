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
clock = None
def update_render(game, window):

    window.fill(black)

    it = game.snake.pos.first
    while it != None:
        pygame.draw.rect(window, white, (it.item[0] * 10, it.item[1] * 10, 10, 10))
        it = it.next
    for food in game.foods:
        pygame.draw.circle(window, (255, 0, 0), (food[0]*10+5, food[1]*10+5), 5)
    score_display(game, window)
    pygame.display.flip()

def score_display(game, window):
    pygame.draw.rect(window, blue, (0, 400, 400, 100))
    score_disp = font.render("Score " + str(game.snake.score), False, black)
    high_score = max(Score.score.get_highest(), game.snake.score)
    high_score_disp = font.render("High Score " + str(high_score), False, black)
    window.blit(high_score_disp, (10, 450))
    window.blit(score_disp, (10, 410))


def gameloop(window):
    global clock
    name = name_input.get_value()
    if len(name) == 0:
        name = 'Unknown'
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
            Score.score.save_score()
            game_over(game, window)
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
    menu.add_button('Scores', score_menu, window)
    menu.add_button('Reset Scores', Score.reset_scores)
    menu.add_button('Quit', exit)
    menu.mainloop(window)

def score_menu(window):
    global font
    score_menu = pygame_menu.Menu(500, 400, 'Scores', onclose=pygame_menu.events.BACK, theme=pygame_menu.themes.THEME_DARK)
    for name, score in Score.score.scores:
        score_menu.add_label(name + " " +  str(score), font_size=20, font_name=pygame_menu.font.FONT_8BIT, font_color=(255, 0, 0))
    score_menu.mainloop(window)


def game_over(game, window):
    global clock
    window.fill(black)
    game_over_disp = font.render("GAME OVER", False, white)
    window.blit(game_over_disp, (90, 180))
    score_display(game, window)
    pygame.display.flip()
    game_over_sound = pygame.mixer.Sound("resources/game_over.wav")
    game_over_sound.play()
    exit = pygame.time.get_ticks() + 3000
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN and event.key == K_RETURN:
                return
        if pygame.time.get_ticks() >= exit:
            return
        pygame.display.flip()
        clock.tick(30)




def exit():
    Score.score.save_score()
    pygame_menu.events.EXIT
    pygame.quit()
    sys.exit()


def main():
    Score.init_score()
    pygame.init()
    global font
    font = pygame.font.Font(pygame_menu.font.FONT_8BIT, 25)
    pygame.display.set_caption("Snake")
    window = pygame.display.set_mode((400, 500))
    menu(window)

if __name__ == '__main__':
    main()
