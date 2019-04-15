import numpy as np
arr = np.arange(15).reshape((3, 5))
# print(arr)


# 对数组进行转置
# print(arr.T)

# 也是对ndarray进行转置
# print(arr.transpose())


# arr = np.random.randn(6, 3)
# 计算矩阵内积
# print(np.dot(arr.T, arr))

# 对于高维数组，tranpose需要得到一个由轴编号组成的元祖才能对这些轴进行转置(比较费脑子)
# arr = np.arange(16).reshape((2, 2, 4))
# print(arr)

# 对高维矩阵进行转置，第1个轴被换成第2个，第2个轴被换成第1个，最后一个轴不变
# print(arr.transpose((1, 0, 2)))

# swapaxes(),需要接收一对轴编号,用来交换轴
arr = np.arange(16).reshape((2, 2, 4))
print("arr : ")
print(arr)

arr = np.array([[1, 2], [3, 4]])
print("swapaxes : ")
print(arr.swapaxes(0, 1))