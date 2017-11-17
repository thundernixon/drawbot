canvasSize = 500

numSteps = 25
dotSize = canvasSize / numSteps

numFrames = 20

for frame in range(numFrames):
    t = frame / numFrames
    print t
    newPage(500,500)
    
    amplitude = 100
    ampChange = 50

    for i in range(numSteps + 1):
        numPixels = 30
        f = i / numPixels #between 1 and 0
        angleA = 2 * pi * f
        diameter = .25 + 0.6 * (1 + sin(angleA + 2 * pi * t))
        x = i * dotSize
        angle = 360 * i / numSteps
        angle += t * 360 # change this number to see wave move! 0 and 360 give the same result
        print i, angle
        # y  = 500 + 200 * sin(-0.14) # sin wave multiplier naturally eases
        y = 250 + amplitude * sin(radians(angle)) # converts current angle to radians # the other added values will change position and amplitude
        oval(x,y, diameter*16, diameter*16) 
        save()
        translate(0,400)
        oval(x,y*-.5, diameter*8, diameter*8) 
        restore()
        
saveImage("../exports/gifs/wavyWave-4-111717.gif")