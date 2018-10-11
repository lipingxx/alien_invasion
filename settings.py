#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Settings():
    '''存储外星人入侵的所有设置类'''

    def __init__(self):
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width  = 1200
        self.screen_height = 800
        self.bg_color      = (230,230,230)

        # 调整飞船移动速度，每次移动1.5个像素，但是centerx属性只能存储整数值
        self.ship_speed_factor = 1.5

        # 子弹设置，设置创建宽3像素、高15像素的深灰色子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = 60,60,60

        # 限制子弹的数量，则需要在keydown事件创建子弹前检查未消失的子弹数量
        self.bullets_allowed = 3


