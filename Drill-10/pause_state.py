import game_framework
import main_state
from pico2d import *


name = "PauseState"
image = None
blinktime = 0.01


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw():
    clear_canvas()
    game_framework.stack[1].grass.draw()
    game_framework.stack[1].boy.draw()
    if blinktime > 1.0:
        image.draw(400, 300)
    update_canvas()







def update():
    global blinktime

    delay(0.01)
    blinktime += 0.01

    if blinktime > 2.0:
        blinktime = 0.0


def pause():
    pass


def resume():
    pass