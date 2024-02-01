# 一、输入正整数n，输出n行由大写字母（从A-Z重复使用）组成的三角形阵列。
# 例如：输入3，输出
# A B C 
# D E
# F
# 又如：输入7，输出
# A B C D E F G
# H I J K L M
# N O P Q R
# S T U V
# W X Y
# Z A
# B
# 注意:输出数据的产生,利用ord和chr会很方便.

if __name__=='__main__':
    n = input("请输入正整数 n：")
    n = int(n)
    cur = ord('A')
    for i in range(n):
        for j in range(n-i):
            print(chr(cur), end=" ")
            cur += 1
            if cur > ord('Z'):
                cur = ord('A')
        print("", end='\n')