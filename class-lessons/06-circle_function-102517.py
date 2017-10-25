# cx = 300
# cy =400
# d = 450
# r = d/2
# oval(cx-r, cy-r, d, d)


# cx = 550
# cy =710
# d = 190
# r = d/2
# oval(cx-r, cy-r, d, d)

def circle(cx, cy, r):
    print cx, cy, r
    d = r*2
    oval(cx-r, cy-r, d, d)
    
circle(300, 400, 140)
circle(600, 650, 70)