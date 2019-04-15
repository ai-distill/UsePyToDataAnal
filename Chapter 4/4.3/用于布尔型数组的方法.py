import numpy as np
arr = np.random.randn(10)
print(arr)
# 求正数的个数
print((arr > 0).sum())
print(arr > 0)

bools = np.array([False, False, True, False])
# any方法，any用于测试数组中是否存在一个或多个True
print(bools.any())
# all方法，all则检查数组中所有值是否都是True
print(bools.all())