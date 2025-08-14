import pygame
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

class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        # --- 应用 resource_path 函数 ---
        self.image = pygame.image.load(resource_path("images/bullet1.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 12  # 稍微提高了普通子弹的速度，使其更有用
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        # --- 应用 resource_path 函数 ---
        self.image = pygame.image.load(resource_path("images/bullet2.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 14  # 稍微提高了超级子弹的速度
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True