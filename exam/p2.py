# 我们学过的选择排序算法是针对一维数据的，试修改该算法，对给定的m行n列的二维数据排序。
# 例如，[[3,7,2,1], [5,8,4,0]]经排序变成[[0,1,2,3], [4,5,7,8]]。
# 注意，尽量少请求系统分配存储空间。例如，将二维列表中的数据拷贝到一个新建的一维列表（即请求分配存储空间），然后抄书上的排序代码。（10分）

def merge(list1, list2, arr):
    i1 = 0
    i2 = 0
    n1 = len(list1)
    n2 = len(list2)
    k = 0
    while i1 < n1 and i2 < n2:
        j1 = list1[i1]
        j2 = list2[i2]
        if j1 < j2:
            arr[k] = j1
            i1 += 1
        else:
            arr[k] = j2
            i2 += 1
        k += 1
    while i1 < n1:
        arr[k] = list1[i1]
        i1 += 1
        k += 1
    while i2 < n2:
        arr[k] = list2[i2]
        i2 += 1
        k += 1

def mergeSort1D(arr):
    n = len(arr)
    if n > 1:
        m = n // 2
        list1, list2 = arr[:m], arr[m:]
        mergeSort1D(list1)
        mergeSort1D(list2)
        merge(list1, list2, arr)

def sort2D(array):
    m = len(array)
    n = len(array[0])
    array1D = []
    for l in array:
        array1D.extend(l)
    mergeSort1D(array1D)
    for i in range(m):
        for j in range(n):
            array[i][j] = array1D[i * n + j]
    return array

print(sort2D([[3,7,2,1], [5,8,4,0]]))