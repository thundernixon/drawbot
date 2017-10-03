
Variable([
    dict(name="rotation", ui="Slider",
            args=dict(
                # some vanilla specific
                # setting for a slider
                value=0,
                minValue=0,
                maxValue=720)),
    dict(name="numberOfOvals", ui="Slider",
            args=dict(
                # some vanilla specific
                # setting for a slider
                value=1,
                minValue=1,
                maxValue=100))
    ], globals())

canvasWidth = 1000
canvasHeight = canvasWidth
ovals = 5

rotate(rotation)
# translate(x=canvasWidth/2, y=canvasWidth/2)

ovals = int(numberOfOvals)

for i in range(0,ovals):
    ovalSize = canvasWidth/((ovals * 2)+1)
    x = ovalSize + (i * ovalSize*2)
    for j in range(0,ovals):
        y = ovalSize + (j * ovalSize * 2)
        oval(x,y, ovalSize, ovalSize)