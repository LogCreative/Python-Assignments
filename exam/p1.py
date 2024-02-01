# 输入正整数n，输出1～n之间的所有满足条件的正整数x：x各位数字的立方和等于x。
# 要求程序是模块化的：主函数调用函数p(x)，p(x)判断x是否满足条件，返回布尔值；而p(x)调用函数d(x)，d(x)返回x的各位数字组成的列表。(10分)

def d(x):
    str_x = str(x)
    return [int(d) for d in str_x]

def p(x):
    digit_x = d(x)
    return sum([d*d*d for d in digit_x]) == x

n = int(input("输入正整数 n:"))
for i in range(1, n+1):
    if p(i):
        print(i)