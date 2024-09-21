class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        if value < 0:
            self._x = 0
        elif value > 1000:
            self._x = 1000
        else:
            self._x = value
            
    @x.deleter
    def x(self):
        print('x foi deletado')
        self._x = 0

foo = Foo(10)
print(foo.x)  
del foo.x
print(foo.x)
foo.x = 1001
print(foo.x)