from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 640, 480

def run_anim_dot_to_dot(x1, y1, x2, y2):
    global characterx, charactery
    global animkind
    global movecnt
    if x2 > x1:
        animkind = 1
    else:
        animkind = 0
    if movecnt < 50:
        characterx = (x2 - x1) / 50 * movecnt + x1
        charactery = (y2 - y1) / 50 * movecnt + y1
        movecnt += 1

def handle_events():
    global startx, starty
    global running
    global x, y
    global destx, desty
    global moving
    global movecnt
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                movecnt = 0
                moving = True
                destx, desty = event.x, KPU_HEIGHT - 1 - event.y + 25
                startx, starty = characterx, charactery

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursorimg = load_image('hand_arrow.png')

movecnt = 0
moving = False
running = True
animkind = 3
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
destx, desty = KPU_WIDTH // 2, KPU_HEIGHT // 2
startx, starty = KPU_WIDTH // 2, KPU_HEIGHT // 2
characterx, charactery = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursorimg.draw(x + 25, y - 25)
    character.clip_draw(frame * 100, 100 * animkind, 100, 100, characterx, charactery)
    update_canvas()
    frame = (frame + 1) % 8

    if moving == True:
        run_anim_dot_to_dot(startx,starty,destx,desty)

    delay(0.02)
    handle_events()
    if movecnt == 50:
        moving = False
        movecnt = 0
        if animkind == 0:
            animkind = 2
        elif animkind == 1:
            animkind = 3

close_canvas()