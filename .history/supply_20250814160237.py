import pygame
from random import *
import os
import sys

# ==================== 为打包添加的关键函数 ====================
def resource_path(relative_path):
    """ 获取资源的绝对路径，无论是作为脚本运行还是打包后 """
    try:
        # PyInstaller/py2app 创建一个临时文件夹并将路径存储在 _MEIPASS 中
        base_path = sys._MEIPASS
    except Exception:
        # 如果不是通过打包程序运行，则使用常规路径
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# =============================================================

class Bullet_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        # --- 应用 resource_path 函数 ---
        self.image = pygame.image.load(resource_path("images/bullet_supply.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = \
                        randint(0, self.width - self.rect.width), \
                        -100
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = \
                        randint(0, self.width - self.rect.width), \
                        -100


class Bomb_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        # --- 应用 resource_path 函数 ---
        self.image = pygame.image.load(resource_path("images/bomb_supply.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = \
                        randint(0, self.width - self.rect.width), \
                        -100
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = \
                        randint(0, self.width - self.rect.width), \
                        -100