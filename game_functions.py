#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys

import pygame
from alien_invasion.bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        # ship.rect.centerx += 1
        # 将向右移动标志设为True
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 如果为空格，则创建一个子弹，并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullets_allowed :
           new_bullet = Bullet(ai_settings,screen,ship)
           bullets.add(new_bullet)

def check_keyup_events(event,ship):
    '''响应松开'''
    #if event.type == pygame.KEYUP:  # 键盘松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False  # 向右移动的键盘松开后，将标志位设为False
    if event.key == pygame.K_LEFT:
            ship.moving_left = False


# 游戏编程基础：鼠标键盘控制物品移动、物体的碰撞
def check_events(ai_settings,screen,ship,bullets):
    '''响应按键和鼠标事件'''
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        # 点击“关闭”按钮
        if event.type == pygame.QUIT:
            # 退出游戏
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 键盘按下
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:  # 键盘松开
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitem()  # 将飞机绘制到屏幕上

    # 让最近绘制的屏幕可见，则将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，营造平滑移动的效果
    pygame.display.flip()
