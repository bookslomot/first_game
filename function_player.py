import pygame as pg

hight = 1150
width = 1920
scr = pg.display.set_mode([width, hight])


def wallk1(x, player, keyesr, keyesl):
    keys = pg.key.get_pressed()
    if keys[keyesr]:
        player.right = True
        player.left = False
        player.idle_right = True
        player.idle_left = False
        player.right_loop = True
        player.left_loop = False
        return x + player.step_x
    elif keys[keyesl]:
        player.left = True
        player.right = False
        player.idle_right = False
        player.idle_left = True
        player.left_loop = True
        player.right_loop = False
        return x - player.step_x
    else:
        player.anim_point = 0
        player.left = False
        player.right = False
        return x


# функуции с прыжком ставить перед самим прыжком


def jump(Player, Keyes, lift, barel_f):
    # прыжок 1
    keys = pg.key.get_pressed()
    if not Player.isJump:
        if keys[Keyes] and ((Player.y == hight - 200) or
                            (Player.y == 880 and barel_f.x - 30 <= Player.x + 64 <= barel_f.x + 80) or
                            (Player.y == 715 and 240 <= Player.x <= 300) or
                            (Player.y == 662 and -60 < Player.x <= 240) or
                            (Player.y == 705 and 1640 < Player.x <= width - 85) or
                            (Player.y == 168 and Player.x + 47 >= 270 and Player.x <= 590) or
                            (Player.y == 168 and 1050 <= Player.x + 47 <= 1110) or
                            (Player.y == 168 and 750 <= Player.x + 47 <= 810) or
                            (lift.y - 150 <= Player.y <= lift.y - 146 and lift.x - 70 <= Player.x <= lift.x + 143)):
            Player.isJump = True
    else:
        if Player.jumpCount >= 0:
            Player.y -= (Player.jumpCount ** 2) / 2
            Player.jumpCount -= 0.5
        else:
            Player.isJump = False
            Player.jumpCount = 10


def jump2(Player, Keyes):
    # прыжок 1
    keys = pg.key.get_pressed()
    if not Player.isJump:
        if keys[Keyes] and (Player.y == hight - 220):
            Player.isJump = True
    else:
        if Player.jumpCount >= 0:
            Player.y -= (Player.jumpCount ** 2) / 2
            Player.jumpCount -= 0.5
        else:
            Player.isJump = False
            Player.jumpCount = 10


def jump3(Player, Keyes, elevator):
    # прыжок 1
    keys = pg.key.get_pressed()
    if not Player.isJump:
        if keys[Keyes] and ((hight - 250 <= Player.y <= hight - 200) or
                            (elevator.y - 150 <= Player.y <= elevator.y - 146 and elevator.x - 80 <= Player.x <= elevator.x + 193) or
                            (Player.y == 552 and -100 <= Player.x <= 132) or
                            (Player.y == 352 and 1400 <= Player.x <= 1482) or
                            (Player.y == 202 and 1600 <= Player.x <= 1682) or
                            (Player.y == 2 and 1300 <= Player.x <= 1632) or
                            (Player.y == 2 and 900 <= Player.x <= 1220) or
                            (Player.y == 152 and 400 <= Player.x <= 482) or
                            (Player.y == 2 and 500 <= Player.x <= 932)
        ):
            Player.isJump = True
    else:
        if Player.jumpCount >= 0:
            Player.y -= (Player.jumpCount ** 2) / 2
            Player.jumpCount -= 0.5
        else:
            Player.isJump = False
            Player.jumpCount = 10


# упереться в пол и стены
def player_stop_x(x):
    if x >= 1920 - 130:
        return 1920 - 130
    elif x <= -58:
        return -58
    else:
        return x


def player_stop_y(y):
    if y >= 1150 - 200:
        return 1150 - 200
    elif y <= -47:
        return -47
    else:
        return y


# гравитация
def grav(y):
    if y < hight - 200:
        y += 2
        return int(y)
    else:
        return int(y)


def grav2(y):
    if y < hight - 220:
        y += 2
        return int(y)
    else:
        return int(y)


