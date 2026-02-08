import core
import random

def kamni3():
    core.running = False
    quit("вылет")
#/\по желанию второго игрока у первого игрока может вылететь игра  
def kamni34():
    "spy"
#/\делает камень шпион, если на него наехать игра вылетает
def kamni5():
    core.stop_me = True
#
def kamni6():
    offset = 10
    core.camera_x += random.randint(-offset, offset)
    core.camera_y += random.randint(-offset, offset)

def kamni7():
    core.camera_x = core.screen_x / 2
    core.camera_y = core.screen_y / 2

def kamni8():
    core.time_reverse = True

