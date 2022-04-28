import random
import function_player
import pygame as pg
from function_player import Player
import time
import score
width = 1920
hight = 1150




class FlagArg:
    def __init__(self, running3, lever1, lever2, lever3, end):
        self.running3 = running3
        self.lever1 = lever1
        self.lever2 = lever2
        self.lever3 = lever3
        self.end = end


class lift:
    """ливт, вправо влево, вверх, влево """

    def __init__(self, x, y, right, left, left_player, up, down, left_end, texture):
        self.x = x
        self.y = y
        self.right = right
        self.left = left
        self.up = up
        self.left_end = left_end
        self.texture = texture
        self.left_player = left_player
        self.down = down


class Lava_down:
    """лава поднимается снизу вверх"""

    def __init__(self, x, y, texture):
        self.x = x
        self.y = y
        self.texture = texture


class Kapli:
    """капли, которые падают вниз"""

    def __init__(self, x, y, texture):
        self.x = x
        self.y = y
        self.texture = texture


def lets_go3():
    class magma:
        """"создание стольца магмы"""

        def __init__(self, x, y, anim_point, potok):
            self.x = x
            self.y = y
            self.potok = potok
            self.anim_point = anim_point

    kapli1 = Kapli(random.randint(50, 800), random.randint(-100, 0), "texture/Liquidlavaicon.png")
    kapli2 = Kapli(random.randint(50, 800), random.randint(-100, 0), "texture/Liquidlavaicon.png")
    kapli3 = Kapli(random.randint(50, 800), random.randint(-100, 0), "texture/Liquidlavaicon.png")
    kapli4 = Kapli(random.randint(1000, 1920), random.randint(-100, 0), "texture/Liquidlavaicon.png")
    kapli5 = Kapli(random.randint(1000, 1920), random.randint(-100, 0), "texture/Liquidlavaicon.png")
    kapli6 = Kapli(random.randint(1000, 1920), random.randint(-100, 0), "texture/Liquidlavaicon.png")
    lava_down = Lava_down(0, hight, pg.image.load("texture/2d-lava-clipart-2-removebg-preview.png"))
    elevator = lift(200, 850, True, False, False, False, False, False, pg.image.load("texture/lift_lvl3.png"))
    flagarg = FlagArg(True, False, False, False, False)
    Magma = magma(860, 0, 0,
                  [pg.image.load("texture/magma/stolb_iz_magma_1.png"),
                   pg.image.load("texture/magma/stolb_iz_magma_2.png"),
                   pg.image.load("texture/magma/stolb_iz_magma_3.png"),
                   pg.image.load("texture/magma/stolb_iz_magma_4.png"),
                   pg.image.load("texture/magma/stolb_iz_magma_5.png"),
                   pg.image.load("texture/magma/stolb_iz_magma_6.png"),
                   pg.image.load("texture/magma/stolb_iz_magma_7.png"),
                   pg.image.load("texture/magma/stolb_iz_magma_8.png"),
                   pg.image.load("texture/magma/stolb_iz_magma_9.png"),
                   pg.image.load("texture/magma/stolb_iz_magma_10.png"),
                   pg.image.load("texture/magma/stolb_iz_magma_11.png")])
    Player1 = Player(0, 920, width / 1000, 10, 0, 0, 0, False, False, False, True, True, False, False, False,
                     [pg.image.load("texture/wallking1_right/0_Golem_Walking_000-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_001-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_002-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_003-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_004-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_005-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_006-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_007-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_008-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_009-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_010-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_011-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_012-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_013-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_014-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_015-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_016-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_017-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_018-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_019-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_020-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_021-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_022-removebg-preview.png"),
                      pg.image.load("texture/wallking1_right/0_Golem_Walking_023-removebg-preview.png")],
                     # wallkint_left
                     [pg.image.load("texture/wallking1_left/0_Golem_Walking_000-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_001-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_002-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_003-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_004-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_005-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_006-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_007-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_008-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_009-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_010-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_011-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_012-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_013-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_014-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_015-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_016-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_017-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_018-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_019-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_020-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_021-removebg-preview-removebg-preview.png"),
                      pg.image.load("texture/wallking1_left/0_Golem_Walking_022-removebg-preview-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking1_left/0_Golem_Walking_023-removebg-preview-removebg-preview.png")],
                     # looop_right
                     [pg.image.load("texture/JumpLoop/0_Golem_Jump_Loop_000.png"),
                      pg.image.load("texture/JumpLoop/0_Golem_Jump_Loop_001.png"),
                      pg.image.load("texture/JumpLoop/0_Golem_Jump_Loop_002.png"),
                      pg.image.load("texture/JumpLoop/0_Golem_Jump_Loop_003.png"),
                      pg.image.load("texture/JumpLoop/0_Golem_Jump_Loop_004.png"),
                      pg.image.load("texture/JumpLoop/0_Golem_Jump_Loop_005.png")],
                     # loop_left
                     [pg.image.load("texture/JumpLoopLeft/0_Golem_Jump_Loop_000-removebg-preview (1).png"),
                      pg.image.load("texture/JumpLoopLeft/0_Golem_Jump_Loop_001-removebg-preview (1).png"),
                      pg.image.load("texture/JumpLoopLeft/0_Golem_Jump_Loop_002-removebg-preview (1).png"),
                      pg.image.load("texture/JumpLoopLeft/0_Golem_Jump_Loop_003-removebg-preview (1).png"),
                      pg.image.load("texture/JumpLoopLeft/0_Golem_Jump_Loop_004-removebg-preview (1).png"),
                      pg.image.load("texture/JumpLoopLeft/0_Golem_Jump_Loop_005-removebg-preview (1).png")],
                     # idle
                     pg.image.load("texture/0_Golem_Idle_000-removebg-preview.png"),
                     pg.image.load("texture/0_Golem_Idle_000-removebg-preview___копия-removebg-preview.png"))
    Player2 = Player(width - width / 8, 920, width / 1000, 10, 0, 0, 0, False, False, True, False, False, True, False,
                     False,
                     [pg.image.load("texture/wallking2_right/0_Golem_Walking_000-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_001-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_002-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_003-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_004-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_005-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_006-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_007-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_008-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_009-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_010-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_011-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_012-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_013-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_014-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_015-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_016-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_017-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_018-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_019-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_020-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_021-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_022-removebg-preview (1).png"),
                      pg.image.load("texture/wallking2_right/0_Golem_Walking_023-removebg-preview (1).png")],
                     # wallking_left
                     [pg.image.load(
                         "texture/wallking2_left/0_Golem_Walking_000-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_001-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_002-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_003-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_004-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_005-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_006-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_007-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_008-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_009-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_010-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_011-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_012-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_013-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load("texture/wallking2_left/0_Golem_Walking_014-removebg-preview (2).png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_015-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_016-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_017-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_018-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_019-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_020-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_021-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_022-removebg-preview__1_-removebg-preview.png"),
                      pg.image.load(
                          "texture/wallking2_left/0_Golem_Walking_023-removebg-preview__1_-removebg-preview.png")],
                     # looping_right
                     [pg.image.load("texture/JumpLoop2/0_Golem_Jump_Loop_000-removebg-preview (2).png"),
                      pg.image.load("texture/JumpLoop2/0_Golem_Jump_Loop_001-removebg-preview (2).png"),
                      pg.image.load("texture/JumpLoop2/0_Golem_Jump_Loop_002-removebg-preview (2).png"),
                      pg.image.load("texture/JumpLoop2/0_Golem_Jump_Loop_003-removebg-preview (2).png"),
                      pg.image.load("texture/JumpLoop2/0_Golem_Jump_Loop_004-removebg-preview (2).png"),
                      pg.image.load("texture/JumpLoop2/0_Golem_Jump_Loop_005-removebg-preview (2).png")],
                     # looping_left
                     [pg.image.load(
                         "texture/JumoLoop2Left/0_Golem_Jump_Loop_000-removebg-preview__2_-removebg-preview.png"),
                         pg.image.load(
                             "texture/JumoLoop2Left/0_Golem_Jump_Loop_001-removebg-preview__2_-removebg-preview.png"),
                         pg.image.load(
                             "texture/JumoLoop2Left/0_Golem_Jump_Loop_002-removebg-preview__2_-removebg-preview.png"),
                         pg.image.load(
                             "texture/JumoLoop2Left/0_Golem_Jump_Loop_003-removebg-preview__2_-removebg-preview.png"),
                         pg.image.load(
                             "texture/JumoLoop2Left/0_Golem_Jump_Loop_004-removebg-preview__2_-removebg-preview.png"),
                         pg.image.load(
                             "texture/JumoLoop2Left/0_Golem_Jump_Loop_005-removebg-preview__2_-removebg-preview.png")],
                     # idle
                     pg.image.load("texture/3_Golem_Idle_000-removebg-preview.png"),
                     pg.image.load("texture/3_Golem_Idle_000-removebg-preview (1).png"))

    scr = pg.display.set_mode([width, hight])
    bg = pg.image.load("texture/bg_lvl3.png")
    magma = pg.image.load("texture/stolb_iz_magma.png")
    totem = pg.image.load("texture/totems_red.png")
    lever = pg.image.load("texture/lever.png")
    lever_red = pg.image.load("texture/lever_red.png")
    block = pg.image.load("texture/block_lava.png")
    platforms = pg.image.load("texture/lift_lvl3.png")
    game_end = pg.image.load("texture/portal_in_new_lvl__activation.png")
    kap_kap = pg.image.load(kapli1.texture)

    def draw():
        scr.blit(bg, [0, 0])
        scr.blit(elevator.texture, [elevator.x, elevator.y])
        # блок 2 половины
        scr.blit(totem, [-5, 670])
        scr.blit(block, [1500, 500])
        scr.blit(block, [1700, 350])
        #  блок 1 половины
        scr.blit(block, [500, 300])
        scr.blit(platforms, [600, 150])
        # блок 2 половины
        scr.blit(platforms, [1400, 150])
        scr.blit(platforms, [1000, 150])
        scr.blit(lava_down.texture, [lava_down.x, lava_down.y])
        scr.blit(kap_kap, [kapli1.x, kapli1.y])
        scr.blit(kap_kap, [kapli2.x, kapli2.y])
        scr.blit(kap_kap, [kapli3.x, kapli3.y])
        scr.blit(kap_kap, [kapli4.x, kapli4.y])
        scr.blit(kap_kap, [kapli5.x, kapli5.y])
        scr.blit(kap_kap, [kapli6.x, kapli6.y])
        if not flagarg.lever1:
            scr.blit(lever, [10, 580])
        else:
            scr.blit(lever_red, [10, 580])

        if not flagarg.lever2:
            scr.blit(lever, [1050, 50])
        else:
            scr.blit(lever_red, [1050, 50])

        if not flagarg.lever3:
            scr.blit(lever, [650, 50])
        else:
            scr.blit(lever_red, [650, 50])
            scr.blit(game_end, [840, 0])

    def move_kapli(kapli):
        if kapli.y <= 1200:
            kapli.y += random.randint(1, 3)
        else:
            kapli.y = random.randint(-20, 0)
            kapli.x = random.randint(50, 1800)

    def kapli_death(kapli, Player, removing):
        if Player.x + 28 <= kapli.x <= Player.x + 120 and Player.y + 30 <= kapli.y <= Player.y + 150:
            Player.x = removing
            Player.y = 920

    def lever1_actiiavtion():
        if Player1.y == 550 and 0 <= Player1.x <= 15:
            flagarg.lever1 = True
            elevator.right = False
            elevator.left = False
            elevator.left_player = True

    def lever2_activation():
        if Player2.y == 0 and 1000 <= Player2.x <= 1075:
            flagarg.lever2 = True
            elevator.left_player = False
            elevator.left_end = True

    def lever3_activation():
        if Player1.y == 0 and 575 <= Player1.x <= 700:
            flagarg.lever3 = True

    def lava():
        if Magma.anim_point + 1 >= 275:
            Magma.anim_point = 0

    def lift_up_player(Player):
        if elevator.x - 80 <= Player.x <= elevator.x + 193:
            # сверху
            if Player.y + 120 <= elevator.y <= Player.y + 148:
                Player.y = elevator.y - 148
                if elevator.right:
                    Player.x += 1
                elif elevator.left:
                    Player.x -= 1
            # снизу
            if Player.y + 47 <= elevator.y + 95 <= Player.y + 100:
                Player.y = elevator.y + 48

    def stop_block(Player):
        # 1
        if -100 <= Player.x <= 132:
            # сверху
            if Player.y + 120 <= 700 <= Player.y + 148:
                Player.y = 550
            # снизу
            if Player.y + 47 <= 789 <= Player.y + 100:
                Player.y = 741
        # 2
        if 1400 <= Player.x <= 1482:
            # сверху
            if Player.y + 120 <= 500 <= Player.y + 148:
                Player.y = 350
        # 3
        if 1600 <= Player.x <= 1682:
            # сверху
            if Player.y + 120 <= 350 <= Player.y + 148:
                Player.y = 200
        # 4
        if 1300 <= Player.x <= 1632:
            # сверху
            if Player.y + 120 <= 150 <= Player.y + 148:
                Player.y = 0
            # снизу
            if Player.y + 47 <= 139 <= Player.y + 100:
                Player.y = 91
        # 5
        if 900 <= Player.x <= 1220:
            # сверху
            if Player.y + 120 <= 150 <= Player.y + 148:
                Player.y = 0
        # 6
        if 400 <= Player.x <= 482:
            # сверху
            if Player.y + 120 <= 300 <= Player.y + 148:
                Player.y = 150
            # снизу
            if Player.y + 47 <= 363 <= Player.y + 100:
                Player.y = 315
        # 7
        if 500 <= Player.x <= 932:
            # сверху
            if Player.y + 120 <= 150 <= Player.y + 148:
                Player.y = 0
            # снизу
            if Player.y + 47 <= 139 <= Player.y + 100:
                Player.y = 91

    def vektor_liff():
        if elevator.x <= 200:
            elevator.right = True
            elevator.left = False
        elif elevator.x >= 1200:
            elevator.right = False
            elevator.left = True
            elevator.up = True

    def elevator_move():
        if elevator.right:
            elevator.x += 1
        elif elevator.left:
            elevator.x -= 1
        elif elevator.left_player:
            if elevator.x <= 1000:
                elevator.x += 1
            elif elevator.up:
                elevator.y -= 1
            elif elevator.down:
                elevator.y += 1
        elif elevator.left_end:
            if elevator.x >= 300:
                elevator.x -= 1
            elif elevator.up:
                elevator.y -= 1
            elif elevator.down:
                elevator.y += 1

    def elevator_vektor():
        if elevator.y == 600:
            elevator.up = False
            elevator.down = True
        elif elevator.y == hight - 50:
            elevator.up = True
            elevator.down = False

    def magma_move():
        if not flagarg.lever3:
            scr.blit(Magma.potok[Magma.anim_point // 25], [Magma.x, Magma.y])
            scr.blit(Magma.potok[Magma.anim_point // 25], [Magma.x, Magma.y + 126])
            scr.blit(Magma.potok[Magma.anim_point // 25], [Magma.x, Magma.y + 126 * 2])
            scr.blit(Magma.potok[Magma.anim_point // 25], [Magma.x, Magma.y + 126 * 3])
            scr.blit(Magma.potok[Magma.anim_point // 25], [Magma.x, Magma.y + 126 * 4])
            scr.blit(Magma.potok[Magma.anim_point // 25], [Magma.x, Magma.y + 126 * 5])
            scr.blit(Magma.potok[Magma.anim_point // 25], [Magma.x, Magma.y + 126 * 6])
            scr.blit(Magma.potok[Magma.anim_point // 25], [Magma.x, Magma.y + 126 * 7])
            scr.blit(Magma.potok[Magma.anim_point // 25], [Magma.x, Magma.y + 126 * 8])
            scr.blit(Magma.potok[Magma.anim_point // 25], [Magma.x, Magma.y + 126 * 9])
            Magma.anim_point += 1

    def magma_death(player, removing):
        if not flagarg.lever3:
            if 725 <= player.x <= 927:
                player.x = removing
                player.y = 920

    def all_kapli():
        move_kapli(kapli1)
        kapli_death(kapli1, Player1, 50)
        kapli_death(kapli1, Player2, 1860)
        # 2
        move_kapli(kapli2)
        kapli_death(kapli2, Player1, 50)
        kapli_death(kapli2, Player2, 1860)
        # 3
        move_kapli(kapli3)
        kapli_death(kapli3, Player1, 50)
        kapli_death(kapli3, Player2, 1860)
        # 4
        move_kapli(kapli4)
        kapli_death(kapli4, Player1, 50)
        kapli_death(kapli4, Player2, 1860)
        # 5
        move_kapli(kapli5)
        kapli_death(kapli5, Player1, 50)
        kapli_death(kapli5, Player2, 1860)
        # 6
        move_kapli(kapli6)
        kapli_death(kapli6, Player1, 50)
        kapli_death(kapli6, Player2, 1860)

    def lvl_3end(player):
        if player.y == 0 and 769 <= player.x <= 983:
            flagarg.end = True

    while flagarg.running3:
        player_time = int(time.process_time())
        print(player_time)
        draw()
        lava()
        magma_move()
        vektor_liff()
        elevator_move()
        stop_block(Player1)
        stop_block(Player2)
        lever1_actiiavtion()
        lever2_activation()
        elevator_vektor()
        function_player.animation(Player1)
        function_player.animation(Player2)
        magma_death(Player1, 0)
        magma_death(Player2, width - width/8)
        lever3_activation()
        all_kapli()
        lvl_3end(Player1)
        lvl_3end(Player2)
        Player1.y = function_player.grav2(Player1.y)
        Player2.y = function_player.grav2(Player2.y)
        Player1.x = function_player.player_stop_x(Player1.x)
        Player2.x = function_player.player_stop_x(Player2.x)
        Player1.y = function_player.player_stop_y(Player1.y)
        Player2.y = function_player.player_stop_y(Player2.y)
        Player1.x = function_player.wallk1(Player1.x, Player1, pg.K_d, pg.K_a)
        Player2.x = function_player.wallk1(Player2.x, Player2, pg.K_RIGHT, pg.K_LEFT)
        function_player.position_draw(Player1)
        function_player.position_draw(Player2)
        lift_up_player(Player1)
        lift_up_player(Player2)
        function_player.looping3(Player1, elevator)
        function_player.looping3(Player2, elevator)
        function_player.jump3(Player1, pg.K_SPACE, elevator)
        function_player.jump3(Player2, pg.K_RSHIFT, elevator)
        if flagarg.end:
            break
        for event in pg.event.get():
            if event.type == pg.QUIT:
                flagarg.running3 = False
        pg.display.flip()
