import pygame
import core
import textures
import math
# коробка для столкновения с тачкой
class Hitbox:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

# базовый класс для тачки
class Car:
    def crash(self,x,y,r=20):
        if abs(self.x - x) < r:
            if abs(self.y - y) < r:
                return True
        return False 
        

        
    def __init__(self):
        self.hitbox = Hitbox(0, 0, 20, 40)
        self.speed = 0
        self.acceleration = 100 # ускорение
        self.force = 100        # тормоза
        self.control_speed = 250
        self.x = 0 
        self.y = 0
        self.hp = 10
        self.texture = None
        self.texturer = None
        self.texturel = None
        self.name = "Noname"
    
    def update(self, dt, keys):
        if keys[pygame.K_UP]:    
            self.texture =  "ы"
            self.speed -= self.acceleration * dt
        if keys[pygame.K_DOWN]:  self.speed += self.force * dt
        if keys[pygame.K_RIGHT]: 
            self.texture =  self.texturel
            self.x += self.control_speed * dt
        if keys[pygame.K_LEFT]:  
            self.texture =  self.texturer
            self.x -= self.control_speed * dt
        self.y += self.speed * dt
        print(f"скорость: {self.speed}")

    def draw(self, screen):
        self.hitbox.x = self.x
        self.hitbox.y = self.y
        if (self.texture == None):
            pygame.draw.rect(screen, (128,128,0), (self.hitbox.x, self.hitbox.y, self.hitbox.w, self.hitbox.h))
        else:
            textures.draw(self.texture, self.x + core.camera_x, self.y + core.camera_y, screen)

class Batmobile(Car):
    def __init__(self):
        super().__init__()
        self.name = "Бэтмобиль"
        self.texture = "ы"
        self.texturer = "r"
        self.texturel = "l"
    
class Badmobile(Car):
    pass
