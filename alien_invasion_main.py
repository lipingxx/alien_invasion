#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys

import pygame
from alien_invasion.settings import Settings
from alien_invasion.ship import Ship
from alien_invasion import game_functions as gf
from pygame.sprite import Group

def run_game():
    '''初始化游戏，并创建一个屏幕对象'''
    # 初始化背景设置
    pygame.init()
    # 创建screen 窗口，并指定游戏窗口的尺寸
    # screen 是一个surface，在py中，surface是屏幕的一部分，用于显示游戏元素
    # 游戏中的每一个元素都是 surface
    #screen = pygame.display.set_mode((1200,800))

    # 法2：通过settings类实例进行屏幕的绘制
    #  设置项目归为一个类
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    # 设置框t体标题
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 设置背景色
    #bg_color = (230,230,230)

    # 开始游戏的主循环，没经过一次循环都将自动重绘这个surface
    while True:

        # 监视键盘和鼠标事件
        '''
        for event in pygame.event.get():
            # 点击“关闭”按钮
            if event.type == pygame.QUIT:
                sys.exit()  # 退出游戏
        '''
        # 取得标志位
        #gf.check_evects(ship)
        gf.check_events(ai_settings,screen,ship,bullets)

        # 根据标志位，调用update()方法，进行飞船的移动
        ship.update()
        bullets.update()

        # 循环 重绘屏幕,用背景色进行填充
        #screen.fill(bg_color)
        # 法2：
        '''
        screen.fill(ai_settings.bg_color)
        ship.blitem() # 将飞机绘制到屏幕上
        # 让最近绘制的屏幕可见，则将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，营造平滑移动的效果
        pygame.display.flip()
        '''
        # 删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(bullets )

        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()