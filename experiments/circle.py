size(500,500)

a = (290, 248)
b = (323, 248)
c = (350, 275)
d = (350, 308)
e = (350, 341)
f = (323, 367)
g = (290, 367)
h = (257, 367)
i = (230, 341)
j = (230, 308)
k = (230, 275)
l = (257, 248)

points = [a,b,c,d,e,f,g,h,i,j,k,l]

fill(None);
stroke(0,1,1);

def printPoint(x, y):
    oval(x - 3, y - 3, 6, 6)

for point in points:
    printPoint(point[0], point[1])

fill(None);
stroke(0,.2,1);

newPath();
moveTo(a);
curveTo(b,c,d);
curveTo(e,f,g);
curveTo(h,i,j);
curveTo(k,l,a);

drawPath();