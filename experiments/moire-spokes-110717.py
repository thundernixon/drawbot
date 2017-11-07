
def spokedCircle(x, y, radius, centerRadius, spokes, spokeWidth):
    save()
    translate(x, y)
    for spoke in range(spokes):
        # fill(0 + 1/spokes,0,0)
        rect(0,centerRadius,spokeWidth,radius-centerRadius)
        rotate(360/spokes)
    restore()
    


distance = 240
    
radius = 928
centerRadius = 34
spokes = 44

translate(500,500-centerRadius)
rotate(356)

# x, y, radius, centerRadius, spokes, spokeWidth
spokedCircle(0, distance, radius, centerRadius, spokes, 1)
spokedCircle(0, -distance, radius, centerRadius, spokes, 1)

