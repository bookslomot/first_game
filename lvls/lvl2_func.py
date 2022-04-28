import function_player
import pygame as pg
from lvls import lvl3_func
from function_player import Player
import time

width = 1920
hight = 1150


class FlagArg:
    def __init__(self, ice_r, ice_l, door1, door2, door3, door4, door5, door6, ice_stop, bot_move_r, bot_move_l, dragon_r, dragon_l, dragon_stop, lever1, lvl3):
        self.ice_r = ice_r
        self.ice_l = ice_l
        self.door1 = door1
        self.door2 = door2
        self.door3 = door3
        self.door4 = door4
        self.door5 = door5
        self.door6 = door6
        self.ice_stop = ice_stop
        self.bot_move_r = bot_move_r
        self.bot_move_l = bot_move_l
        self.dragon_r = dragon_r
        self.dragon_l = dragon_l
        self.dragon_stop = dragon_stop
        self.lever1 = lever1
        self.lvl3 = lvl3


class Bot:
    """Создание бота """

    def __init__(self, x, y, step_x, anim_point, wallking_right, wallking_left):
        self.x = x
        self.y = y
        self.step_x = step_x
        self.anim_point = anim_point
        self.wallking_right = wallking_right
        self.wallking_left = wallking_left


class Flag_blue:
    def __init__(self, x, y, position):
        self.x = x
        self.y = y
        self.position = position


class Dragon:
    def __init__(self, x, y, anim_point, wallking_right, wallking_left):
        self.x = x
        self.y = y
        self.anim_point = anim_point
        self.wallking_right = wallking_right
        self.wallking_left = wallking_left


