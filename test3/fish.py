# 1. 利用自顶向下设计方法编程：假设某人从2000年1月1日开始“三天打鱼两天晒网”，输入此后任意一个日期，问此人在这一天是在打鱼还是在晒网？
# 提示：可参考打印年历程序的一些函数模块。

def isLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def leapYears(year):
    cnt = 0
    for y in range(2000, year):
        if isLeapYear(y):
            cnt += 1
    return cnt

def yearPastDays(year):
    ly = leapYears(year)
    return (year - 2000) * 365 + ly

def monthPastDays(year, month):
    monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year):
        monthDays[1] = 29
    mDays = 0
    for m in range(0, month - 1):
        mDays += monthDays[m]
    return mDays

def numOfDays(year, month, day):
    yDays = yearPastDays(year)
    mDays = monthPastDays(year, month)
    return yDays + mDays + day

if __name__=='__main__':
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入日："))
    if (numOfDays(year, month, day) - 1) % 5 in [0,1,2]:
        print("该日打鱼。")
    else:
        print("该日晒网。")