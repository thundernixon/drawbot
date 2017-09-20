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
    dict(name="letterWidth", ui="Slider",
        args=dict(
                value=300,
                minValue=10,
                maxValue=300)),
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
leftside = 100;

letterTop = letterHeight + baseline;
bowlHeight = letterHeight * bowlHeightRatio;

letterRight = letterWidth * 300 + leftside

print "letter height is ";
print letterHeight;
print "///";
print "bowl ratio is ";
print bowlHeightRatio;
print "///";
print "bowl height is ";
print bowlHeight;
print "///";

print "letter width is ";
print letterWidth;
print "///";
print "letter right is ";
print letterRight;
print "///";



lineCap("round")

a = (100,100)
b = (100,letterTop) # left
c = (leftside + (letterWidth * .65) ,letterTop) # 3/4 width
c2 = (leftside + (letterWidth * .9) ,letterTop) # 7/8 width
c3 = (leftside + letterWidth,(letterTop - bowlHeight / 4)) 
d = (leftside + letterWidth, (letterTop - bowlHeight / 2)) 
d2 = (leftside + letterWidth,(letterTop - bowlHeight * .75)) 
d3 = (leftside + (letterWidth * .9) ,(letterTop - bowlHeight)) # 7/8 width
e = (leftside + (letterWidth * .65) ,(letterTop - bowlHeight)) # 3/4 width
f = (100,(letterTop - bowlHeight)) # left
g = (leftside + letterWidth,100)
points = [a,b,c,c2,c3,d,d2,d3,e,f,g]


# print e;

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





