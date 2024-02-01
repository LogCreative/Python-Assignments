# 程序设计:画一幅冬季景色,有雪人圣诞树之类.

from tkinter import *

root = Tk()

c = Canvas(root, width=300, height=300, bg='white')

# floor
c.create_line(0,230,300,230)

# snowman
c.create_oval(100,190,140,230)
c.create_oval(108,167,132,191)

# tree
c.create_rectangle(219,230,226,170,fill='brown',outline='brown')
c.create_polygon(190,171,255,171,222,131,fill='white',outline='green')
c.create_polygon(195,141,250,141,222,106,fill='white',outline='green')
c.create_polygon(200,115,245,115,222,86,fill='white',outline='green')

# sun
c.create_oval(50,50,80,80,fill='yellow',outline='white')

c.pack()

root.mainloop()