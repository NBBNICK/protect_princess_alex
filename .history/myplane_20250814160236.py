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

class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        # --- 应用 resource_path 函数 ---
        self.image1 = pygame.image.load(resource_path("images/me1.png")).convert_alpha()
        self.image2 = pygame.image.load(resource_path("images/me2.png")).convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load(resource_path("images/me_destroy_1.png")).convert_alpha(), \
            pygame.image.load(resource_path("images/me_destroy_2.png")).convert_alpha(), \
            pygame.image.load(resource_path("images/me_destroy_3.png")).convert_alpha(), \
            pygame.image.load(resource_path("images/me_destroy_4.png")).convert_alpha() \
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.speed = 10
        self.active = True
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.active = True
        self.invincible = True