# python 系统学习
    系统学习一门语言，比半知不解就开始写代码，要好！
## 函数定义形式
1. 参数默认值 : 只有prompt是必须给出的，其余两个参数都有默认值
   ```
   def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
   
   ```
有以下几种调用方式：
- 只给出必需的参数：ask_ok('Do you really want to quit?')
- 给出一个可选的参数：ask_ok('OK to overwrite the file?', 2)
- 或者给出所有的参数：ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

注意：默认参数的类型不同

2. 关键字参数 : 形如kwarg = value来调用函数\
   传递参数的顺序不重要，重要的是key要对应
```
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```
以下几种方式是有效的：
```
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
```
以下几种则无效：
```
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
```

## 数据结构
1. 列表list
- 常用命令
```
list.append(x)
list.insert(i, x)
list.remove(x)
list.pop([i])
list.clear()
list.count(x)
list.sort(, key=None, reverse=False)
list.reverse()
list.copy()
```
- 作为stack使用
```
    stack.append(x)
    stack.pop()
```
- 作为queue使用
```
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  
queue.popleft()
```
-  列表推导式
```
# 更加python的写法
squares = [x ** 2 for x in range(10)]
```

2. 集合set

```
a = set()  # 初始化
a - b                              # letters in a but not in b
a | b                              # letters in a or b or both
a & b                              # letters in both a and b
a ^ b                              # letters in a or b but not both
```
3. 字典dict
- 常用指令
```
tel = {'jack': 4098, 'sape': 4139}
```

4. 模块概念
```
    from fibo import fib
    from fibo import *
```

5. 输入输出
更漂亮的输出格式
```
:后传递一个整数可以让该字段成为最小字符宽度
for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')

str.format()
```

6. 读写文件
```
f = open('workfile', 'w')
第一个参数是包含文件名，第二个参数是打开方式
r——只能读取 w——只能写入 r+——读写 a——追加

在处理文件对象时，最好使用with关键字。优点是当子句结束后文件会正确关闭
with open("filename","r") as f:
    f.read()

f.readline()——读取某一行
f.readlines()———以列表的形式读取
```

7. 使用json保存结构化数据
```
json.dumps() 序列化
json.dump() 文件内容序列化
json.loads() json格式化
json.load() 解码对象
```
8. 错误和异常
- 处理异常
  一个try语句可能有多个except子句，处理不同的异常
  ```
  try：

  except valueError:
  ```
- 抛出异常
  ```
  rasise NameError
  ```
- 用户自定义异常
  class Error():

- finally子句
  如果存在finnaly子句，则无论try是否异常，都会被执行

9. 类
- 作用域和命名空间
  namespace ：名字到对象都映射
- 派生类和基类
  派生类实例化，搜索相应属性，转往底层寻找
  派生类可能会重写基类的方法
  多重继承
- 私有变量
  python中是没有private的概念的，默认加下划线标识私有

10. 标准库
```
 os 模块
 sys 命令行参数
 re 正则表达式
 math 
 random 
 datatime
 threading多线程
 logging 日志
```