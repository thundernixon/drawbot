w = 1000
h = 1000
fill(.57, .08, 1, 0.25)
rect(0,0,1000,1000)
rows = 8
cols = rows # make as many columns as rows, to make a grid

fill(.57, .08, 1, 0.75)
strokeWidth(2)
stroke(0,0,0)

        
# We want to position dots in a grid, so we first need to make a loop to change the x position for each new dot — this will create multiple columns.
for currentCol in range(cols):
    dotSize = w / (cols + (cols+1))
    # we want to move the x position *each time the loop runs*, and add some extra space between each column
    x = dotSize + currentCol*(dotSize+dotSize)
    # We need a second loop to change the y position of dots, to make rows.
    for currentRow in range(rows):
        y = dotSize + currentRow*(dotSize+dotSize)
        
        rect(x, y, dotSize, dotSize)  

saveImage(u"~/Desktop/perfect-grid.png")