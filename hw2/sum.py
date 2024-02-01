# 输入自然数m和n,输出m和n之间所有奇数的和.要求能多次输入并计算.

if __name__=='__main__':
    while True:
        try:
            m = int(input("输入整数 m："))
            n = int(input("输入整数 n："))
        except ValueError:
            break
        if n < m:
            m, n = n, m
        sum = 0
        for i in range(m,n+1):
            if i % 2 == 1:
                sum += i
        print("之间的所有奇数和为：%d" % sum)