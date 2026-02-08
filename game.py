import pygame
import pygame.mixer
import core
import car
import textures
import skald_gonshika
import komanda_tvicha
import random
import lan

class Game:
    def __init__(self):
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
        self.uploaded = None
        self.zov_timer = 0

    def update_server(self, dt, keys):
        from_client = ""
        if lan.use_lan:
            from_client = lan.upload_data()
            if from_client == '':
                return
            #print(f"from_client: {from_client}")
            #lan.send_data("test")
            commands = from_client.split('%')
            #print(f'commands: {commands}')
            for cmd in commands:
                if cmd == '':
                    continue
                params = cmd.split('=')
                if params[0] == 'key':
                    if params[1] == 'u': komanda_tvicha.kamni3()
                    if params[1] == 'l': komanda_tvicha.kamni34()
                    if params[1] == 'r': komanda_tvicha.kamni5()
                    if params[1] == 'd': komanda_tvicha.kamni6()
                    if params[1] == '1': komanda_tvicha.kamni7()
                    if params[1] == '2': komanda_tvicha.kamni8()

        # замедлить игрока в 10 раз
        if core.stop_me:
            dt *= 0.1
            core.stop_me = False
        
        if core.time_reverse:
            dt = -dt
            core.time_reverse = False

        self.p1.update(dt, keys)
        self.track.update(dt, self.p1)

        # пройтись по всем объектам карты
        for ne_kamen in self.track.blocks:
            # если врезались в пакень
            if self.p1.crash(ne_kamen.x,ne_kamen.y,80):
                self.p1.texture = "gg"
                ne_kamen.texture = "k3"

                # эпилепсия на фоне
                core.bg_color = (
                    random.randint(0,125),
                    random.randint(0,125),
                    random.randint(0,125))

                # не запускать новые звуки, пока время не придёт
                if self.zov_timer > 0:
                    break
                
                zov = pygame.mixer.Sound("infa/5.mp3")
                zo = pygame.mixer.Sound("infa/6.mp3")
                zov.set_volume(0.05)
                zo.set_volume(0.05)
                zo.play()
                zov.play()
                self.zov_timer = 60 * 33
                break # одного столкновения достаточно

            else: # никто не врезался
                core.bg_color = (64, 127, 127) # обычный цвет фона
                self.p1.texture = "ы" # ы

        # двигаем мир вокруг себя, но не себя самих - мы в центре мира
        self.p1.x = 0
        self.p1.y = 0
    
    def update_client(self, dt, keys):
        to_server = ""
        if keys[pygame.K_RIGHT]: to_server += "%key=r"
        if keys[pygame.K_LEFT]:  to_server += "%key=l"
        if keys[pygame.K_UP]:    to_server += "%key=u"
        if keys[pygame.K_DOWN]:  to_server += "%key=d"
        if keys[pygame.K_1]:     to_server += "%key=1"
        if keys[pygame.K_2]:     to_server += "%key=2"
        lan.send_data(to_server)
        #self.uploaded = lan.upload_data()

    def update(self, dt, keys):
        self.zov_timer -= 1

        if lan.is_server:
            self.update_server(dt, keys)
        else:
            self.update_client(dt, keys)
    
    def draw(self, screen):
        if lan.is_server:
            self.track.draw(screen)
            self.p1.draw(screen)
        else:
            print('client')
