# Setting sliders
Variable([
    dict(name="width", ui="Slider"),
    dict(name="height", ui="Slider"),
    dict(name="R", ui="Slider"),
    dict(name="G", ui="Slider"),
    dict(name="B", ui="Slider"),
    dict(name="alpha", ui="Slider"),
    dict(name="strokeThickness", ui="Slider"),
    ],globals())
    


# setting up: stroke thickness, stroke colour, fill colour
strokeWidth(strokeThickness)
stroke(0,0,0,1)
fill(R/100,G/100,B/100,alpha/100)

##### H
# left stem
rect(100,100,100,height*10)
# right stem
rect(width*10,100,100,height*10)
# middle bar
rect(100,height*10/2+52,width*10,100)


##### I

# moves the canvas to the right for the next shapes
translate(width*10+100,0)

# stem
rect((width*10/2+52),100,100,height*10)
# top bar
rect(100,height*10+52-50,width*10,100)
# bottom bar
rect(100,100,width*10,100)
print(width*10, width*5)