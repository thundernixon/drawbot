canvas = 1000
center = canvas/2

scaleFactor = 5

moveFactor = 1/(scaleFactor/2) # this needs some kind of logarhtmic solution

scale(scaleFactor)
translate(-canvas*(moveFactor), -canvas*(moveFactor))

w, h = 100,100

rect(center-w/2,center-h/2, w, h)