# 二、输入两个正整数a和n，计算a + aa + aaa +...+ a...a（n个a）之和。要求定义函数f(a,n)用于计算n个a组成的数。
# 例如：输入2和3，输出2+22+222=246。
# 注意：函数该做和不该做哪些事。例如此题的“输入a和n”是f该做的事吗？另外如何构造n个a组成的aa...a才简便?

def f(a, n):
    sum = 0
    cur = 0
    for i in range(n):
        cur = cur * 10 + a
        sum += cur
    return sum

if __name__=='__main__':
    a = int(input("请输入正整数 a："))
    n = int(input("请输入正整数 n："))
    print("f(a,n)=%d" % f(a,n))