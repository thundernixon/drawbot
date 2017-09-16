size(500,500)


fill(None)
stroke(0,1,0)
def printPoint(x,y):
    oval(x-3, y-3, 6, 6)

a = (100,100)
b = (100,200)
c = (200,200)
d = (200,100)
e = (10,10)
points = [a,b,c,d,e]

for point in points:
    printPoint(point[0],point[1])

fill(None)
stroke(1,0,0)


path = BezierPath()
path.moveTo(a)
path.curveTo(b,c,d)
path.lineTo(e)

drawPath(path)