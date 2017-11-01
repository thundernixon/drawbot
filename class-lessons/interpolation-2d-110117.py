def dot(center, diameter):
    cx, cy = center
    radius = diameter / 2
    oval(cx - radius, cy - radius, diameter, diameter)

def interpolatePoints(a,b,f):
    ax, ay = a
    bx, by = b
    mx = ax + f * (bx - ax)
    my = ay + f * (by - ay)
    return (mx, my)

a = (228, 244)
b = (604, 642)
m = interpolatePoints(a,b,0.7)

y = 500
dotSize = 15

dot(a, dotSize)
dot(b, dotSize)
fill(1,0,0)
dot(m, dotSize) 

fill(0,0,1,0.5)
numSteps = 29
for i in range(1, numSteps):
    f = i / numSteps
    print f
    dot(interpolatePoints(a,b,f), 30)
