import numpy as np
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# numpy的where函数是三元表达式x if condition else y的矢量化版本

## 下面是使用纯Python,如果对于大数组处理速度并不是很快；第二，无法应用于多维数组
result = [(x if c else y)
            for x, y, c in zip(xarr, yarr, cond)]
print(result)

## 采用Numpy进行处理, 第2个参数和第3个参数不必是数组，可以是标量值。
result = np.where(cond, xarr, yarr)
print(result)


arr = np.random.randn(4, 4)
print(arr)
print(arr > 0)

## 用常数2替换arr中所有正的值
## 传递给where的数组大小可以不相等，甚至可以是标量
print(np.where(arr > 0, 2, arr))