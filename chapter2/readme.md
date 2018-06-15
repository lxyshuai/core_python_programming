# 第2章 快速入门

``语句``:使用关键字组成命令,告诉解释器一个命令
``表达式``:表达式没有关键字.可以是使用数据操作构成的算术表达式,也可以是使用括号调用的函数

## 程序输出
```python
print 'Hello World'
print '%s is number %d!' % ("python", 1)
```
* print语句调用str()函数显示对象，交互式解释器则调用repr()函数显示对象
* 下划线(_)在解释器中有特殊含义，表示最后一个表达式的值
* print语句与字符串格式操作符(%)结合运用,实现字符串替换功能.%s表示由一个字符串替换,%d表示由一个整数替换,%f表示由一个浮点型替换.

```python
import sys
print >> sys.stdout, 'Fatal error : invalid input!'
logfile = open('./mylog.txt', 'a')
print >> logfile, 'Fatal error : invalid input!'
logfile.close()
```
* 符号>>用来重定向输出,可以将输出重定向到标准错误输出和日志文件

## 程序输入
```python
user = raw_input('Enter login name: ')
print 'Your login is:', user
num = raw_input('Now enter a number: ')
print 'Doubling your number: %d ' % (int(num) * 2)
```
* raw_input()读取标准输入,赋值到指定变量
* 核心风格:一直在函数外做用户交互操作

## 注释
```python
# one comment
def foo():
    '''This is a doc string'''
    return True
```
* #是单行注释
* 有一种叫做文档字符串的特别注释,在模块、类或者函数开始添加一个字符串,起到在线文档作用.
文档字符串可以在运行时访问,也可以自动生成文档

## 操作符
### 标准算术操作符
``+``  ``-``  ``*``  ``/``  ``//``  ``%``  ``**``
```python
print -2 * 4 + 3 ** 2
```
* ``+``  ``-``优先级最低,``*``  ``/``  ``//``  ``%``优先级较高,单目操作符``+``  ``-``(取正取负)优先级最高,``**``优先级最高

### 标准比较操作符
``<`` ``<=`` ``>`` ``>=`` ``==`` ``!=`` ``<>``
```python
print 2 < 4
print 2 == 4
print 2 > 4
print 6.2 <= 6
print 6.2 <= 6.2
print 6.2 <= 6.20001
```
* ``<>``慢慢淘汰,推荐用``!=``

### 逻辑操作符
``and`` ``or`` ``not``
```python
2 < 4 and 2 == 4
2 > 4 or 2 < 4
not 6.2 <= 6
3 < 4 < 5
```
* 核心风格:合理使用括号增强代码可读性

## 变量赋值
```python
counter = 0
n = n * 10
n*= 10
```
* 变量名大小写敏感
* Python动态类型语言,不需要事先声明变量类型,变量的类型在赋值那一刻被初始化
* Python支持增量赋值(操作符和等号合并在一起)
* Python不支持自增自减

## 数字
* 有符号整数(int) ``0011`` ``84`` ``-237`` ``0x80`` ``017`` ``-0X92``
    * 长整型 ``23213L``
    * 布尔值
* 浮点值
* 复数

