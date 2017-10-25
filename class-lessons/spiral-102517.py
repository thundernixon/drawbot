save() #save the current coordinate system

translate(500,500)

fill(0,1,1)
for i in range(200):
    rect(270,0,200,10)
    rotate(1-(-1008*.01))     
    scale(1-(1*.01))
    fill(0+(.01*i),1-(.01*i),1-(.01*i))

restore() # restore the saved coordinate system