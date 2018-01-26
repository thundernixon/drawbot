# yo

size(2700,1800)
image("2017-12-09 10.27.17-HDR.jpg", (0,0))

im = ImageObject(path="2017-12-09 10.27.17-HDR.jpg")

with im:
    # size(1600,1600) ## why can't I control the size of this?
    fill(0,0,0,0)
    rect(0, 0, width(), height())

imgNum = 50
imgDist = 20
x = 69
y = 84
translate(width()/2,height()/2)
scale(1.35)

for i in range(imgNum):
    # translate(imgDist,imgDist)
    # x = width()/imgNum
    # y = height()/imgNum
    save()
    # translate(x*i*2,y*i)
    rotate(i*(360/imgNum))
    image(im, (100, 100))
    
    
    restore()
    
saveImage("psychedelic-skyline.jpg")