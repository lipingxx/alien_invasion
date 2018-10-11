#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Sprite

# 通过使用精灵，可将游戏中相关的元素编组，进而同时操作编组中的所有元素
class Bullet(Sprite):
    '''一个对飞船发射的子弹进行管理的类'''
    def __init__(self, ai_setting, screen, ship):
        '''在飞船所处的位置发射一个子弹'''
        super(Bullet,self).__init__()
        self.screen = screen

        # 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        # 子弹不是基于图像的，因此必须使用pygame.Rect()类从空白开始创建一个矩形
        # 提供矩形左上角的xy坐标、矩形的宽度、矩形的高度
        self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)

        # 创建完子弹矩形之后，子弹的初始位置取决于飞船的位置
        # 子弹从飞船顶部发射出
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        '''绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)
