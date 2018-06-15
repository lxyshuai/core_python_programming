# Python对象
## Python对象
* Python对象拥有三个特性:身份,类型和值
    * 身份:每一个对象都有一个唯一的身份标识.对象的内存地址,使用内建函数id()获得.
    * 类型:对象类型决定对象可以保持神秘类型的值.可以用内建函数type()查看.在Python中类型也是对象,所以type()返回的是对象不是字符串
    * 值:对象表示的数据项
* 对象属性:属性,值或可执行代码.

## 标准类型(基本数据类型,Python内建的基本数据类型)
* Integer
* Boolean
* Long Integer
* Floating point real number
* Complex number
* String
* List
* Tuple
* Dictionary

## 其他内建类型
* type
* Null对象(None)
* File
* set/frozenset
* 函数/方法
* 模块
* 类

### 类型对象和type类型对象
* 所有类型对象的类型都是type,type也是所有Python类型的根和所有Python标准类的默认元类
* 类就是类型,实例是对应类型的对象

### None
* Python有一个特殊的类型,称为Null对象或NoneType,只有一个值,就是None.不支持任何运算也没有内建方法
* None没有可用属性,布尔值也总是False
* 核心风格:任何标准对象都可用于布尔测试.每个对象天生拥有True或False.空对象,值为0的任何数字或者Null对象None布尔值都是False.其余都是True.用户可通过定义``__nonzero__()``或``__len__()``为0定义布尔值为False

## 内部类型
* 代码
* 帧
* 跟踪记录
* 切片
* 省略
* Xrange

### 代码
* 代码对象是编译过的Python源代码对象,是可执行对象.
* 通过调用内建函数compile()得到代码对象.
* 代码对象可以被 exec命令或内建函数eval()执行
* 代码对象不包括任何执行环境信息,是用户自定义函数的核心,函数的一个属性,在执行时获得上下文.
* 一个函数除了有代码对象属性意外,还有一些其他函数必须的属性,包括函数名,文档字符,默认参数,命名空间等

### 帧对象
* 帧对象表示Python的执行栈帧.
* 帧对象包含Python解释器在运行时需要的所有信息
* 帧对象属性包括上一帧的链接,正在执行的代码对象,本地及全局名称空间字典及当前指令等.
* 每次函数调用产生一个新的帧,对应一个C栈帧
* 用到帧对象的一个地方是跟踪记录对象

### 跟踪记录对象
* 当异常发生,一个针对异常的栈跟踪信息的跟踪记录对象诶创建.如歌一个异常有自己处理程序,处理程序就可以访问这个跟踪记录对象

### 切片对象
* 当使用扩展切片语法就会创建切片对象.
* 切片对象也可以由内建函数sliece()生成

### 省略对象
* 省略对象用于扩展切片语法,起做记号作用.这个对象在切片语法中表示省略号
* 唯一名字Ellipsis,布尔值为True

### XRange对象
调用内建函数xrange()生成Xrange对象,用于节省内存或range()无法完成的超大数据集场合

## 标准类型比较
### 对象值比较
``<`` ``<=`` ``>`` ``>=`` ``==`` ``!=`` ``<>``

### 对象身份比较
* ``is``测试两个变量是否指向同一对象
* ``==``比较变量的值
* Python整型对象和字符串对象是不可变对象,有高效缓存机制.(整型有范围)

### 布尔类型
``not`` ``and`` ``or``

## 标准类型内建函数
### type()
* Python会以一种相对标准的格式表示对象,<object_something_or_another>

### cmp()
* 比较两个对象大小
```python
a, b = -4, 12
cmp(a,b)
```
* 如果是用户自定义对象,会调用该类的特殊方法``__cmp__()``

### str(),repr()
* ``str()``函数得到字符串可读性好
* ``repr()``函数得到的字符串通常可以重新获得该对象,``obj == eval(repr(obj))``通常成立
* \`\`和``repr()``通常做一样的事情

### type(),isinstance()
```python
class Foo: # 旧式类
    pass
class Bar(object): # 新式类
    pass
foo = Foo()
bar = Bar()
print type(Foo) # <type 'classobj'>
print type(foo) # <type 'instance'>
print type(Bar) # <type 'type'>
print type(bar) # <class '__main__.Bar'>
```
* 在python2中,旧式类的type是classobj,旧式类实例的type是instance.新式类(继承了object),该类type是type,该类实例是该类.

## 类型工厂函数
* python2.2统一了类和类型,内建转换函数像int(),type(),list()都变成工厂函数.实质上是类.

## 标准类型分类
### 存储模型
|分类| Python类型|
| ---------- | --- |
| 标量/原子|  数值,字符串 |
| 容器| list,tuple,dict|

### 更新模型
分类 | Python类型
---- | ---
可变 | list,dict
不可变 | 数字,字符串,tuple

### 访问模型
分类 | Python类型
---- | ---
直接访问 | 数字
顺序访问 | list,字符串,tuple
映射访问 | dict

## 不支持类型
* char
* byte
* 指针
* int short long
* float double
