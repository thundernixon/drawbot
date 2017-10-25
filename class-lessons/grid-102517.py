pixelSize = 40
gridSize = 50

letter_a = """
- xxxx
----x
-xxxx
x---x
x--xx
-xx-x
"""

y = 800
x = 100

for row in letter_a.splitlines():
    x = 100
    for pix in row: 
        if pix == "x":
            # print "yes pixel"
            fill(0,0,1)
            rect(x,y, pixelSize,pixelSize)
        else:
            # print "no pixel"
            fill(1,1,.5)
            oval(x,y, pixelSize,pixelSize)
        x = x + gridSize
    y = y - gridSize   