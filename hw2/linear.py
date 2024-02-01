from math import inf, nan

def slope(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    if dx == 0:
        return inf
    return dy / float(dx)

def intercept(p1, p2):
    # y1 = kx1 + b
    # y2 = kx2 + b
    k = slope(p1,p2)
    if k == inf:
        return nan
    return p1[1] - k * p1[0]

if __name__=='__main__':
    x1 = float(input("坐标 1 的 x："))
    y1 = float(input("坐标 1 的 y："))
    x2 = float(input("坐标 2 的 x："))
    y2 = float(input("坐标 2 的 y："))
    p1 = (x1, y1)
    p2 = (x2, y2)
    print("斜率为 %.2f，截距为 %.2f" % (slope(p1,p2), intercept(p1,p2)))