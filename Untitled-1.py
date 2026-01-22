def dibuixar(Xx, Xy):
    Coord = [[[2,-2],  [2,-1], [2,0], [2,1], [2,2]],
             [[1,-2],  [1,-1], [1,0], [1,1], [1,2]],
             [[0,-2],  [0,-1], [0,0], [0,1], [0,2]],
             [[-1,-2],[-1,-1],[-1,0],[-1,1],[-1,2]],
             [[-2,-2],[-2,-1],[-2,0],[-2,1],[-2,2]]]
    XCoord = []
    for a in range(len(Coord)):
        XCoord.append[[]]
        XCoord.remove(None)
        for b in range(len(Coord[a])):
            XCoord[a] = XCoord[a].append([Xx(Coord[a][b][1], Coord[a][b][0]), Xy(Coord[a][b][1], Coord[a][b][0])])
    return XCoord

def X1x(x, y):
    return -y
def X1y(x, y):
    return x
def Euler(x, y, h, T):
    for a in range(0, int(T/h)):
        x = x - h*X1x(x, y)
        y = y + h*X1y(x, y)
    return x, y
print(dibuixar(X1x, X1y))   
x0  = 0
y0 = 1
h = 0.01
T = 10
print(Euler(x0, y0, h, T))

