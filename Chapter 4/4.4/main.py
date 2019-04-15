import numpy as np
arr = np.arange(10)
print(arr)
# 如果文件路径末尾没有扩展名.npy,则该扩展名会被自动加上
# 然后可以通过np.load读取磁盘上的数组
np.save('some_array', arr)

arr2 = np.load('some_array.npy')
print(arr2)

# 通过np.savez可以将多个数组保存到一个未压缩文件中，将数组以关键字形式传入即可
np.savez('array_archive.npz', n=arr, b=arr)

# 加载.npz文件时，你会得到一个类似字典的对象，该对象会对各个数组进行延迟的加载
arch = np.load("array_archive.npz")
print(arch['b'])

# 如果要将数据压缩，可以使用numpy.savez_compressed
np.savez_compressed('arrays_compresed.npz', a=arr, b=arr)
