from pico2d import *
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
    while movecnt < 50:
        clear_canvas()
        grass.draw(0, 0)

        xposition = (x2 - x1) / 50 * movecnt + x1
        yposition = (y2 - y1) / 50 * movecnt + y1

        character.clip_draw(frame * 100, animkind * 100, 100, 100, xposition, yposition)
        update_canvas()

        frame = (frame + 1) % 8
        movecnt += 1
        delay(0.05)

running = True

while running:
    run_anim_dot_to_dot(203,535,132,243)
    run_anim_dot_to_dot(132,243,535,470)
    run_anim_dot_to_dot(535,470,477,203)
    run_anim_dot_to_dot(477,203,715,136)
    run_anim_dot_to_dot(715,136,316,225)
    run_anim_dot_to_dot(316,225,510,92)
    run_anim_dot_to_dot(510,92,692,518)
    run_anim_dot_to_dot(692,518,682,336)
    run_anim_dot_to_dot(682,336,712,349)
    run_anim_dot_to_dot(712,349,203,535)

    handle_events()


close_canvas()