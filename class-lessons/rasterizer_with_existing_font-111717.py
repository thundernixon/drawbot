scale(50)

bez = BezierPath()
bez.text("A", font="InputSans-Bold", fontSize=27, offset=(0,0))

for x in range(20):
    for y in range(20): 
        if bez.pointInside((x,y)):
            oval(x,y,0.8,0.8)
        else:
            oval(x,y,0.4,0.4)