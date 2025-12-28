import pygame
import pygame.mixer
import core
import car
import textures
import skald_gonshika
import random
import lan

class Game:
    def __init__(self):
        lan.init()

        textures.bimport("ы", "infa/ы.png")
        textures.bimport("r", "infa/r.png")
        textures.bimport("l", "infa/l.png")
        textures.bimport("kamen", "infa/kamen.png")
        textures.bimport("k3", "infa/k3.png")
        textures.bimport("г", "infa/г.png")
        textures.bimport("gg", "infa/gg.png")
        pygame.mixer.init()
        self.p1 = car.Batmobile()
        self.track = skald_gonshika.Track()

    def update(self, dt, keys):
        self.p1.update(dt, keys)
        self.track.update(dt, self.p1)
        for ne_kamen in self.track.blocks:
            if self.p1.crash(ne_kamen.x,ne_kamen.y,80):
                self.p1.texture = "gg"  
                zov = pygame.mixer.Sound("infa/5.mp3")
                zo = pygame.mixer.Sound("infa/6.mp3")
                zo.play()
                zov.play()
                ne_kamen.texture = "k3"  
                break
            else:
                self.p1.texture = "ы"
        self.p1.x = 0
        self.p1.y = 0
        core.bg_color = (random.randint(0,125),random.randint(0,125),random.randint(0,125))
    
    def draw(self, screen):
        self.track.draw(screen)
        self.p1.draw(screen)
