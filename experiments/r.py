size(500,500)


def printPoint(x,y):
    oval(x-4, y-4, 8, 8)



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




fill(None)
stroke(1,0,0)
strokeWidth(3)


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

# show handles

stroke(0, 0, 0, .5)
strokeWidth(1)

handle1 = BezierPath()
handle1.moveTo(c)
handle1.lineTo(c2)
drawPath(handle1)

handle2 = BezierPath()
handle2.moveTo(d)
handle2.lineTo(c3)
drawPath(handle2)

handle3 = BezierPath()
handle3.moveTo(d)
handle3.lineTo(d2)
drawPath(handle3)

handle4 = BezierPath()
handle4.moveTo(e)
handle4.lineTo(d3)
drawPath(handle4)


# show handle "controls"


fill(None)
stroke(0,1,0)
strokeWidth(2)

for point in points:
    printPoint(point[0],point[1])
