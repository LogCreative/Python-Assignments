# 8. 利用筛法找出小于等于n的所有质数.

# 基本思想:首先创建从2到n的数值列表;然后将列表的第一个数(是质数)显示输出,并从列表中删除该数的所有倍数.重复此过程直至列表为空.

if __name__ == '__main__':
    n = int(input("请输入数值上限："))
    nums = list(range(2, n + 1))
    print("质数有：", end='')
    while len(nums) > 0:
        k = nums[0]
        print(k, end=' ')
        for i in range(k, n + 1, k):
            if i in nums:
                nums.remove(i)