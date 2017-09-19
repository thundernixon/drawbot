height = 1000
width = 1000
rows = 20
cols = 10

fill(0,0.1,.3)
rect(0,0,width, height)

# for each row of height/20, 
# make 10 bricks, and
# add width/10 to the x-coordinate each time
# then move to next row

# stroke(1,0,0)

def brickRow(x, y):
    for col in range(cols):
        if randint(1,6) == 1:
            print x, y
            fill(0,1,0)
        else:
            fill(0,0.1,.3)
        rect(x, y, (width/cols), (height/rows))
        x += (width/cols)

for row in range(rows):
    brickRow(0, row*(height/rows))

for i in range(12):
    print randint(1,6)
    
# each brick has a 1 in 6 chance of being a color
