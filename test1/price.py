# 水果价格查询：有4种水果，单价分别是3.00、2.50、4.10、10.20元/千克。
# 程序首先在屏幕上显示如下菜单：
# [1] 苹果
# [2] 梨
# [3] 橙子
# [4] 葡萄
# [0] 退出
# 请输入序号：
# 然后用户输入序号查询水果价格。每次运行程序可以连续查询4次，即：程序输出用户所选水果的单价后自动回到菜单让用户继续查询，当用户用完4次查询机会就自动退出。当然，任何时候用户可选择0主动退出。

name_price = [["苹果",3.00],["梨",2.50],["橙子",4.10],["葡萄",10.20]]
for i in range(4):
    for j in range(len(name_price)):
        print("[%1d] %s" % (j+1,name_price[j][0]))
    print("[0] 退出")
    num = input("请输入序号：")
    num = int(num)
    if num == 0:
        break
    elif num >= 1 and num <= 4:
        selected = name_price[num-1]
        print("%s的价格是 %2.2f 元/千克。" % (selected[0], selected[1]))
