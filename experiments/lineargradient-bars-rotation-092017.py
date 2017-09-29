w = 1000
h = w

frames = 40
divs = 16

def interpolate(a, b, t):
    interAB = a*(1-t) + b*t
    return interAB
    
def interpolateB(a, b, t):
    interAB = a*(1-t) + b*t
    return interAB
    
colorA = (0,1,0.5)
colorB = (1,0,1)
colorC = (0,0,1)



for frame in range(frames):
    newPage(w,h)
    divs = 1 + frame
    fill(colorA[0], colorA[1], colorA[2])
    frameDuration(.25)
    rect(0,0,w, h)
    
    for i in range(divs):
        # rotate(360/frames + i)
        t = i/divs
        fill( interpolate( colorA[0], colorB[0], t ), interpolate(colorA[1], colorB[1], t), interpolate(colorA[2], colorB[2], t), 1)
        rect(i*(w/divs),0,(w/divs*2)+1, h)
        for j in range(divs):
            rotate(-360/frames)
            t = j/divs
            blendMode("multiply")
            fill( interpolateB( colorC[0]/(j/divs+1), colorB[0], t ), interpolate(colorC[1]/(j/divs+1), colorB[1], t), interpolate(colorC[2]/(j/divs+1), colorB[2], t),.15)
            rect(0,j*(h/divs),w, (h/divs*2))
            blendMode("normal")
saveImage('../gifs/gradient-multiply-4.mov')
