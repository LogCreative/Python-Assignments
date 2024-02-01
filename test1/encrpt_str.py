# 输入一个四位整数，对其加密后输出。
# 加密方法：每位数字分别加9后除以10取余数，从而得到四位新数字。然后将千位和十位数字互换,百位和个位数字互换。
# 例如：输入2017，经加密后输出0619。注意加密后四位整数最高位是0时也要输出。
# 思考：题目要求输入整数，程序中的数据就必须用int类型吗？
# 要求：数据分别用整数表示和字符串表示，完成两个版本。

_str = input("请输入四位整数：")

# 字符串版本
encrpt_digits = ""
for char in _str:
    encrpt_digits = encrpt_digits + str((int(char) + 9) % 10)
encrpted = ""
for i in [2,3,0,1]:     # [0,1,2,3] -> [2,3,0,1]
    encrpted = encrpted + encrpt_digits[i]
print("加密后的整数为：%4s" % encrpted)
