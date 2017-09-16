size(500,500)


fill(None)
stroke(0,1,0)
def printPoint(x,y):
    oval(x-3, y-3, 6, 6)



a = (100,100)
b = (100,400)
c = (275,400)
c2 = (360,400)
c3 = (400,360)
d = (400,300)
d2 = (400,240)
d3 = (360,200)
e = (275,200)
f = (100,200)
g = (400,100)
points = [a,b,c,c2,c3,d,d2,d3,e,f,g]

for point in points:
    printPoint(point[0],point[1])


fill(None)
stroke(1,0,0)


path = BezierPath()
path.moveTo(a)
path.lineTo(b)
path.lineTo(c)

path.curveTo(c2,c3,d)
path.curveTo(d2,d3,e)
path.lineTo(f)
path.lineTo(e)
path.lineTo(g)

drawPath(path)


