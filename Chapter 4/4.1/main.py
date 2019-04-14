import numpy as np
print(np.__version__)

# 返回一个采用随机正态分布的矩阵，每个元素都是0-1之间的数字
data = np.random.randn(2, 3)
print(data)

# 矩阵中所有元素都*10
print(data * 10)
# 每个元素与自身相加
print(data + data)

# 打印元素的形状和类型
print(data.dtype)
print(data.shape)

# 创建ndarray
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
print(type(arr1))

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)  # 打印维度

# 创建指定长度的全0数组
arr3 = np.zeros(10)
print(arr3)

# 创建指定长度的全1数组
arr4 = np.ones((3, 6))
print(arr4)

# 使用empty()创建全0数组是不安全的，默认会返回一堆尚未初始化的垃圾值
arr5 = np.empty((2, 3, 2))
print(arr5)


# numpy中的arange函数等同于Python中的range函数
arr6 = np.arange(15)
print(arr6)


# eye(N) 创建一个正方形的N维数组，除了主对角线为1剩下全为0
arr7 = np.eye(10)
print(arr7)

# identity(N) 创建一个正方形的N维数组，除了主对角线为1剩下全为0
arr8 = np.identity(10)
print(arr8)