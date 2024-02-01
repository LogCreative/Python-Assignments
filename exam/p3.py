# 设计类Fangyuan描述形状：从一个正方形内部挖去一个圆后剩余部分。圆心即正方形中心。创建对象时提供参数：中心(x,y)、正方形边长a、圆直径d。注意d<a才有意义。对象的方法：
# draw(color)：画形状，且涂color颜色；
# move()：左键单击画布时，将形状移动至鼠标点击位置； 
# area()：右键单击画布时计算形状面积并将结果显示在画布左上角。（15分）

from tkinter import *
import math

root = Tk()

class Fangyuan:
    def __init__(self, center, a, d):
        if (d>=a):
            raise Exception("直径应小于边长！")
        self.center = center
        self.a = a
        self.d = d
        self.ha = self.a / 2
        self.r = self.d / 2
        self.canvas = Canvas(root, width=1000, height=800, bg='white')
        self.canvas.bind('<Button-1>', self.move)
        self.canvas.bind('<Button-3>', self.area)
        self.canvas.pack()

    def draw(self,color):
        self.rec = self.canvas.create_rectangle(
            self.center[0] - self.ha, self.center[1] - self.ha,
            self.center[0] + self.ha, self.center[1] + self.ha, fill=color)
        self.cir = self.canvas.create_oval(
            self.center[0] - self.r, self.center[1] - self.r,
            self.center[0] + self.r, self.center[1] + self.r, fill='white'
        )

    def move(self, e):
        if self.rec and self.cir:
            self.canvas.moveto(self.rec, e.x - self.ha, e.y - self.ha)
            self.canvas.moveto(self.cir, e.x - self.r, e.y - self.r)

    def area(self, e):
        A = self.a ** 2 - math.pi * self.d ** 2 / 4
        self.canvas.create_text(0,0,text=str(A),anchor=NW)
        self.canvas.update()

fy = Fangyuan((100,100), 50, 30)
fy.draw('yellow')

root.mainloop()