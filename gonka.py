import pygame
import game
import core
import pygame.mixer
#import font
#import lan

#lan.init()

screen = pygame.display.set_mode((core.screen_x, core.screen_y), vsync=0)
clock = pygame.time.Clock()
g = game.Game()
#font.load_fonts()

# основной цикл игры
while core.running:
    # цикл обработки событий из Pygame
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                core.running = False
        if event.type == pygame.QUIT:
            core.running = False

    keys = pygame.key.get_pressed()
    g.update(1.0/core.max_fps, keys)
    
    screen.fill(core.bg_color) # залить экран цветом
    g.draw(screen)
    pygame.display.flip() # показать кадр на экране
    clock.tick(core.max_fps) # скорость игры
pygame.quit()
