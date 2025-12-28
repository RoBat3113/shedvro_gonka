import core
import textures
import random
import car

class Block:
    def __init__(self, wolrd_height, w=40, h=40):
        self.x = random.random() * core.screen_x
        self.y = random.random() * wolrd_height * -1
        self.w = w
        self.h = h
        self.texture = 'kamen'
    
    def move(self, dt, car: car.Car):
        self.x -= car.x 
        self.y -= car.y
    
    def draw(self, screen):
        textures.draw(self.texture, self.x + core.camera_x, self.y + core.camera_y, screen)

class Track:
    def __init__(self):
        self.length = 100000
        self.HP = 100
        self.max_speed = -600
        self.min_speed = 350
        self.max_blocks = 1000
        self.blocks = []

        for _ in range(self.max_blocks):
            self.blocks.append( Block(self.length) )
    
    def update(self, dt, car: car.Car):
        car.y -= self.min_speed * dt # добавляем постоянную скорость уровня

        # лимит на макс скросоть:
        if car.speed < self.max_speed:
            car.speed = self.max_speed

        for block in self.blocks:
            block.move(dt, car)
        
    
    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)
