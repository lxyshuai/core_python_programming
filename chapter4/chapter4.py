# -*- coding:utf-8 -*-
class Foo: # 旧式类
    pass
class Bar(object): # 新式类
    pass
foo = Foo()
bar = Bar()
print type(Foo)
print type(foo)
print type(Bar)
print type(bar)