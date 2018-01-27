W, H = 1440,960
frames = 100#100

message = "نوع وسائل الإعلام"

##########################

# message = message.upper()
messageLength = len(message)
for frame in range(frames):
    newPage(W,H)
    frameDuration(.2)
    fill(0)
    rect(0,0,W,H)
    print("frame " + str(frame))
    t = frame * 1/frames
    print t
    
    # translate(40,40)
    resolution = 30
    posX = t*W/resolution
    print posX
    
    print(messageLength)
    bez = BezierPath()
    bez.text(message, font="Cooper Arabic v0.0.17 Black", fontSize=resolution*0.5, offset=(-147+posX*messageLength / 9,5.55)) #offset=(20-posX,1)
    
    # get pixel dimensions to fit screen
    pixW, pixH = W/resolution*.75, W/resolution*.75
    
    # make grid and light up pixels that are inside letters
    for x in range(resolution):
        save()
        translate(pixW/2,pixH/2)
        for y in range(resolution): 
            if bez.pointInside((x,y)):                
                fill(.15,0,0,1)
                sizeFactor = 1.5
                oval((x*W/resolution)-(pixW*(1-sizeFactor/2)), (y*W/resolution)-(pixW*(1-sizeFactor/2)), pixW*sizeFactor, pixH*sizeFactor)
                fill(1,0,0)
                oval((x*W/resolution)+(pixW*.125), (y*W/resolution)+(pixW*.125), pixW*.75, pixH*.75)
            else:
                fill(1,0,0,.1)
                sizeFactor = .5
                oval((x*W/resolution)+(pixW*(1-sizeFactor)/2), (y*W/resolution)+(pixW*(1-sizeFactor)/2), pixW*sizeFactor, pixH*sizeFactor)
        restore()
        
saveImage("../exports/type_media-arabic.gif")