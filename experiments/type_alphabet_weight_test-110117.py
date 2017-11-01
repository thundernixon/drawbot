import string

size('A3')

w = 1000
h = 1000

# set canvas to a3 size

alpha = string.lowercase

# print alpha

font("Stroop")
fontSize(100)
fallbackFont("Input Mono")


counter = 1

#for each character in string, repeat three times in new string

# def generateNewString(string):
#     newString = ""
#     for char in string:
#         newString += char*3
#     return newString
        

def testWeights(string):
    counter = 1
    lineCount = 1
    textWidth = 0
    starterPosX = 50
    starterPosY = 100
    positionX = starterPosX
    positionY = height()-150
    # generateNewString(string)
    newString = ""
    for char in string:
        newString += char*3
    
    for char in newString:
        if counter % 3 == 0:
            # fill(1,0,0) # red
            font("Stroop Extrabold")
        elif (counter + 1) % 3 ==0:
            # fill(0,1,.5) # teal
            font("Stroop")
        else:
            # fill(0,0,1) # blue
            font("Stroop Sans Book")
        
        
        
        text(char, (positionX, positionY)) # to do: set this equal to something based on font size
        letterWidth, letterHeight = textSize(char)
        
        textWidth += letterWidth
        positionX += letterWidth
        
        if counter % 9 == 0: # to do: set this equal to something based on overall text width
            # translate(100-textWidth,-letterHeight)
            lineCount += 1
            positionX = starterPosX
            positionY -= starterPosY
            print lineCount
        # else:
            # translate(letterWidth,0)
        counter += 1
        
        # if letter doesn't exist, replace with n

testWeights(alpha)
# generateNewString(alpha)