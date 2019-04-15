names = ['yirufeng', 'wuxiaowen']
ages = [18, 22]
for name, age in names, ages:
    print(name, age)

# zip() 函数用于将可迭代的对象作为参数，
# 将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
for name, age in zip(names, ages):
    print(name, age)