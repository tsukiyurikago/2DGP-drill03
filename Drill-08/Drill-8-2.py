from pico2d import *
import random
open_canvas()
grass = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

global n

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def run_anim_dot_to_dot(x1, y1, x2, y2, x3, y3, x4, y4):
    animkind = 0
    if x3 > x2:
        animkind  = 1
    movecnt = 0
    frame = 0
    #p1-p2
#    for i in range(0,50,2):
 #       clear_canvas()
  #      grass.draw(400, 300)
#
 #       t = i / 100
  #      xposition = (2*t**2-3*t+1)*x1+(-4*t**2+4*t)*x2+(2*t**2-t)*x3
   #     yposition = (2*t**2-3*t+1)*y1+(-4*t**2+4*t)*y2+(2*t**2-t)*y3
#
 #       character.clip_draw(frame * 100, animkind * 100, 100, 100, xposition, yposition)
  #      update_canvas()
#
 #       frame = (frame + 1) % 8
  #      movecnt += 1
   #     delay(0.05)

    #p2-p3
    for i in range(0,100,2):
        clear_canvas()
        grass.draw(400, 300)

        t = i / 100
        xposition = ((-t**3+2*t**2-t)*x1+(3*t**3-5*t**2+2)*x2+(-3*t**3+4*t**2+t)*x3+(t**3-t**2)*x4)/2
        yposition = ((-t**3+2*t**2-t)*y1+(3*t**3-5*t**2+2)*y2+(-3*t**3+4*t**2+t)*y3+(t**3-t**2)*y4)/2

        global randomxs
        global randomys
        global cnt

        for i in range(3,cnt):
            if(cnt<10):
                character.clip_draw(1 * 100, 1 * 100, 100, 100, randomxs[i], randomys[i])
            else:
                character.clip_draw(1 * 100, 1 * 100, 100, 100, randomxs[i-10], randomys[i-10])


        character.clip_draw(frame * 100, animkind * 100, 100, 100, xposition, yposition)
        update_canvas()

        frame = (frame + 1) % 8
        movecnt += 1
        delay(0.05)

    #p3-p4
#    for i in range(50,100,2):
 #       clear_canvas()
  #      grass.draw(400, 300)
#
 #       t = i / 100
  #      xposition = (2*t**2-3*t+1)*x2+(-4*t**2+4*t)*x3+(2*t**2-t)*x4
   #     yposition = (2*t**2-3*t+1)*y2+(-4*t**2+4*t)*y3+(2*t**2-t)*y4
#
 #       character.clip_draw(frame * 100, animkind * 100, 100, 100, xposition, yposition)
  #      update_canvas()
#
 #       frame = (frame + 1) % 8
  #      movecnt += 1
   #     delay(0.05)


running = True
randomxs = [random.randint(0,800) for n in range(10)]
randomys = [random.randint(0,600) for n in range(10)]

size = len(randomxs)
cnt = 3
n = 1
while running:
    if(n+3<10):
        run_anim_dot_to_dot(randomxs[n],randomys[n],randomxs[n+1],randomys[n+1],randomxs[n+2],randomys[n+2],randomxs[n+3],randomys[n+3])
        if(cnt<13):
            cnt = cnt + 1
    elif(n==7):
        run_anim_dot_to_dot(randomxs[n],randomys[n],randomxs[n+1],randomys[n+1],randomxs[n+2],randomys[n+2],randomxs[0],randomys[0])
        if(cnt<13):
            cnt = cnt + 1
    elif(n==8):
        run_anim_dot_to_dot(randomxs[n],randomys[n],randomxs[n+1],randomys[n+1],randomxs[0],randomys[0],randomxs[1],randomys[1])
        if(cnt<13):
            cnt = cnt + 1
    elif(n==9):
        run_anim_dot_to_dot(randomxs[n],randomys[n],randomxs[0],randomys[0],randomxs[1],randomys[1],randomxs[2],randomys[2])
        if(cnt<13):
            cnt = cnt + 1

    n = ( n + 1) % size


    handle_events()


close_canvas()