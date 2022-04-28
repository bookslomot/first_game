import help
import pygame as pg
width = 1920
hight = 1150
running_menu = True
running = False
clock = pg.time.Clock()
scr = pg.display.set_mode([width, hight])
back_round = pg.image.load("texture/tony-martinez-golen-small.jpg")
button_playNone = pg.image.load("texture/buttom_none.png")
button_play = pg.image.load("texture/buttom.png")
button_help = pg.image.load("texture/buttom_help.png")
button_help_act = pg.image.load("texture/buttom - копия.png")
but_exit = pg.image.load("texture/buttom_ exit.png")
but_exit_activ = pg.image.load("texture/buttom_exit_activ.png")
but_skrep = pg.image.load("texture/but_skrep.png")


def draw():
    global event, running_menu, running
    pos = pg.mouse.get_pos()
    clock.tick(120)
    scr.blit(back_round, [0, 0])
    scr.blit(but_skrep, [1400, 400])
    scr.blit(but_skrep, [1670, 400])
    scr.blit(button_playNone, [1300, 200])
    scr.blit(but_skrep, [1400, 700])
    scr.blit(but_skrep, [1670, 700])
    scr.blit(button_help, [1300, 500])
    scr.blit(but_exit, [1300, 800])
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if 1300 <= pos[0] <= 1800 and 200 <= pos[1] <= 436:
                running = True
                running_menu = False

            if 1300 <= pos[0] <= 1800 and 500 <= pos[1] <= 736:
                help.game_help()

            if 1300 <= pos[0] <= 1800 and 800 <= pos[1] <= 1036:
                running = True
                return False

    if 1300 <= pos[0] <= 1800 and 200 <= pos[1] <= 436:
        scr.blit(button_play, [1313, 200])
        return True
    if 1300 <= pos[0] <= 1800 and 500 <= pos[1] <= 736:
        scr.blit(button_help_act, [1313, 500])
    if 1300 <= pos[0] <= 1800 and 800 <= pos[1] <= 1036:
        scr.blit(but_exit_activ, [1313, 800])


def menu(running_menu):
    global running
    while running_menu:
        draw()
        pg.display.flip()
        if running:
            break
    return draw()


