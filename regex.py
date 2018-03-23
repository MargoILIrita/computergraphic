import re
import geometry_primitives as gp

# регулярные выражения для разных типов чисел
floatnumbers = re.compile('-?\d+\.?\d*')
intnumbers = re.compile('\d+')

# регулярные выражения для различных случаев описания полигонов
allvalues = re.compile('\d+\/\d+\/\d+')
twovalues = re.compile('\d+\/\d+\/?')
nosecondvalue = re.compile('\d+\/\/\d+')
onevalue = re.compile('\d+\/?')


# функция парсящая точку из файла типа obj
def v(str):
    return gp.Point3D(floatnumbers.findall(str))


# функция, парсящая информацию о полигоне
def f(str):
    polygonunits = []
    for x in str.split(' '):
        # находим совпадения шаблонов
        all = allvalues.match(x)
        two = twovalues.match(x)
        double = nosecondvalue.match(x)
        one = onevalue.match(x)
        # в зависимости от того, сколько чисел в наборе n/n/n разная логика сохранения юнита полигона
        if all != None:
            polygonunits.append(gp.PolygonUnit(all.group(0).split('/')))
        elif two != None:
            t = two.group(0).split('/')
            polygonunits.append(gp.PolygonUnit([t[0], t[1]]))
        elif double != None:
            t = double.group(0).split('//')
            polygonunits.append(gp.PolygonUnit([t[0], '0', t[1]]))
        elif one != None:
            polygonunits.append(gp.PolygonUnit([one.group(0).replace('/', '')]))
    return gp.Polygon(polygonunits)


# на данный момент читает только v и f
def init(file):
    points = []
    triangles = []
    try:
        while True:
            str = file.readline()
            if str == '':
                break
            char = re.match('[v, f]\s', str)
            if (char != None):
                if char.group(0) == 'v ':
                    points.append(v(str))
                elif char.group(0) == 'f ':
                    triangles.append(f(str))
    except Exception:
        pass
    print(points.__len__())
    print(triangles.__len__())
