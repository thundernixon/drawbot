size(500,500)

frames = 50

width = 50

blue = 0
red = 0

for frame in range( frames ):
    blue += 0.01
    red += 0.015
    width += 1
    newPage()
    fill(red,0,blue)
    rect(100,100,width,100)

saveImage('test.gif')