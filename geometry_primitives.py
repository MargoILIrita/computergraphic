import PIL.Image as pilimg
from PIL import ImageDraw
from PIL.ImageQt import rgb


# описывает точку в двумерном пространстве
# на вход конструктора list of String
class Point2D:
    def __init__(self, list, color=None, isfloat=True):
        if isfloat:
            self.setfloat(list[0], list[1])
        else:
            self.setint(list[0], list[1])
        # PIL.ImageQt.rgb
        self.color = color

    def setfloat(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self._isfloat = True

    def setint(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self._isfloat = False

    def __str__(self):
        return (self.x, self.y).__str__()


# описывает точку в трёхмерном пространстве
#на вход конструктора list of String
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


# описывает узлы полигона.
# Vertex - номер точки, обязательный;
# Texture - текстурная координата, необязательный
# Normal - нормаль, необязательна
# конструктор принимает list of String
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

    # был нужен для печати в консоль, пока оставлю
    def __str__(self):
        try:
            return (self.vertex, self.texture if self.texture != None else '',
                    self.normal if self.normal != None else '').__str__()
        except AttributeError:
            try:
                return (self.vertex, self.texture if self.texture != None else '').__str__()
            except AttributeError:
                return (self.vertex).__str__()


#описывает полигон, на вход рекомендуется list of PolygonUnit
class Polygon:
    def __init__(self, list):
        self._list = list

    def __str__(self):
        rlist = []
        for s in self._list:
            rlist.append(s.__str__())
        return rlist.__str__()


class Image:
    def __init__(self, points):
        self.points = points

    def draw(self, filename):
        img = pilimg.new('RGB', self._getMaxXY(), rgb(255, 255, 255))
        imgDrawer = ImageDraw.Draw(img)
        for p in self.points:
            imgDrawer.point([p.x, p.y], p.color)
        img.save(filename)

    def _getMaxXY(self):
        x, y = 0
        for p in self.points:
            if Point2D(p).x > x:
                x = Point2D(p).x
            if Point2D(p).y > y:
                y = Point2D(p).y
        return (x, y)
