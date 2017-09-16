size(500,500)

stroke(1,0,0)

Variable([
    dict(name="letterHeight", ui="Slider",
        args=dict(
                value=300,
                minValue=25,
                maxValue=300)),
    dict(name="bowlHeightRatio", ui="Slider",
        args=dict(
                value=0.5,
                minValue=0.15,
                maxValue=0.95)),
    # create a variable called 'useColor'
    # and the related ui is a CheckBox.
    dict(name="useColor", ui="CheckBox"),
    # create a variable called 'c'
    # and the related ui is a ColorWell.
    dict(name="c", ui="ColorWell")
    ], globals())

# check if the 'useColor' variable is checked
if useColor:
    # set the fill color from the variables
    stroke(c)

baseline = 100;

letterTop = letterHeight + baseline;
bowlHeight = letterHeight * bowlHeightRatio;

print "letter height is ";
print letterHeight;
print "bowl ratio is ";
print bowlHeightRatio;
print "bowl height is ";
print bowlHeight;

lineCap("round")

a = (100,100)
b = (100,letterTop)
c = (275,letterTop)
c2 = (360,letterTop) # top
c3 = (400,(letterTop - bowlHeight / 4)) # 1/4 of way to of bowl
d = (400,(letterTop - bowlHeight / 2)) # halfway to bottom of bowl
d2 = (400,(letterTop - bowlHeight * .75)) # 3/4 of way to bottom of bowl 
d3 = (360,(letterTop - bowlHeight)) # bottom of bowl
e = (275,(letterTop - bowlHeight)) # bottom of bowl
f = (100,(letterTop - bowlHeight)) # bottom of bowl
g = (400,100)
points = [a,b,c,c2,c3,d,d2,d3,e,f,g]


print c2;

fill(None)

strokeWidth(3)


path = BezierPath()
path.moveTo(a)
path.lineTo(b)
path.lineTo(c)

path.curveTo(c2,c3,d)
path.curveTo(d2,d3,e)
path.lineTo(f)
path.lineTo(e)
path.lineTo(g)

drawPath(path)


# show handle "controls"


# fill(None)
# stroke(0,1,0)
# strokeWidth(2)

# for point in points:
#     printPoint(point[0],point[1])


#####################




