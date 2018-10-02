from pico2d import *
import random
open_canvas()
grass = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def run_anim_dot_to_dot(x1, y1, x2, y2):
    animkind = 0
    if x2 > x1:
        animkind  = 1
    movecnt = 0
    frame = 0
    radian = math.atan2(x2 - x1, y2 - y1) // 3.14 * 180
    while movecnt < 10:
        clear_canvas()
        grass.draw(400, 300)

        xposition = (x2 - x1) / 10 * movecnt + x1
        yposition = (y2 - y1) / 10 * movecnt + y1

        character.clip_draw(frame * 100, animkind * 100, 100, 100, xposition, yposition)
        update_canvas()

        frame = (frame + 1) % 8
        movecnt += 1
        delay(0.05)

running = True
randomxs = [random.randint(0,800) for n in range(20)]
randomys = [random.randint(0,600) for n in range(20)]

size = len(randomxs)
n = 1
while running:
    run_anim_dot_to_dot(randomxs[n-1],randomys[n-1],randomxs[n],randomys[n])
    n = ( n + 1) % size

    handle_events()


close_canvas()