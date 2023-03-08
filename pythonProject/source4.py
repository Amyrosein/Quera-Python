class Foo:
    def __init__(self, x = 0):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        if val >= 0:
            self._x = int(str(val)[-2:])
        else:
            self._x = -1


