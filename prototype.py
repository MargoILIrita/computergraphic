import meshh

def tofloat(t, isInt=False):
    tt = []
    for i in t:
        a = None
        try:
            if isInt:
                a = int(i)
            else:
                a = float(i)
        except:
            pass
        if a != None:
            tt.append(a)
    return tt

def splitto(strrr, chunk):
    tmp = []
    for s in strrr:
        t = s.split(chunk)
        t = tofloat(t, True)
        if t != None:
            tmp.append(t)
    return tmp

def init(filename):
    file = open(filename)
    strV = []
    strVT = []
    strVN = []
    strF = []
    g = ''

    try:
        while True:
            strs = file.readline().split(' ')
            if strs[0] == '':
                break
            if strs[0] == 'v':
                strV.append(tofloat(strs))
            elif strs[0] == 'vt':
                strVT.append(tofloat(strs))
            elif strs[0] == 'vn':
                strVN.append(tofloat(strs))
            elif strs[0] == 'f':
                strF.append(splitto(strs,'/'))
            elif strs[0] == 'g':
                g = strs[1]
    except EOFError:
        pass

    obj = meshh.Meshh()
    obj.vertices = strV
    obj.vertex_normals = strVN
    obj.texture_vertices = strVT
    obj.faces = strF
    obj.g = g
    return obj