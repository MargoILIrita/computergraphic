class Point2D:
    def __init__(self, list, isfloat=True):
        if isfloat:
            self.setfloat(list[0], list[1])
        else:
            self.setint(list[0], list[1])

    def setfloat(self, x, y):
        self._x = float(x)
        self._y = float(y)
        self._isfloat = True

    def setint(self, x, y):
        self._x = int(x)
        self._y = int(y)
        self._isfloat = False

    def __str__(self):
        return (self._x, self._y).__str__()


class Point3D:
    def __init__(self, list, isfloat=True):
        if isfloat:
            self.setfloat(list[0], list[1], list[2])
        else:
            self.setint(list[0], list[1], list[2])

    def setfloat(self, x, y, z):
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)
        self._isfloat = True

    def setint(self, x, y, z):
        self._x = int(x)
        self._y = int(y)
        self._z = int(z)
        self._isfloat = False

    def __str__(self):
        return (self._x, self._y, self._z).__str__()


class PolygonUnit:
    def __init__(self, list):
        if list.__len__() == 1:
            self.vertex = int(list[0])
        elif list.__len__() == 2:
            self.vertex = int(list[0])
            self.texture = int(list[1])
        else:
            self.vertex = int(list[0])
            self.texture = int(list[1])
            self.normal = int(list[2])


class Polygon:
    def __init__(self, list):
        self._list = list
