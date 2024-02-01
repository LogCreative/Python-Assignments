# 快速移动一个图形形成动画。
# 皮球从高处落地弹起.
# 提示:假设速度矢量向下为正,向上为负(注意坐标系方向),
# 且以皮球距地面高度(而非纵坐标)为位置变量,
# 则主要计算公式为
#   球的新高度 = 球的旧高度 - 球速 * 时间间隔
#   球的新速度 = 球的旧速度 + 9.8 * 时间间隔 
#   落地反弹:if 新高度 < 球半径:                                    
#                应设置新高度=球半径
#                然后速度方向取反

from time import sleep
from tkinter import *


if __name__ == '__main__':
    root = Tk()
    H = 600
    canvas = Canvas(root,width=300, height=H)

    x = 150
    h = 500
    r = 20
    dt = 1.0/60
    refresh = dt - 1.0 / 120

    ball = canvas.create_oval(x-r, H-h-r, x+r, H-h+r)
    canvas.pack()

    root.update()
    
    v = 0
    while True:
        sleep(refresh)
        v += 9.8 * dt
        dh = v * dt
        h -= dh
        if h < r:
            h = r
            v = -v
            canvas.moveto(ball, x-r, H-h-r)
        else:
            canvas.move(ball, 0, dh)
        root.update()