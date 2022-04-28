import function_player
from lvls import lvl2_func
import pygame as pg
from function_player import Player
import time
width = 1920
hight = 1150



class FlagArgAll:
    def __init__(self, running, knopka_down, portal_active, lever_up, lift, mini1, mini2, level_tp, lvl2):
        self.running = running
        self.knopka_down = knopka_down
        self.portal_active = portal_active
        self.portal_active = portal_active
        self.lever_up = lever_up
        self.lift = lift
        self.mini1 = mini1
        self.mini2 = mini2
        self.level_tp = level_tp
        self.lvl2 = lvl2


class Barel():
    """create barel"""

    def __init__(self, x, y) -> object:
        self.x = x
        self.y = y


class Lift_upper():
    """create width and hight lift"""

    def __init__(self, x, y, down, up):
        self.x = x
        self.y = y
        self.down = down
        self.up = up


class Flag_red():
    def __init__(self, x, y, position):
        self.x = x
        self.y = y
        self.position = position


def lets_go():
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
    barel_f = Barel(1300, 1030)
    lift_upper = Lift_upper(1300, hight - 15, False, True)
    flag_red = Flag_red(810, 170, False)
    FlagArg = FlagArgAll(True, True, False, True, False, False, False, False, False)

    block1 = pg.image.load("texture/block3.png")
    block2 = pg.image.load("texture/block2.png")
    block3 = pg.image.load("texture/73f603489f951ab582cbdee4dc8d83d7___копия.png")
    block_up = pg.image.load("texture/kisspng-leaf-flowerpot-2d-grass-5b40c3fa420da2.7916902515309711302706.png")
    lever = pg.image.load("texture/lever.png")
    lever2 = pg.image.load("texture/lever.png")
    back_round = pg.image.load("texture/BG_01.png")
    barel = pg.image.load("texture/бочка.png")
    knopka = pg.image.load("texture/knopka.png")
    knopka_red = pg.image.load("texture/knopka_red.png")
    totems = pg.image.load("texture/totems_green.png")
    green_tp = pg.image.load("texture/портал.png")
    red_tp = pg.image.load("texture/портал1.png")
    lever_red = pg.image.load("texture/lever_red.png")
    lever_red2 = pg.image.load("texture/lever_red.png")
    mini_block1 = pg.image.load("texture/mini_block1.png")
    level_tp_lvl2 = pg.image.load("texture/level_1.png")
    flag = pg.image.load("texture/flag1.png")

    scr = pg.display.set_mode([width, hight])

    def stop_barel(Player):
        if barel_f.x - 30 <= Player.x + 64 <= barel_f.x + 80 and Player.y + 150 >= barel_f.y and not Player.isJump:
            Player.y = barel_f.y - 150

        # движение бочки

    def bocka(Player):
        if barel_f.x <= Player.x and Player.y == hight - 200:
            if barel_f.x >= Player.x - 40:
                barel_f.x = Player.x - 40
        elif Player.y == hight - 200:
            if barel_f.x <= Player.x + 100:
                barel_f.x = Player.x + 100

    def totem_power(Player):
        if FlagArg.knopka_down:
            scr.blit(totems, [300, 870])
            if -100 <= Player.x <= 300 and Player.y >= 900:
                if Player.x + 134 >= 300:
                    Player.x = 166
            elif Player.y >= 300 and Player.y >= 800:
                if Player.x <= 319 and Player.x >= 300:
                    Player.x = 319
            if Player.y >= 715 and 240 <= Player.x <= 300:
                Player.y = 715

    def knopkaDown():
        if 960 >= barel_f.x >= 840:
            FlagArg.knopka_down = False
        else:
            FlagArg.knopka_down = True

    def lever_activation(player):
        if player.x >= 1760 and player.y == 705:
            FlagArg.lever_up = False

    def lift_activation(player):
        if 350 <= player.x <= 370 and player.y == 168:
            FlagArg.lift = True

    def portal_activation(player):
        if not FlagArg.lever_up:
            FlagArg.portal_active = True
            if 130 <= player.x <= 200 and player.y == 662:
                player.y = 100
                player.x = 450

    def draw():
        scr.blit(back_round, [0, 0])
        scr.blit(block1, [-30, 780])
        scr.blit(block2, [1700, 850])
        scr.blit(block3, [300, 300])
        scr.blit(barel, [barel_f.x, barel_f.y])
        if FlagArg.mini1:
            scr.blit(mini_block1, [1100, 320])
        if FlagArg.mini2:
            scr.blit(mini_block1, [800, 320])
            scr.blit(flag, [flag_red.x, flag_red.y])
        # portal_not
        if not FlagArg.portal_active:
            scr.blit(green_tp, [170, 580])
        else:
            scr.blit(red_tp, [170, 580])
            scr.blit(red_tp, [450, 90])
        # knopka_red
        if 960 >= barel_f.x >= 840:
            scr.blit(knopka_red, [900, 1080])
        else:
            scr.blit(knopka, [900, 1080])
        if FlagArg.lever_up:
            scr.blit(lever, [1820, 745])
        else:
            scr.blit(lever_red, [1820, 745])

        if not FlagArg.lift:
            scr.blit(block_up, [lift_upper.x, lift_upper.y])
            scr.blit(lever2, [350, 200])
        else:
            scr.blit(lever_red2, [350, 200])
            if lift_upper.y >= 300 and lift_upper.up:
                lift_upper.y -= 1
            elif lift_upper.y <= hight - 15 and lift_upper.down:
                lift_upper.y += 1
                FlagArg.mini1 = True
            scr.blit(block_up, [lift_upper.x, lift_upper.y])

    def draw_lvl2_tp():
        if FlagArg.level_tp:
            scr.blit(level_tp_lvl2, [850, hight - 300])

    def stop_block(player):
        # 1
        if -60 < player.x <= 240:
            if player.y + 47 <= 964 and player.y >= 850:
                player.y = 917
            elif player.y + 120 <= 800 and player.y >= 662:
                player.y = 662

        # 2
        if 1640 < player.x <= width - 85:
            if 890 <= player.y + 47 <= 948:
                player.y = 901
            elif player.y + 162 >= 850 and player.y <= 750:
                player.y = 705

        # 3
        if player.x + 47 >= 270 and player.x <= 590:
            if player.y <= 300 and player.y + 162 >= 300:
                player.y = 168
        # 4
        if 1050 <= player.x + 47 <= 1110:
            if player.y <= 220 and player.y + 162 >= 320:
                player.y = 168
                FlagArg.mini2 = True
        # 5
        if 750 <= player.x + 47 <= 810:
            if player.y <= 220 and player.y + 162 >= 320:
                player.y = 168

    def lift_up_player(Player):
        if lift_upper.x - 70 <= Player.x <= lift_upper.x + 143:
            if Player.y + 120 <= lift_upper.y <= Player.y + 148:
                Player.y = lift_upper.y - 148
            if Player.y + 47 <= lift_upper.y + 95 <= Player.y + 100:
                Player.y = lift_upper.y + 48

    def lif_vektor():
        if lift_upper.y == 300:
            lift_upper.up = False
            lift_upper.down = True
        elif lift_upper.y == hight - 15:
            lift_upper.up = True
            lift_upper.down = False

    def portal_in_lvl2(player):
        if 750 <= player.x + 47 <= 810:
            if player.y <= 350 and player.y + 162 >= 320:
                flag_red.position = True
                FlagArg.level_tp = True

    def flag_move():
        if flag_red.position:
            flag_red.x = Player2.x + 87
            flag_red.y = Player2.y - 40

    def lvl1_end(player):
        if 850 <= player.x <= 1100 and player.y >= hight - 300 and FlagArg.level_tp:
            FlagArg.lvl2 = True
            FlagArg.running = False
            return True

    # lvl1
    while FlagArg.running:
        player_time = int(time.process_time())
        print(player_time)
        draw()
        lif_vektor()
        function_player.animation(Player1)
        function_player.animation(Player2)
        function_player.looping(Player1, lift_upper, barel_f)
        function_player.looping(Player2, lift_upper, barel_f)
        Player1.y = function_player.grav(Player1.y)
        Player2.y = function_player.grav(Player2.y)
        Player1.x = function_player.player_stop_x(Player1.x)
        Player2.x = function_player.player_stop_x(Player2.x)
        Player1.y = function_player.player_stop_y(Player1.y)
        Player2.y = function_player.player_stop_y(Player2.y)
        Player1.x = function_player.wallk1(Player1.x, Player1, pg.K_d, pg.K_a)
        Player2.x = function_player.wallk1(Player2.x, Player2, pg.K_RIGHT, pg.K_LEFT)
        stop_barel(Player1)
        stop_barel(Player2)
        totem_power(Player1)
        totem_power(Player2)
        stop_block(Player1)
        stop_block(Player2)
        function_player.position_draw(Player1)
        function_player.position_draw(Player2)
        draw_lvl2_tp()
        bocka(Player1)
        bocka(Player2)
        knopkaDown()
        lever_activation(Player1)
        lever_activation(Player2)
        portal_activation(Player1)
        lift_activation(Player1)
        lift_activation(Player2)
        lift_up_player(Player1)
        lift_up_player(Player2)
        function_player.jump(Player1, pg.K_SPACE, lift_upper,barel_f)
        function_player.jump(Player2, pg.K_RSHIFT, lift_upper,barel_f)
        flag_move()
        portal_in_lvl2(Player2)
        lvl1_end(Player2)
        if FlagArg.lvl2:
            lvl2_func.lets_go_2(True)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                FlagArg.running = False
        pg.display.flip()

