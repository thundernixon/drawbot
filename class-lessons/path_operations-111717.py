fill(0,.5)

bez1 = BezierPath()
bez1.oval(100,100,200,300)

bez2 = BezierPath()
bez2.rect(150,274,300,400)

drawPath(bez1)
drawPath(bez2)

# bez3 = bez1 & bez2 # intersection
# bez3 = bez1 | bez2 # union
# bez3 = bez1 ^ bez2 # "exclusive or"
bez3 = bez1 % bez2 # bez 1 minus bez 2
# bez3 = bez2 % bez1 # bez 2 minus bez 1

fill(1,0,0,0.5)

translate(10,10)
drawPath(bez3)