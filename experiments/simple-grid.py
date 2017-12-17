w = 1000
h = 1000
rows = 18
cols = 6 # make as many columns as rows, to make a grid

# fill(0,1,1)
# strokeWidth(2)
# stroke(0,0,0)

        
# We want to position dots in a grid, so we first need to make a loop to change the x position for each new dot — this will create multiple columns.
for currentCol in range(cols):
    dotWidth = w / (cols + (cols+1))
    # we want to move the x position *each time the loop runs*, and add some extra space between each  
    x = dotWidth + currentCol*(dotWidth+dotWidth)
    # We need a second loop to change the y position of dots, to make rows.
    for currentRow in range(rows):
        dotHeight = w / (rows + (rows+1))
        y = dotHeight + currentRow*(dotHeight+dotHeight)
        
        rect(x, y, dotWidth, dotHeight)    