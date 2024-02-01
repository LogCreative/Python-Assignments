# 输入一个四位整数，对其加密后输出。
# 加密方法：每位数字分别加9后除以10取余数，从而得到四位新数字。然后将千位和十位数字互换,百位和个位数字互换。
# 例如：输入2017，经加密后输出0619。注意加密后四位整数最高位是0时也要输出。
# 思考：题目要求输入整数，程序中的数据就必须用int类型吗？
# 要求：数据分别用整数表示和字符串表示，完成两个版本。

_str = input("请输入四位整数：")

# 整数版本
num = int(_str)
num_digits = []
for i in range(4):      # 保证 4 位
    num_digits.insert(0,num % 10)
    num = int(num / 10)
encrpt_digits = []
for digit in num_digits:
    encrpt_digits.append((digit + 9) % 10)
encrpt_digits[2], encrpt_digits[0] = encrpt_digits[0], encrpt_digits[2]
encrpt_digits[3], encrpt_digits[1] = encrpt_digits[1], encrpt_digits[3]
encrpted = 0
for digit in encrpt_digits:
    encrpted = encrpted * 10 + digit
print("加密后的整数为：%04d" % encrpted)
