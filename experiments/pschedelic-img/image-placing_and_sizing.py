size(2700,1800) # size canvas

path="2017-12-09 10.27.17-HDR.jpg" # set up path variable

bez = BezierPath() # set up bezier object
bez.oval(500, 500, 1200, 1200) # make your bezier
# bez.rect(100, 100, 200, 200) # you could also do a rectangle or whatever you want

with savedState(): # only use the clipping path for the image, not anything that comes later
    clipPath(bez) #use the clipping path
    translate(-300, 100) # position the image
    # scale(0.1) # scale the image
    image(path, (0, 0)) # insert the image


rect(0, 0, 100, 100) # do other stuff
