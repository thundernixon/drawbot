size(500,500);


# Variable([
#     dict(name="snowSize", ui="Slider",
#         args=dict(
#                 value=10,
#                 minValue=3,
#                 maxValue=25))
#     ], globals())

fill(0,0,.15);
rect(0,0,500,500);


# fill(1,1,1)
# rect(0,0,500,40)

def printMountains(x,y,w,h):
    rotate(45)
    fill(1,1,1)
    rect(x,y, w, h)
    rotate(-45)


def makeMountains():
    fill(1,1,1)
    rect(0,0,500,40)
    for m in range( 20 ):
        printMountains(m*20,m*-20, randint(40,150),randint(40,150));



snowSize = 10

def printSnow(x, y, alpha, rotation):
    fill(1,1,1,alpha);
    rotate(rotation*22.5)
    rect(x - snowSize/2, y - 1, snowSize, 2)
    rect(x - 1, y - snowSize/2, 2, snowSize)
    rotate(-rotation*22.5)
    # rect(x - snowSize/2, y - 1, snowSize, 2)
    # rect(x - 1, y - snowSize/2, 2, snowSize)



def makeItSnow():
    for i in range(300):
        printSnow(random()*500,random()*500, random(), random())

makeItSnow();
makeMountains();



frames = 20

for frame in range( frames ):
    newPage()
    fill(0,0,.15);
    rect(0,0,500,500);
    makeItSnow();
    makeMountains();
    


saveImage('mountains.gif')