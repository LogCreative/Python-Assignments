# 输入x，计算下面这个函数并输出结果。

import math

x = input("请输入自变量 x：")
x = float(x)

res = 0
if x == 0:
    res = math.pi
else:
    t = math.sin(x) ** 2 + math.cos(x)
    if x > 0:
        res = (t + 1) ** 3 - 3 * t
    else:
        res = 4 * t - 1

print("结果为 %.4f" % res)
