# 快速显示一组静态图像形成动画。
# Canvas下载yupan.rar并解压，得到23个图像文件（yupanN.gif）。在画布上按次序逐一显示这些图像。
# 注意：一幅图像显示过后最好从画布上删除，以免画布上item过多，尤其是在循环播放动画的情况下。另外注意图像文件存储路径，最好与程序文件存储在一个目录，这样PhotoImage(file=...)中就无需指明图像文件路径，用文件名即可。（文件名有规律哦，你不会用23条语句来创建图像对象吧？）

from time import sleep
from tkinter import *

if __name__ == '__main__':
    root = Tk()

    duration = 1.0/24
    
    l = None
    while True:
        for i in range(1, 24):
            if l:
                l.pack_forget()
            p = PhotoImage(file="yupan/yupan" + str(i) + ".gif")
            l = Label(root, image=p)
            l.pack()
            root.update()
            sleep(duration)