class block:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def lets_go_2(running2):
    block1 = block(0, 600)
    block2 = block(1800, 600)
    dragon_ice = Dragon(0, 680, 0, [pg.image.load("texture/ice_dragon/Sprite_FX_Water_0000-removebg-preview.png"),
                                    pg.image.load("texture/ice_dragon/Sprite_FX_Water_0001-removebg-preview.png"),
                                    pg.image.load("texture/ice_dragon/Sprite_FX_Water_0002-removebg-preview.png"),
                                    pg.image.load("texture/ice_dragon/Sprite_FX_Water_0003-removebg-preview.png"),
                                    pg.image.load("texture/ice_dragon/Sprite_FX_Water_0004-removebg-preview.png"),
                                    pg.image.load("texture/ice_dragon/Sprite_FX_Water_0005-removebg-preview.png"),
                                    pg.image.load("texture/ice_dragon/Sprite_FX_Water_0006-removebg-preview.png"),
                                    pg.image.load("texture/ice_dragon/Sprite_FX_Water_0007-removebg-preview.png"),
                                    pg.image.load("texture/ice_dragon/Sprite_FX_Water_0008-removebg-preview.png"),
                                    pg.image.load("texture/ice_dragon/Sprite_FX_Water_0009-removebg-preview.png")],
                        # left
                        [pg.image.load("texture/ice_dragon_l/Sprite_FX_Water_0000-removebg-preview (1).png"),
                         pg.image.load("texture/ice_dragon_l/Sprite_FX_Water_0001-removebg-preview (1).png"),
                         pg.image.load("texture/ice_dragon_l/Sprite_FX_Water_0002-removebg-preview (1).png"),
                         pg.image.load("texture/ice_dragon_l/Sprite_FX_Water_0003-removebg-preview (1).png"),
                         pg.image.load("texture/ice_dragon_l/Sprite_FX_Water_0004-removebg-preview (1).png"),
                         pg.image.load("texture/ice_dragon_l/Sprite_FX_Water_0005-removebg-preview (1).png"),
                         pg.image.load("texture/ice_dragon_l/Sprite_FX_Water_0006-removebg-preview (1).png"),
                         pg.image.load("texture/ice_dragon_l/Sprite_FX_Water_0007-removebg-preview (1).png"),
                         pg.image.load("texture/ice_dragon_l/Sprite_FX_Water_0008-removebg-preview (1).png"),
                         pg.image.load("texture/ice_dragon_l/Sprite_FX_Water_0009-removebg-preview (1).png")])

    bot = Bot(1500, 370, width / 1000, 0,
              [pg.image.load("texture/Running_right/0_Golem_Running_000-removebg-preview (1).png"),
               pg.image.load("texture/Running_right/0_Golem_Running_001-removebg-preview (1).png"),
               pg.image.load("texture/Running_right/0_Golem_Running_002-removebg-preview (1).png"),
               pg.image.load("texture/Running_right/0_Golem_Running_003-removebg-preview (1).png"),
               pg.image.load("texture/Running_right/0_Golem_Running_004-removebg-preview (1).png"),
               pg.image.load("texture/Running_right/0_Golem_Running_005-removebg-preview (1).png"),
               pg.image.load("texture/Running_right/0_Golem_Running_006-removebg-preview (1).png"),
               pg.image.load("texture/Running_right/0_Golem_Running_007-removebg-preview (1).png"),
               pg.image.load("texture/Running_right/0_Golem_Running_008-removebg-preview (1).png"),
               pg.image.load("texture/Running_right/0_Golem_Running_009-removebg-preview (1).png"),
               pg.image.load("texture/Running_right/0_Golem_Running_010-removebg-preview (1).png"),
               pg.image.load("texture/Running_right/0_Golem_Running_011-removebg-preview (1).png")],
              # left
              [pg.image.load("texture/Running_left/0_Golem_Running_000-removebg-preview.png"),
               pg.image.load("texture/Running_left/0_Golem_Running_001-removebg-preview.png"),
               pg.image.load("texture/Running_left/0_Golem_Running_002-removebg-preview.png"),
               pg.image.load("texture/Running_left/0_Golem_Running_003-removebg-preview.png"),
               pg.image.load("texture/Running_left/0_Golem_Running_004-removebg-preview.png"),
               pg.image.load("texture/Running_left/0_Golem_Running_005-removebg-preview.png"),
               pg.image.load("texture/Running_left/0_Golem_Running_006-removebg-preview.png"),
               pg.image.load("texture/Running_left/0_Golem_Running_007-removebg-preview.png"),
               pg.image.load("texture/Running_left/0_Golem_Running_008-removebg-preview.png"),
               pg.image.load("texture/Running_left/0_Golem_Running_009-removebg-preview.png"),
               pg.image.load("texture/Running_left/0_Golem_Running_010-removebg-preview.png"),
               pg.image.load("texture/Running_left/0_Golem_Running_011-removebg-preview.png")])

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
    Player2 = Player(width - width / 8, 20, 3, 10, 0, 0, 0, False, False, True, False, False, True, False,
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
    flag_blue = Flag_blue(800, 50, False)
    flag_arg = FlagArg(False, False, False, False, False, False, False, False, True, True, False, True, False, True, False, False)
    scr = pg.display.set_mode([width, hight])
    bg = pg.image.load("texture/bg2_new.jpg")
    door_locket = pg.image.load("texture/door_locket.png")
    door_open = pg.image.load("texture/door_open.png")
    flag_ice = pg.image.load("texture/flag_ice.png")
    portal = pg.image.load("texture/portal_in_new_lvl.png")
    portal_open = pg.image.load("texture/portal_in_new_lvl__activation.png")
    stop_lvl = pg.image.load("texture/stop_lvl.png")
    lever_down = pg.image.load("texture/lever.png")
    lever_up = pg.image.load("texture/lever_red.png")

    def animation_bot():
        if bot.anim_point + 1 >= 77:
            bot.anim_point = 0

    def animation_dragon():
        if dragon_ice.anim_point + 1 >= 100:
            dragon_ice.anim_point = 0

    def ice_stop_player():
        if flag_arg.ice_stop:
            if Player2.y == 370 and Player2.x + 58 <= 723:
                Player2.x = 665
        else:
            if Player2.y == 370 and Player2.x + 100 >= 560:
                Player2.x = 460
        if flag_arg.dragon_stop:
            if Player2.x <= 65 and Player2.y == 700:
                Player2.x = 65
            if Player2.x >= width - 240 and Player2.y == 700:
                Player2.x = width - 240

    def door_tp():
        # 1
        # door
        if 257 <= Player1.x <= 454:
            flag_arg.door1 = True
            flag_arg.door2 = True
            # tp
            if 1200 <= Player2.x <= 1220 and Player2.y == 35:
                Player2.x = 100
        # 2
        elif 507 <= Player1.x <= 703:
            flag_arg.door2 = True
            flag_arg.door3 = True
            if flag_blue.position:
                if 0 <= Player2.x <= 162 and Player2.y == 35:
                    Player2.y = 370
                    Player2.x = 1100
        # 3
        elif 7 <= Player1.x <= 231:
            flag_arg.door3 = True
            flag_arg.door4 = True
            if 1050 <= Player2.x <= 1114 and Player2.y == 370:
                Player2.y = 700
                Player2.x = 600
        # 5
        elif 1502 <= Player1.x <= 1727:
            flag_arg.door5 = True
            flag_arg.door6 = True
            if 1250 <= Player2.x <= 1314 and Player2.y == 700:
                Player2.y = 370
                Player2.x = 300
                flag_arg.ice_stop = False

        else:
            flag_arg.door1 = False
            flag_arg.door2 = False
            flag_arg.door3 = False
            flag_arg.door4 = False
            flag_arg.door5 = False
            flag_arg.door6 = False

    def flag_up():
        if 680 <= Player2.x <= 792 and Player2.y == 35:
            flag_blue.position = True

    def flag_move():
        if flag_blue.position:
            flag_blue.x = Player2.x + 75
            flag_blue.y = Player2.y - 40

    def draw():
        scr.blit(bg, [0, 0])
        if not flag_blue.position:
            scr.blit(portal, [0, 330])
        else:
            scr.blit(portal_open, [0, 330])
        if not flag_arg.door2:
            scr.blit(door_locket, [100, 30])
        else:
            scr.blit(door_open, [100, 30])
        if not flag_arg.door1:
            scr.blit(door_locket, [1200, 30])
        else:
            scr.blit(door_open, [1200, 30])
        if not flag_arg.door3:
            scr.blit(door_locket, [1100, 365])
        else:
            scr.blit(door_open, [1100, 365])
        if not flag_arg.door4:
            scr.blit(door_locket, [600, 680])
        else:
            scr.blit(door_open, [600, 680])
        if not flag_arg.door5:
            scr.blit(door_locket, [1300, 680])
        else:
            scr.blit(door_open, [1300, 680])
        if not flag_arg.door6:
            scr.blit(door_locket, [350, 365])
        else:
            scr.blit(door_open, [350, 365])
        scr.blit(flag_ice, [flag_blue.x, flag_blue.y])
        scr.blit(stop_lvl, [600, 280])
        if not flag_arg.lever1:
            scr.blit(lever_down, [1500, 400])
        else:
            scr.blit(lever_up, [1500, 400])

        if flag_arg.dragon_stop:
            scr.blit(stop_lvl, [block1.x, block1.y])
            scr.blit(stop_lvl, [block2.x, block2.y])
        else:
            if block1.y <= 2000:
                block1.y += 5
                block2.y += 5
                scr.blit(stop_lvl, [block1.x, block1.y])
                scr.blit(stop_lvl, [block2.x, block2.y])

    def stop_kol():
        if Player2.y == 35 and 938 <= Player2.x <= 1060:
            Player2.x = width - width / 8

    def stop_floor(player):
        # 1
        if 10 <= player.y - 22 <= 180:
            player.y = 35
        # 2
        if 46 <= player.y - 32 <= 530:
            player.y = 370
        # 3
        if 406 <= player.y - 32 <= 800:
            player.y = 700
        elif 850 <= player.y + 47 <= 933:
            player.y = 886

    def wallk2(player, keyesr, keyesl):
        keys = pg.key.get_pressed()
        if keys[keyesr]:
            player.right = True
            player.left = False
            player.idle_right = True
            player.idle_left = False
            player.right_loop = True
            player.left_loop = False
            flag_arg.ice_l = False
            flag_arg.ice_r = True
        elif keys[keyesl]:
            player.left = True
            player.right = False
            player.idle_right = False
            player.idle_left = True
            player.left_loop = True
            player.right_loop = False
            flag_arg.ice_r = False
            flag_arg.ice_l = True

    def ice_go(player):
        if flag_arg.ice_r:
            player.x += player.step_x
        if flag_arg.ice_l:
            player.x -= player.step_x

    def vektor_bot():
        if bot.x >= 1700:
            flag_arg.bot_move_r = False
            flag_arg.bot_move_l = True
        elif bot.x <= 1200:
            flag_arg.bot_move_r = True
            flag_arg.bot_move_l = False

    def vektor_dragon():
        if flag_arg.dragon_stop:
            if dragon_ice.x >= 1550:
                flag_arg.dragon_r = False
                flag_arg.dragon_l = True
            elif dragon_ice.x <= 100:
                flag_arg.dragon_r = True
                flag_arg.dragon_l = False
        else:
            if dragon_ice.x >= 2300:
                flag_arg.dragon_r = False
                flag_arg.dragon_l = False
            elif dragon_ice.x <= -300:
                flag_arg.dragon_r = False
                flag_arg.dragon_l = False

    def bot_move():
        if  flag_arg.bot_move_r:
            bot.x += bot.step_x
            scr.blit(bot.wallking_right[bot.anim_point // 7], [bot.x, bot.y])
            bot.anim_point += 1
        elif flag_arg.bot_move_l:
            bot.x -= bot.step_x
            scr.blit(bot.wallking_left[bot.anim_point // 7], [bot.x, bot.y])
            bot.anim_point += 1

    def dragon_move():
        if flag_arg.dragon_r:
            dragon_ice.x += 2
            scr.blit(dragon_ice.wallking_right[dragon_ice.anim_point // 10], [dragon_ice.x, dragon_ice.y])
            dragon_ice.anim_point += 1
        if flag_arg.dragon_l:
            dragon_ice.x -= 2
            scr.blit(dragon_ice.wallking_left[dragon_ice.anim_point // 10], [dragon_ice.x, dragon_ice.y])
            dragon_ice.anim_point += 1

    def bot_kill():
        if Player2.y == 370:
            if Player2.x + 136 >= bot.x + 62 and Player2.x <= bot.x:
                Player2.x = width - width / 8
                Player2.y = 35

    def dragon_kill():
        if Player2.y == 700:
            if Player2.x + 132 >= dragon_ice.x >= Player2.x - 100:
                Player2.x = width - width / 8
                Player2.y = 35

    def lever_upper():
        if Player2.x >= 1400 and Player2.y == 370:
            flag_arg.lever1 = True
            flag_arg.dragon_stop = False

    def lvl2_end():
        global running2
        if Player2.y == 370 and Player2.x <= 50:
            flag_arg.lvl3 = True
            return True
    while running2:
        player_time = int(time.process_time())
        print(player_time)
        draw()
        stop_kol()
        door_tp()
        flag_up()
        flag_move()
        ice_stop_player()
        animation_bot()
        bot_move()
        vektor_bot()
        bot_kill()
        animation_dragon()
        dragon_move()
        vektor_dragon()
        lever_upper()
        dragon_kill()
        lvl2_end()
        function_player.animation(Player1)
        function_player.animation(Player2)
        function_player.looping2(Player1)
        function_player.looping2(Player2)
        Player1.y = function_player.grav2(Player1.y)
        Player2.y = function_player.grav2(Player2.y)
        Player1.x = function_player.player_stop_x(Player1.x)
        Player2.x = function_player.player_stop_x(Player2.x)
        Player1.y = function_player.player_stop_y(Player1.y)
        Player2.y = function_player.player_stop_y(Player2.y)
        Player1.x = function_player.wallk1(Player1.x, Player1, pg.K_d, pg.K_a)
        wallk2(Player2, pg.K_RIGHT, pg.K_LEFT)
        ice_go(Player2)
        stop_floor(Player2)
        stop_floor(Player1)
        function_player.jump2(Player1, pg.K_SPACE)
        function_player.jump2(Player2, pg.K_RSHIFT)
        function_player.position_draw(Player1)
        function_player.position_draw(Player2)
        if flag_arg.lvl3:
            lvl3_func.lets_go3()
            break
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running2 = False
        pg.display.flip()


