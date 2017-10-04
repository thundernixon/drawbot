# lineCap("round")
# lineJoin("round")

# lineDash(randint(1, 20), randint(1, 20),randint(1, 20),randint(1, 20),randint(1, 20),randint(1, 20),randint(1, 20))

fill(None)
stroke(0,.5,1)
strokeWidth(20)

for i in range(2):
    line((840, 562), (516, 836))
    rect(156, 164,218, 310)
    polygon(
        (658, 488),
        (302, 612),
        (154, 732),
        (474, 738),
        (482, 410),
        close=False,
    )
    strokeWidth(2)
    stroke(0)