def grav3(y):
    if y <= hight - 220:
        y += 10
        return int(y)
    else:
        return int(y)


def looping(player, lift, barel_f):
    if ((player.y == hight - 200) or
                            (player.y == 880 and barel_f.x - 30 <= player.x + 64 <= barel_f.x + 80) or
                            (player.y == 715 and 240 <= player.x <= 300) or
                            (player.y == 662 and -60 < player.x <= 240) or
                            (player.y == 705 and 1640 < player.x <= width - 85) or
                            (player.y == 168 and player.x + 47 >= 270 and player.x <= 590) or
                            (player.y == 168 and 1050 <= player.x + 47 <= 1110) or
                            (player.y == 168 and 750 <= player.x + 47 <= 810) or
                            (lift.y - 150 <= player.y <= lift.y - 146 and lift.x - 70 <= player.x <= lift.x + 143)):
        player.loop = False
    else:
        player.loop = True


def looping2(player):
    if player.y == hight - 220:
        player.loop = False
    else:
        player.loop = True


def looping3(player, elevator):
    if ((hight - 250 <= player.y <= hight - 200) or
                            (elevator.y - 150 <= player.y <= elevator.y - 146 and elevator.x - 80 <= player.x <= elevator.x + 193) or
                            (player.y == 552 and -100 <= player.x <= 132) or
                            (player.y == 352 and 1400 <= player.x <= 1482) or
                            (player.y == 202 and 1600 <= player.x <= 1682) or
                            (player.y == 2 and 1300 <= player.x <= 1632) or
                            (player.y == 2 and 900 <= player.x <= 1220) or
                            (player.y == 152 and 400 <= player.x <= 482) or
                            (player.y == 2 and 500 <= player.x <= 932)

    ):
        player.loop = False
    else:
        player.loop = True


def animation(Player):
    if Player.anim_point + 1 >= 120:
        Player.anim_point = 0
    if Player.anim_loop_right + 1 >= 30:
        Player.anim_loop_right = 0
    if Player.anim_loop_left + 1 >= 30:
        Player.anim_loop_left = 0


# положение персонажа стоит бежит падает
def position_draw(Player):
    if Player.loop:
        if Player.right_loop:
            scr.blit(Player.JumpLoopRight[Player.anim_loop_right // 5], [Player.x, Player.y])
            Player.anim_loop_right += 1
        if Player.left_loop:
            scr.blit(Player.JumpLoopLeft[Player.anim_loop_left // 5], [Player.x, Player.y])
            Player.anim_loop_left += 1
    if Player.right and not Player.loop:
        scr.blit(Player.wallling_right[Player.anim_point // 5], [Player.x, Player.y])
        Player.anim_point += 1
    elif Player.left and not Player.loop:
        scr.blit(Player.wallling_left[Player.anim_point // 5], [Player.x, Player.y])
        Player.anim_point += 1
    elif Player.idle_right and not Player.loop:
        scr.blit(Player.idler, [Player.x, Player.y])
    elif Player.idle_left and not Player.loop:
        scr.blit(Player.idlel, [Player.x, Player.y])


class Player:
    """создание характеристик персонажа"""

    def __init__(self, x, y, step_x,
                 jumpCount, anim_point, anim_loop_right, anim_loop_left,
                 left, right, idle_left, idle_right, right_loop, left_loop, isJump, loop, wallking_right,
                 wallking_left, JumpLoopRight, JumpLoopLeft, idler, idlel):
        self.x = x
        self.y = y
        self.step_x = step_x
        self.jumpCount = jumpCount
        self.anim_point = anim_point
        self.anim_loop_right = anim_loop_right
        self.left = left
        self.right = right
        self.anim_loop_left = anim_loop_left
        self.idle_left = idle_left
        self.right_loop = right_loop
        self.left_loop = left_loop
        self.idle_right = idle_right
        self.isJump = isJump
        self.loop = loop
        self.wallling_right = wallking_right
        self.wallling_left = wallking_left
        self.JumpLoopRight = JumpLoopRight
        self.JumpLoopLeft = JumpLoopLeft
        self.idler = idler
        self.idlel = idlel