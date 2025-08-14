# setup.py
from setuptools import setup
import os

# --- 应用程序基本信息 ---
APP_NAME = "Protect Princess Alex"
# 你的主程序脚本文件列表
APP = ['main.py']

# --- 包含的资源文件和文件夹 ---
# 这里列出所有需要被打包进应用程序的文件夹和独立文件。
# py2app 会将它们复制到 .app 包内的 "Resources" 文件夹中。
DATA_FILES = []
# 遍历 'images', 'sound', 'font' 文件夹，把里面的所有文件都找出来
for folder in ['images', 'sound', 'font']:
    for file in os.listdir(folder):
        f1 = os.path.join(folder, file)
        if os.path.isfile(f1): # 确保只添加文件
            DATA_FILES.append(f1)

# 不要忘记添加根目录下的记录文件
if os.path.exists('record.txt'):
    DATA_FILES.append('record.txt')
else:
    # 如果 record.txt 不存在，创建一个空的，防止打包时因找不到文件而报错
    with open('record.txt', 'w') as f:
        f.write('0')
    DATA_FILES.append('record.txt')

# --- py2app 的详细配置选项 ---
OPTIONS = {
    # 应用程序图标。你需要准备一个名为 'icon.icns' 的图标文件放在根目录。
    # 如果你没有图标，可以把下面这行代码用 '#' 注释掉。
    # 'iconfile': 'icon.icns', 
    
    # 明确告诉 py2app 需要包含这些包，防止打包时遗漏。
    'packages': ['pygame', 'tkinter'], 
    
    # 定义 App 的元数据，这些信息会显示在 "关于" 和 "简介" 窗口中。
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0",
        # 把 com.yourname.protectprincessalex 中的 'yourname' 换成你自己的名字或ID
        'CFBundleIdentifier': "com.nbbnick.protectprincessalex", 
        'NSHumanReadableCopyright': 'Copyright © 2024 NBB Nick. All rights reserved.'
    }
}

# --- 最终设置 ---
setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)