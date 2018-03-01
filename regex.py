import re
import geometry_primitives as gp

floatnumbers = re.compile('-?\d+.?\d+')
doubleslash = re.compile('\d+\/\/\d+')
intnumbers = re.compile('\d+')


def v(str):
    return gp.Point3D(floatnumbers.findall(str))


def f(str):
    pass


def init(file):
    points = []
    triangles = []
    try:
        while True:
            str = file.readline()
            if str == '':
                break
            char = re.match('v|f\b', str)
            if (char != None):
                if char.group(0) == 'v':
                    points.append(v(str))
                elif char.group(0) == 'f':
                    triangles.append(f(str))
    except EOFError:
        pass
