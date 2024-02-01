# 四、输入一个数字不全相同的三位数，然后进行“重排求差”操作：用这三个数字组成的最大数减去用这三个数字组成的最小数。再对所得到的差重复“重排求差”操作，直至“差”不再变化为止。输出操作过程。
# 例如：输入422，输出
# 422－224＝198
# 981－189＝792
# 972－279＝693
# 963－369＝594
# 954－459＝495
# 954－459＝495
# 注意：此题涉及常见的新旧值迭代模式。

def get_digit(n):
    n_str = str("%03d" % n)
    n_arr = []
    for c in n_str:
        n_arr.append(int(c))
    return n_arr

def to_number(arr):
    num = 0
    for d in arr:
        num = num * 10 + d
    return num

if __name__=="__main__":
    n = int(input("输入数字不全相同的三位数 n："))

    while True:
        digits = get_digit(n)
        min_num = sorted(digits)
        max_num = reversed(min_num)
        min_num = to_number(min_num)
        max_num = to_number(max_num)
        cur = max_num - min_num
        print("%3d - %3d = %3d" % (max_num, min_num, cur))
        if cur == n:
            break
        n = cur