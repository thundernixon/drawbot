A = 120

B = 870

M = (A + B) / 2

y = 500
dotSize = 15

f =    # this is our interpolation factor

# f == 0 -> M == A
# f == 1 -> M == B

M = A + f * (B - A)

# we start at `A`, then add the proportion of the distance between A and B
# if f == 0, then the distance is at A
# if f == 1, then the distance is at B
# then, if we start at A and add the distance between A and B, we end up at B

rect(A, y, dotSize, dotSize)
rect(B, y, dotSize, dotSize)
fill(1,0,0)
rect(M, y, dotSize, dotSize)