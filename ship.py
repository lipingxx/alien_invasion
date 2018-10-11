#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pygame

class Ship():

    # def __int__(self,screen):  报错：object() takes no parameters
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像 并 获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        # 获取相应surface的属性:image\screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # 移动标志：增加一个Ship的属性，来判断向右移的开关
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志来调整飞船的位置 x轴y轴'''
        # self.rect.right 返回飞船外接矩形的右边缘位置的x坐标
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left  and self.rect.left > 0:
            #self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center 更新rect对象
        self.rect.centerx = self.center

    def blitem(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)