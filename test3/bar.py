# 2. 输入本金a,年利率i,年数n.计算今后n年的增值情况,计算公式是
# a*((1+i)**n)
# 并用柱状图表示(例如可画成下面形状).
# 注意:为了适应图形窗口大小,最大高度应随a,i,n而定.

from tkinter import *

def money(a, i, year):
    return a*((1+i)**year)

if __name__=='__main__':
    a = int(input("请输入本金："))
    i = float(input("请输入年利率："))
    n = int(input("请输入年数："))

    total = money(a, i, n)

    root = Tk()

    margin = 20
    width = (n + 1) * 50 + margin * 2
    height = 300
    c = Canvas(root, width=width, height=height)
    c.pack()
    c.create_line(margin, height - margin, width - margin, height - margin)
    c.create_line(margin, height - margin, margin, margin)
    for y in range(n+1):
        ym = money(a, i, y)
        c.create_rectangle(margin + 50 * y + 15, height - margin, margin + 50 * y + 20 + 15, height - margin - ym / total * (height - margin * 2), fill='blue')
        c.create_text(margin + 50 * y + 10 + 15, height - margin - ym / total * (height - margin * 2),text='%0.2f' % ym,anchor=S)
        c.create_text(margin + 50 * y + 10 + 15, height - margin, text='%d' % y, anchor=N)

    root.mainloop()