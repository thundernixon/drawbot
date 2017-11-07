
def spokedCircle(x, y, radius, centerRadius, spokes, spokeWidth):
    save()
    translate(x, y)
    for spoke in range(spokes):
        # fill(0 + 1/spokes,0,0)
        fill(randint(750,900)*.001,randint(500,686)*.001,.25) #.68627451, .588235294 
        rect(0,centerRadius,spokeWidth,radius-centerRadius)
        rotate(360/spokes)
    restore()

W, H = 1000, 1000

frames = 50 # currently must be lower than number of maxSpokes
rotations = 2
totalSize = 1000
spokes = 65
maxSpokes = 75 # currently must be higher than number of frames
minSpokes = 20

distance = 0
maxDistance = 1000

starterRadius = 1450
starterCenterRadius = 50

radius = starterRadius
centerRadius = starterCenterRadius
    
incrementDistance = (maxDistance - distance)/frames
incrRadius = ((totalSize-starterRadius)/frames)*4.5
incrCenterRadius = ((totalSize-starterCenterRadius)/frames)*.25

for i in range(frames):
    newPage(W, H)

    if i < frames/2:
        # print "going up " + str(i*((maxDistance - distance)/frames))
        
        distance += incrementDistance
        radius -= incrRadius
        centerRadius += incrCenterRadius
        spokes += 3
        fill(0.1,0.1,0.1)
        print spokes
    else:
        # print "going down " + str(i*((maxDistance - distance)/frames))
        # distance -= i*((maxDistance - distance)/frames)
        distance -= incrementDistance
        radius += incrRadius
        centerRadius -= incrCenterRadius
        spokes -= 3
        print spokes
    fill(0.1,0.1,0.1)
    rect(0,0,1000,1000)
    # radius = totalSize - i*(totalSize/frames)
    # centerRadius = -totalSize + i*(totalSize/frames)*2
    # spokes = maxSpokes
    # spokes = minSpokes + i*int(((maxSpokes - minSpokes)/frames)) #increment up
    # spokes = maxSpokes - i*int(round(((maxSpokes - minSpokes)/frames)))
    # print spokes
    translate(500,500)
    # translate(500,500-centerRadius)
    rotate(0 + i*((360*rotations/frames)))

    # x, y, radius, centerRadius, spokes, spokeWidth
    spokedCircle(0, distance, radius, centerRadius, spokes, 1)
    spokedCircle(0, -distance, radius, centerRadius, spokes, 1)

    # translate(-500,-500+centerRadius)

saveImage("exports/moire_21-110717.gif")
