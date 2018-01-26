CANVAS = 750
# SQUARESIZE = CANVAS * 0.258 * 2
SQUARESIZE = CANVAS * 0.35 * 2
NSQUARES = 100
SQUAREDIST = 1.5

width = NSQUARES * SQUAREDIST

NFRAMES = 45

for frame in range(NFRAMES):
    newPage(CANVAS, CANVAS)
    frameDuration(1/20)
    
    fill(0,0,1)
    rect(0, 0, CANVAS, CANVAS)

    phase = 2 * pi * frame / NFRAMES  # angle in radians
    startAngle = 135 * sin(phase)
    endAngle = 135 * sin(phase + pi * .5)
    
    print startAngle

    translate(CANVAS/2, CANVAS/2 - width+25)
    
    fill(1)
    fill(0,0,1)

    for i in range(NSQUARES + 1):
        f = i / NSQUARES
        
        save()

            
        translate(0, i * SQUAREDIST*1.25)
        scale(1, 0.8)
        rotate(startAngle + f * (endAngle - startAngle))

        ### rectangles – turn on to center different text
        # fill(1)
        # stroke(0)
        # rect(-SQUARESIZE/2, -SQUARESIZE/2, SQUARESIZE, SQUARESIZE)
        
        fill(0+f,0+f,1)
        
        if i == NSQUARES:
            fill(0,0,1)
        
        font("IBM Plex Mono Bold")
        # font("Times New Roman")
        fontSizeVal = SQUARESIZE*0.55
        fontSize(fontSizeVal)
        tracking(-5)
        lineHeight(fontSizeVal*0.85)
        translate(0,-fontSizeVal*0.3)
        scale(1.65, 1.15)
        textBox("NI" + "\n" + "CE", (-SQUARESIZE/2, -SQUARESIZE/2, SQUARESIZE, SQUARESIZE), align="center")
        restore()

# saveImage("StackOfNice9.gif")