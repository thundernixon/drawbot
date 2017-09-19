height = 1000
width = 1000
rows = 20
cols = 10

# for each row of height/20, 
# make 10 bricks, and
# add width/10 to the x-coordinate each time
# then move to next row

stroke(1,0,0)

def brickRow(x, y):
    for col in range(cols):
        rect(x, y, (width/cols), (height/rows))
        x += (width/cols)
        print x

# brickRow(0);

for row in range(rows):
    brickRow(0, row*(height/rows))
    
# each brick has a 1 in 6 chance of being a color
