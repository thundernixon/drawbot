
# Variable([
#     dict(name="rotation", ui="Slider",
#             args=dict(
#                 # some vanilla specific
#                 # setting for a slider
#                 value=0,
#                 minValue=0,
#                 maxValue=720)),
#     dict(name="ovalsPerRow", ui="Slider",
#             args=dict(
#                 # some vanilla specific
#                 # setting for a slider
#                 value=1,
#                 minValue=1,
#                 maxValue=40))
#     ], globals())
# ovals = int(ovalsPerRow)

ovals = 10

w = 1000
h = w
ovals = 5

frames = 60



for i in range(frames):
    newPage(w, h)
    #move origin of each page to center of canvas
    translate(w/2, w/2)
    # rotate each page so that it will end up rotating 360 degrees
    rotate(i * 360/frames)

    rotation = 360/frames * i
    fill(1,1,.5,.25)
    stroke(1,0,0)
    rect(0,0,w, h)
    ovalSize = w/((ovals * 2)+1)

    for j in range(ovals):
        x = ovalSize + (j * ovalSize*2)
        print "frame is " + str(i) + " rect x " + str(j) + str(x)  
        for k in range(ovals):
            translate(-w/2, -w/2)
            y = ovalSize + (k * ovalSize * 2)
            fill(0,0,0)
            print "frame is " + str(i) + " rect y " + str(k) + str(y)
            rect(x,y, ovalSize, ovalSize)


saveImage('../gifs/rotating-squares.gif')