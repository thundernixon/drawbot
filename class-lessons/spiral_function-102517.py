def spiral(cx,cy, radius, rotation):
    save()
    translate(cx,cy)
    scale(radius/500)
    for i in range(50):
        rect(270,0,   ,40)
        rotate(1-(rotation*randint(5,36)*.025))     
        scale(1-(1*.025))
    restore()

margin = 101

gridSize = 200

for i in range(5):
    x= gridSize * i + margin
    for j in range(5):
        y= gridSize * j + margin
        spiral(x,y,gridSize/2, 50)  