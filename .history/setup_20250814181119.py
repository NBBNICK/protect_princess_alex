# setup.py (最终决战版)
from setuptools import setup
import glob

APP_NAME = "Protect Princess Alex"
APP_SCRIPT = 'main.py'

# --- 明确指定数据文件 ---
# 这是最关键的部分。我们告诉 py2app:
# 1. 创建一个名为 'images' 的目标文件夹
# 2. 把本地 'images' 文件夹下的所有文件都复制进去
# 以此类推...
DATA_FILES = [
    ('images', glob.glob('images/*')),
    ('sound', glob.glob('sound/*')),
    ('font', glob.glob('font/*')),
    # 将 record.txt 放在顶层的 Resources 目录
    ('', ['record.txt'])
]

# 确保 record.txt 存在，防止打包时因文件不存在而失败
if not glob.glob('record.txt'):
    with open('record.txt', 'w') as f:
        f.write('0')

# --- py2app 选项 ---
OPTIONS = {
    # 如果没有 .icns 图标文件，请务必用 '#' 注释掉下面这行
    # 'iconfile': 'icon.icns',
    
    # 明确包含所有需要的包
    'packages': ['pygame', 'tkinter'],
    
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0",
        'CFBundleIdentifier': "com.nbbnick.protectprincessalex",
        'NSHumanReadableCopyright': 'Copyright © 2024 NBB Nick. All rights reserved.'
    }
}

# --- 设置 ---
setup(
    app=[APP_SCRIPT],
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)