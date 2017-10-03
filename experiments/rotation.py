
Variable([
    dict(name="rotation", ui="Slider",
            args=dict(
                # some vanilla specific
                # setting for a slider
                value=0,
                minValue=0,
                maxValue=720)),
    dict(name="ovalsPerRow", ui="Slider",
            args=dict(
                # some vanilla specific
                # setting for a slider
                value=1,
                minValue=1,
                maxValue=40))
    ], globals())

canvasWidth = 1000
canvasHeight = canvasWidth
ovals = 5




ovals = int(ovalsPerRow)

for i in range(0,ovals):
    # fill(1,1,.5)
    # rect(5,5,canvasWidth, canvasHeight)
    ovalSize = canvasWidth/((ovals * 2)+1)
    x = ovalSize + (i * ovalSize*2)
    for j in range(0,ovals):
        translate(canvasWidth/2, canvasWidth/2)
        rotate(rotation)
        y = ovalSize + (j * ovalSize * 2)
        oval(x,y, ovalSize, ovalSize)