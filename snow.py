size(500,500);


# Variable([
#     dict(name="snowSize", ui="Slider",
#         args=dict(
#                 value=10,
#                 minValue=3,
#                 maxValue=25))
#     ], globals())

# fill(0,0,.15);
def makeSky():
    linearGradient((250,0),(250,500), ([0,0,.5], [0,0,.15]))

makeSky();
rect(0,0,500,500);


# fill(1,1,1)
# rect(0,0,500,40)

def printMountains(x,y,w,h):
    rotate(45)
    translate(0,-20)
    fill(1,1,1)
    rect(x,y, w, h)
    rotate(-45)


def makeMountains():
    fill(1,1,1)
    rect(0,0,500,40)
    for m in range( 20 ):
        printMountains(m*20,m, randint(100,150),randint(100,150));



snowSize = 10

def printSnow(x, y, alpha, rotation, snowSize):
    fill(1,1,1,alpha);
    rotate(rotation*22.5)
    rect(x - snowSize/2, y - 1, snowSize, 2)
    rect(x - 1, y - snowSize/2, 2, snowSize)
    rotate(-rotation*22.5)



def makeItSnow():
    for i in range(300):
        snowSize = randint(2,12);
        printSnow(random()*500,random()*500, random(), random(), snowSize)

makeItSnow();

makeMountains();
# mountains = makeMountains();



frames = 20

for frame in range( frames ):
    newPage()
    # fill(0,0,.15);
    makeSky();
    rect(0,0,500,500);
    makeItSnow();
    makeMountains(); # can I make a mountain range once, and repeat that in every frame, while still having random snowflakes? Something like defining a mountain range "object" once, then just printing the same one on each new frame...
    # print mountains;
    


saveImage('mountains.gif')