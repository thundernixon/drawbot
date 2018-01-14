CANVAS = 500
SQUARESIZE = 158
NSQUARES = 100
SQUAREDIST = 1.2

width = NSQUARES * SQUAREDIST

NFRAMES = 50

for frame in range(NFRAMES):
    newPage(CANVAS, CANVAS)
    frameDuration(1/20)
    
    fill(0)
    rect(0, 0, CANVAS, CANVAS)

    phase = 2 * pi * frame / NFRAMES  # angle in radians
    startAngle = 90 * sin(phase)
    endAngle = 90 * sin(phase + pi * .5)

    translate(CANVAS/2 - width / 2, CANVAS/2)

    fill(1)
    stroke(0)

    for i in range(NSQUARES + 1):
        f = i / NSQUARES
        save()
        translate(i * SQUAREDIST, 0)
        scale(0.7, 1)
        rotate(startAngle + f * (endAngle - startAngle))
        rect(-SQUARESIZE/2, -SQUARESIZE/2, SQUARESIZE, SQUARESIZE)
        restore()

saveImage("StackOfSquares5.gif")