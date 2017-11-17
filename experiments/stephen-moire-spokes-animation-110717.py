
def spokedCircle(x, y, radius, centerRadius, spokes, spokeWidth, color):
    save()
    translate(x, y)
    for spoke in range(spokes):
        # fill(0 + 1/spokes,0,0)
        # fill(randint(750,900)*.001,randint(500,686)*.001,.25) #.68627451, .588235294 
        # fill(1,randint(450,900)*.001,randint(450,900)*.001)
        fill(randint(650,1000)*.001*color[0],randint(650,1000)*.001*color[1],randint(650,1000)*.001*color[2],)
        rect(0,centerRadius,spokeWidth,radius-centerRadius)
        rotate(360/spokes)
    restore()

W, H = 1000, 1000

frames = 60 # currently must be lower than number of maxSpokes
rotations = 1
totalSize = 1000

maxSpokes = 100 # currently must be higher than number of frames
minSpokes = 20
spokes = minSpokes
distance = 0
maxDistance = 1000

starterRadius = 1500
starterCenterRadius = -150

radius = starterRadius
centerRadius = starterCenterRadius
    
incrementDistance = (maxDistance - distance)/frames
incrRadius = ((totalSize-starterRadius)/frames)*-11
incrCenterRadius = ((totalSize-starterCenterRadius)/frames)*.55

incrSpokes = int(ceil((maxSpokes - minSpokes)/frames))

for i in range(frames):
    newPage(W, H)
    fill(.1,.1,1)
    if i < frames/2:
        # print "going up " + str(i*((maxDistance - distance)/frames))
        
        distance += incrementDistance
        radius -= incrRadius
        centerRadius += incrCenterRadius
        spokes += incrSpokes
        # fill(0.1,0.1,0.1)
        
        print spokes
    else:
        # print "going down " + str(i*((maxDistance - distance)/frames))
        # distance -= i*((maxDistance - distance)/frames)
        distance -= incrementDistance
        radius += incrRadius
        centerRadius -= incrCenterRadius
        spokes -= incrSpokes
        print spokes
    # fill(0.1,0.1,0.1)
    fill(0,0,.1)
    rect(0,0,1000,1000)
    # radius = totalSize - i*(totalSize/frames)
    # centerRadius = -totalSize + i*(totalSize/frames)*2
    # spokes = maxSpokes
    # spokes = minSpokes + i*int(((maxSpokes - minSpokes)/frames)) #increment up
    # spokes = maxSpokes - i*int(round(((maxSpokes - minSpokes)/frames)))
    # print spokes
    translate(500,500)
    # translate(500,500-centerRadius)
    rotate(0 - i*((360*rotations/frames)))

    # x, y, radius, centerRadius, spokes, spokeWidth
    spokedCircle(0, distance, radius, -centerRadius, spokes, 1, (.6,.4,1))
    spokedCircle(0, -distance, radius, centerRadius, spokes, 1, (1,.8,0))
    
    # rotate(0 + i*2*((360*rotations/frames)))
    # spokedCircle(0, distance/2, radius*2, -centerRadius*2, spokes, 1, (1,1,1))
    # spokedCircle(0, -distance/2, radius*2, -centerRadius*2, spokes, 1, (1,1,1))

    # translate(-500,-500+centerRadius)

saveImage("exports/moire_31-110717.gif")
