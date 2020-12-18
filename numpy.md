# numpy教程

## numpy 数组属性
axis = 0 即对列进行操作
```
ndim —— 维度
shape —— n 行 m 列
size —— n * m 元素个数
dtype —— 元素类型
itemize —— 每个元素的大小
flags —— 内存信息
real —— 实部
image —— 虚部
```

## numpy 创建数组
```
numpy.zeros(shape)
numpy.ones(shape)
```

## numpy 数组操作
```
reshape —— 不改变数据条件下改变形状
transpose —— 对换数组对维度
```

## numpy 数学函数
```
np.sin()
np.cos()
np.tan()
np.around(a, decimals = 1) —— 保留一位小数
np.floor() —— 向下取整
np.ceil() —— 向上取整
```

## numpy 算术函数
```
np.add(a, b)
np.substract(a, b)
np.multiply(a, b)
np.divide(a, b)
np.power(a, index)
np.mode(a, b)
```

## numpy 统计函数
```
np.amin(a, axis)
np.amax(a, axis)
np.mean(a, axis)
np.average(a, axis)
np.var(a)
np.std(a)
```