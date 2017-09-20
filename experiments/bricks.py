height = 1000
width = 1000
rows = 20
cols = 10



def makeBackground():
    fill(0,0.1,.3)
    rect(0,0,width, height)

def brickRow(x, y):
    for col in range(cols):
        if randint(1,4) == 1:
            # print x, y
            g = randint(1,10)*.1
            b = randint(1,10)*.1
            fill(0,g,b)
        else:
            b = randint(1,3)*.05
            fill(0.025,0.025,b)
        rect(x, y, (width/cols), (height/rows))
        x += (width/cols)

def makeRows():
    for row in range(rows):
        brickRow(0, row*(height/rows))


frames = 15

# newPage(width,height) for each frame

# in each brick
# decide whether it has a color 
# if randint(1,4) == 1, color is true
# if color is true
#   show color 
#   move color up by height/frames/5
#### but how do you preserve state between multiple pages? with a list above?
#### yes. you could make a list of color on/off values (maybe with each one multiplied by hieght/frames/5?), then reference it. 

for frame in range(frames):
    newPage(width,height)
    makeBackground()
    makeRows()
    
# saveImage('bricks.gif')