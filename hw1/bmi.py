# 注意：本程序使用 Python 3 编写
#
# 12.程序设计: 输入体重(千克), 身高(米),计算身体质量指数BMI, 并输出健康信息.
#
# BMI=体重/身高**2. BMI在19以下为轻体重, [19,25)为健康体重, [25,28)为超重, 28以上为肥胖.

if __name__=='__main__':
    weight = float(input("请输入你的体重(千克):"))
    height = float(input("请输入你的身高(米):"))
    bmi = weight / (height ** 2)
    print("你的BMI指数为: %0.2f" % bmi)
    if bmi < 19:
        print("你的体重过轻。")
    elif bmi < 25:
        print("你的体重健康。")
    elif bmi < 28:
        print("你的体重超重。")
    else:
        print("你的体重肥胖。")
        