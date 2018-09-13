from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
dir = 0
frame = 0
while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, dir * 100, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    if x > 700:
        dir = 0
    elif x < 100:
        dir = 1
    if dir == 1:
        x += 5
    elif dir == 0:
        x -= 5
    delay(0.05)
    get_events()


close_canvas()

