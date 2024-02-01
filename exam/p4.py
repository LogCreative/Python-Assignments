# 甲乙丙丁讨论四姑娘山之大峰、二峰、三峰、幺妹峰的高度排名。
# 甲说：三峰第1，大峰第4；
# 乙说：大峰第1，幺妹峰第2，二峰第3，三峰第4；
# 丙说：三峰第3，大峰第4；
# 丁说：幺妹峰第1，大峰第2，三峰第3，二峰第4。
# 已知每人只判断对了一个名次。请用枚举法编程计算各峰的排名。
# 注意代码风格，超长超繁琐的判断条件不是好风格。（15分）

statments = [
    [[3,1], [1,4]],
    [[1,1], [4,2], [2,3], [3,4]],
    [[3,3], [1,4]],
    [[4,1], [1,2], [3,3], [2,4]]
]

# 名次不能冲突
# 对每个人的情形进行遍历

# [[]] -> [[0],[1]] -> [[0,0],[0,1],[0,2],[0,3],[1,0],...
iter_list = [[]]
for p in statments:
    items = []
    for i in range(len(p)):
        for item in iter_list:
            items.append(item + [i])
    iter_list = items

for possible in iter_list:
    cur = {}
    notlist = {}
    rank = {}
    flag = True
    for j in range(len(statments)):
        correct = possible[j]
        guess = statments[j][correct]
        if guess[0] in cur and cur[guess[0]] != guess[1]:
            flag = False
            break
        if guess[0] in notlist and guess[1] in notlist:
            flag = False
            break
        if guess[1] in rank and rank[guess[1]] != guess[0]:
            flag = False
            break
        rank[guess[1]] = guess[0]
        cur[guess[0]] = guess[1]
        for i in range(len(statments[j])):
            if i == j:
                continue
            notguess = statments[j][i]
            if notguess[0] in notlist:
                notlist[notguess[0]].add(notguess[1])
            else:
                notlist[notguess[0]] = set([notguess[1]])
    if flag:
        remainname = [1,2,3,4]
        remainrank = [1,2,3,4]
        for k in cur:
            remainname.remove(k)
            remainrank.remove(cur[k])
            print("%d 峰为第 %d 位" % (k, cur[k]))
        print("%d 峰为第 %d 位" % (remainname[0], remainname[0]))
