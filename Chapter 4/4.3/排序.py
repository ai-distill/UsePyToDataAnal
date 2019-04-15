import numpy as np

arr = np.random.randn(6)
print(arr)

# 通过sort方法进行就地排序
arr.sort()  # 默认是升序
print(arr)