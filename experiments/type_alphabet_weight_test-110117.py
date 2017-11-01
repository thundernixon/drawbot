import string

w = 1000
h = 1000

alpha = string.lowercase

# print alpha

font("Stroop")
fontSize(50)
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
    # generateNewString(string)
    newString = ""
    for char in string:
        newString += char*3
    
    for char in newString:
        print char
        # text(char, (50*counter, 100))
        if counter % 3 == 0:
            fill(1,0,0) # red
            font("Times New Roman Bold")
        elif (counter + 1) % 3 ==0:
            fill(0,1,.5) # teal
            font("Times New Roman")
        else:
            fill(0,0,1) # blue
            font("Times New Roman Italic")
        
        
        
        text(char, (100, 800))
        letterWidth, letterHeight = textSize(char)
        translate(letterWidth,0)
        print letterWidth
        # print textSize(char)
        counter += 1
        
        # if letter doesn't exist, replace with n

testWeights(alpha)
# generateNewString(alpha)