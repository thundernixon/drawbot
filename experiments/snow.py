size(500,500);

# gradient for night sky
def makeSky():
    linearGradient((250,0),(250,500), ([0,0,.5], [0,0,.15]))

makeSky();
rect(0,0,500,500);

# function to make "mountain range"
def printMountains(x,y,w,h):
    rotate(45)
    translate(0,-20)
    fill(1,1,1)
    rect(x,y, w, h)
    rotate(-45)

# function to start mountain-making
def makeMountains():
    fill(1,1,1)
    rect(0,0,500,40)
    for m in range( 20 ):
        printMountains(m*20,m, randint(100,150),randint(100,150));

# function to make "Snow"
def printSnow(x, y, alpha, rotation, snowSize):
    fill(1,1,1,alpha);
    rotate(rotation*22.5)
    rect(x - snowSize/2, y - 1, snowSize, 2)
    rect(x - 1, y - snowSize/2, 2, snowSize)
    rotate(-rotation*22.5)

# function to start snow-making
def makeItSnow():
    for i in range(300):
        snowSize = randint(2,12);
        printSnow(random()*500,random()*500, random(), random(), snowSize)

# run starts snow-starting function
makeItSnow();

# run starts mountain-starting function
makeMountains();

# sets up number of frames for animation
frames = 20

# creates each frame, cueing snow and mountains
for frame in range( frames ):
    newPage()
    # fill(0,0,.15);
    makeSky();
    rect(0,0,500,500);
    makeItSnow();
    makeMountains(); # can I make a mountain range once, and repeat that in every frame, while still having random snowflakes? Something like defining a mountain range "object" once, then just printing the same one on each new frame...
    # print mountains;
    
# saves gif of animation
saveImage('mountains.gif')