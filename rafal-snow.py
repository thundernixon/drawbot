import random

frames = 40
listOfW = [random.randrange(100,150,1) for _ in range (frames+1)]
listOfH = [random.randrange(100,150,1) for _ in range (frames+1)]

# gradient for night sky
def background():
    linearGradient((250,0),(250,500), ([0,0,.5], [0,0,.15]))
    rect(0,0,500,500)
    
# function to make "Snow"
def printSnow(x, y, alpha, rotation, snowSize):
    fill(1,1,1,alpha);
    rotate(rotation*22.5)
    rect(x - snowSize/2, y - 1, snowSize, 2)
    rect(x - 1, y - snowSize/2, 2, snowSize)
    rotate(-rotation*22.5)

def makeItSnow():  
    for i in range(300):
        snowSize = randint(2,12);
        printSnow(random.random()*500,random.random()*500, random.random(), random.random(), snowSize)

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
        printMountains(m*20,m, listOfW[m],listOfH[m]);

# main printing loop
for frame in range(frames):
    newPage(500,500)
    background()
    makeItSnow()
    makeMountains()


# saves gif of animation
# saveImage('mountains.gif')
    

    