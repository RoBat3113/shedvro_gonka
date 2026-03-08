import textures
import pygame

class knopka:
    def __init__(self,x,y,w,z,bibka,ggggg):
        self.x = x
        self.y = y
        self.w = w
        self.z = z
        self.bibka = bibka # название текстуры от кнопки
        self.ggggg = ggggg # действие при нажатии

    def draw(self,scren):
        # показать текстуру кнопки
        textures.draw(self.bibka , self.x , self.y , scren)

        # отобразить хитбокс кнопки
        #                        R,G,B        x,y,w,h
        # pygame.draw.rect(scren, (255,81,36), (self.x,self.y,self.w,self.z), 3)
    
    def update(self, pos):
        mx = pos[0]
        my = pos[1]
        
        pt = self.x + self.w
        nt = self.y + self.z
        
        if mx in range(self.x, pt):
            if my in range(self.y,nt):
                self.ggggg()