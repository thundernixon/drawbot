size(500,500)

frames = 50

width = 50

for frame in range( frames ):
    width += 2
    newPage()
    rect(100,100,width,100)

saveImage('test.gif')