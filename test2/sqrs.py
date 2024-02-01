# 三、输入一个三位数n，找出100～n之间所有满足如下条件的数x：x是完全平方数并且x有两位数字相同，如144，676等。输出这样的x，并统计个数。


if __name__=='__main__':
    n = int(input("请输入三位数 n："))
    sqrtbase = 10
    cnt = 0
    while True:
        cur = sqrtbase * sqrtbase
        if cur > n:
            break
        cur_str = str(cur)
        if cur_str[0] == cur_str[1] or \
            cur_str[1] == cur_str[2] or \
                cur_str[0] == cur_str[2]:
            print("%d" % cur, end=" ")
            cnt += 1
        sqrtbase += 1
    print("\n个数为 %d" % cnt)