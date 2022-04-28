from pygame .color import THECOLORS
from pygame import font
import pygame as pg


def game_help():
    pg.display.set_caption("Приключение големов")
    scrX = 1920
    scrY = 1150
    scr = pg.display.set_mode([scrX, scrY])

    pic = pg.image.load('texture/crack-brick-wall-black-background-2034695 — копия.jpg')  # Фон
    scr.blit(pic, (0, 0))  # Копирование фона на screen

    x_text = 540  # Положение текста
    y_text = 300  # Положение текста
    font = pg.font.Font(None, 30)  # Шрифт

    file = open("help.txt", "r")  # Открываем файл для чтения
    lines = file.readlines()  # аписываем строчки из файла в список lines
    file.close()
    long = len(lines)  # Количество строчек
    for i in range(0, long):
        st = lines[i]  # Строка
        d = len(st) - 1  # Длина строки без enter
        st = st[0:d]  # Строка без enter
        text = font.render(st, 1, THECOLORS['white'])
        scr.blit(text, [x_text, y_text])
        y_text = y_text + 40

    font2 = pg.font.Font(None, 60)
    text = font2.render('Press "Space" to come back', 1, THECOLORS['white'])
    scr.blit(text, [630, 1000])

    running = True
    while running:
        for event in pg.event.get():  # Просматриваем очередь событий
            if event.type == pg.KEYDOWN:  # Если нажата клавиша
                if event.key == pg.K_SPACE:
                    running = False

        pg.display.flip()

