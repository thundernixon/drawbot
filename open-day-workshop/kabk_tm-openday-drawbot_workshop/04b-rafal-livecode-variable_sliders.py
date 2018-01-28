Variable([
    dict(name="width", ui="Slider"),
    dict(name="height", ui="Slider"),
    dict(name="stemThickness", ui="Slider")
    ], globals()
    )

# var = 100
# x = 100
# y = 100
# width = 200
# height = 300


strokeWidth(53)
stroke(0.-2,0.5,0.8,0.8)
fill(0.5,0.5,0.8,0.8)

# left stem:
rect(100,100,stemThickness,height*10)
# right stem
rect(width*10,100,stemThickness,height*10)
# middle bar
rect(100,(height*10)/2+50,width*10, stemThickness)

# translation of starting point (0,0)
translate(width*10+stemThickness, 0)

rect(100,100,stemThickness,height*10)
