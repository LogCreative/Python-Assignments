# 本程序使用 Python 3 编写
#
# 输入年份, 输出该年是否闰年.
#
# 如果年份能被4整除,且能被100整除时也能被400整除, 则为闰年.
#

if __name__=='__main__':
    year = int(input("请输入年份:"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        # 优先级 and > or，如果左边是被 100 整除的，为 false 会判断右边的条件。
        print("%5d 是闰年" % year)
    else:
        print("%5d 不是闰年" % year)