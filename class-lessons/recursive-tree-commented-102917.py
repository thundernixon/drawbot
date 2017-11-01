def tree(n, rotation):
    rect(0,0,w,h)
    if n > 0:
        save()
        translate(0,h)
        rotate(rotation)
        scale(sqrt(2)/2)
        tree(n-1)
        restore()
        
        save()
        translate(w, h)
        rotate(-rotation)
        scale(sqrt(2)/2)
        translate(-w,0)
        tree(n-1)
        restore()
        
W= H = 700
w = h = 100 #dimensions of the square

levels = 5 # sets number of levels in tree

size(W,H) # sets canvas to W and H that are defined
translate(W/2 - w/2, 100) # puts squares in the middle of canvas
tree(levels) # cues function with argument of how many levels to draw