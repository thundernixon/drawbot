W = H = 700

w = h = 100

def tree(n):
   rect(0, 0, w, h)

   if n > 0:
       save()
       translate(0, h)
       rotate(45)
       scale(sqrt(2)/2)
       tree(n-1)
       restore()

       save()
       translate(w, h)
       rotate(-45)
       scale(sqrt(2)/2)
       translate(-w, 0)
       tree(n-1)
       restore()

print (sqrt(2))

levels = 3

size(W, H)
translate(W/2 - w/2, 100)
tree(levels)