size(500,500);

fill(0,0,.15);
rect(0,0,500,500);

Variable([
    dict(name="snowSize", ui="Slider",
        args=dict(
                value=10,
                minValue=3,
                maxValue=25))
    ], globals())

# snowSize = 10

def printSnow(x, y, alpha):
    fill(1,1,1,alpha);
    rect(x - snowSize/2, y - 1, snowSize, 2)
    rect(x - 1, y - snowSize/2, 2, snowSize)

frames = 20

for frame in range( frames ):
    newPage()
    fill(0,0,.15);
    rect(0,0,500,500);
    for i in range(300):
        printSnow(random()*500,random()*500, random())




saveImage('snow.gif')