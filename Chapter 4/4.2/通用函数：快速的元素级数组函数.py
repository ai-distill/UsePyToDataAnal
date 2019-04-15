import numpy as np

"""
arr = np.arange(10)
print(arr)

# 下面的两个函数都是一元函数，因为只有一个操作数或数组
print(np.sqrt(arr))
print(np.exp(arr))  # 返回e的幂次方

# 下面的都是二元函数，因为接收两个操作数或数组
x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)

# 计算x和y中元素级别最大的元素
print(np.maximum(x, y))
"""
# 有些函数可以返回多个数组，modf就是一个例子
# 返回浮点数数组的小数和整数部分
arr = np.random.randn(7) * 5
print(arr)

remainder, whole_part = np.modf(arr)
print(remainder)  # 返回浮点数数组的小数部分
print(whole_part)  # 返回浮点数数组的整数部分


print("arr---------------------")
print(arr)
# 需要接收一个out可选参数，这样数组就可以在数组原地进行操作
print(np.sqrt(arr, arr))
print(arr)