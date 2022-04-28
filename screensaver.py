import pygame as pg
from menu import menu
width = 1920
hight = 1150
running_0 = True
scr = pg.display.set_mode([width, hight])
back_round = pg.image.load("texture/DA_golem_by_arensh-d5vi281.jpg")


def draw():
    global running_0
    scr.blit(back_round, [0, 0])
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running_0 = False
        if event.type == pg.KEYDOWN:
            running_0 = False
    return True


def screen_saver():
    while running_0:
        draw()
        pg.display.flip()
    menu()


