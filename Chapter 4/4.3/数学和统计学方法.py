import numpy as np
arr = np.random.randn(5, 4)
print(arr)

# 通过数学上一组数学函数或对整个数组或某个轴进行统计计算

# 求算术平均数
print(arr.mean())
# 求算术平均数，与上面的代码等价
print(np.mean(arr))
# 求数组中全部元素的和
print(arr.sum())


# 统计函数可以接收一个axis选项参数，用于计算该轴上的统计值，最终结果是一个少一维的数组
print(arr.mean(axis=1))  # 计算行的平均值
print(arr.sum(axis=0))  # 计算每列的和


# cumsum和cumprod之类的方法则不聚合，而是产生一个由中间结果组成的数组
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr.cumsum())


# 在多维数组中，累加函数cumsum返回的是同样大小的数组，
# 但是会根据每个低维的切片沿着标记轴计算部分聚类
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr)


print(arr.cumsum(axis=0))
print(arr.cumprod(axis=1))

# 求ndarray的最大值
print(arr.max())
# 求ndarray的最小值
print(arr.min())
# 求ndarray的标准差,自由度可以调节，默认为n
print(arr.std())
# 求ndarray的方差,自由度可以调，默认为n
print(arr.var())
# 求ndarray的最大元素的索引
print(arr.argmax())
# 求ndarray的最小元素的索引
print(arr.argmin())
# 求ndarray的所有元素累加和
print(arr.cumsum())
# 求ndarray的所有元素累加积，
print(arr.cumprod())