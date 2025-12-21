import pygame

textures = {}

# загружает текстуру с диска
def bimport(name, path): 
    global textures
    textures[name] = pygame.image.load(path)  

# рисует текстуру
def draw(name, x, y, screen):
    global textures
    screen.blit(textures[name], (x, y))  