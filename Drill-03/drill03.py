import os
os.chdir('g:\\me\\2018autumn\\py\\2018-2DGP\\Labs\\Lecture03')
from pico2d import *
open_canvas()
character=load_image('character.png')
x=100
y=100
degree=0
dir=0
import math

while(1):
    if dir==0:
        x= x+10
    elif dir==1:
        y=y+10
    elif dir==2:
        x=x-10
    elif dir==3:
        y=y-10
    elif dir==4:
        if degree>360:
            degree=0
        if degree==269:
            dir=0
        degree=degree+1
        x=200*math.cos(degree*3.14/180)+400
        y=200*math.sin(degree*3.14/180)+300
    if x==400 and y==100:
        dir=4
        degree=270
    if dir!=4:
        if x>700:
            dir=1
            x=700
        if y>500:
            dir=2
            y=500
        if x<100:
            dir=3
            x=100
        if y<100:
            dir=0
            y=100
    clear_canvas_now()
    character.draw_now(x,y)
    delay(0.01)

close_canvas()
