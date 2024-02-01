# 从Canvas下载数据文件data.txt，文件每一行是用逗号分隔的15个数据。如第1行：
# 25, Private, 2261002, 11th, 7, Never-married, Machine-op-inspct, Own-child, Black, Male, 0, 0, 40, United-States, <=50K.

# 15个数据中，第4，9，10，15个数据的含义如下（x表示忽略其他11个数据）：
# x，x，x，教育程度，x，x，x，x，种族，性别，x，x，x，x，收入
# 这四个数据可能取的值分别是：
# 教育程度值: Preschool, 1st-4th, 5th-6th, 7th-8th, 9th, 10th, 11th,12th, HS-grad, Assoc-acdm, Assoc-voc, Prof-school, Some-college, Bachelors, Masters, Doctorate.
# 种族值: White, Black, Asian-Pac-Islander, Amer-Indian-Eskimo, Other.
# 性别值: Female, Male.
# 收入值：<=50K, >50K

# 按如下维度，分别统计各类人群的收入情况，即某类人群中<=50K和>50K的各占多少？
# 教育：有学位的人（Bachelors/Masters/Doctorate） vs 其他人
# 种族：白人（White）vs 其他人
# 性别：男人（Male）vs 女人（Female）

# 用图形给出直观的结果（例如用分为两色的柱状图表示各占的比例）。如果时间不够，以文字形式输出。

from tkinter import *


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        line = f.readline()

        degreed = 0
        white = 0
        male = 0
        poor = 0

        hc = 0
        
        while line:
            objs = line.split(', ')
            if objs[3] == 'Bachelors' or objs[3] == 'Masters' or objs[3] == 'Doctorate':
                degreed += 1
            if objs[8] == 'White':
                white += 1
            if objs[9] == 'Male':
                male += 1
            if objs[14] == '<=50K.\n':
                poor += 1
            hc += 1
            line = f.readline()

    root = Tk()

    margin = 20
    width = (4) * 100 + margin * 2
    height = 300
    c = Canvas(root, width=width, height=height)
    c.pack()
    c.create_line(margin, height - margin, width - margin, height - margin)
    c.create_line(margin, height - margin, margin, margin)

    labelone = ["Degreed", "White", "Male", "<=50K"]
    labeltwo = ["Others", "Others", "Female", ">50K"]

    for i, v in enumerate([degreed, white, male, poor]):
        c.create_rectangle(margin + 100 * i + 30, height - margin, margin + 100 * i + 15 + 30, height - margin - v / hc * (height - margin * 2), fill='blue')
        c.create_text(margin + 100 * i + 30 + 15 - 2, height - margin, text='%s' % labelone[i], anchor=NE)
        c.create_text(margin + 100 * i + 15 + 30, height - margin - v / hc * (height - margin * 2), text="%2.0f%%" % ((100.0 * v) / hc), anchor=SE, fill="blue")
        c.create_rectangle(margin + 100 * i + 15 + 30, height - margin, margin + 100 * i + 30 + 30, height - margin - (hc - v) / hc * (height - margin * 2), fill='red')
        c.create_text(margin + 100 * i + 15 + 30 + 2, height - margin, text='%s' % labeltwo[i], anchor=NW)
        c.create_text(margin + 100 * i + 15 + 30, height - margin - (hc - v) / hc * (height - margin * 2), text="%2.0f%%" % ((100.0 * (hc - v)) / hc), anchor=SW, fill="red")
    
    root.mainloop()