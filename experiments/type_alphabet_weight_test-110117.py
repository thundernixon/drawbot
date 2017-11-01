import string

alpha = string.lowercase

# print alpha

font("Stroop")
fontSize(50)

counter = 1

def testWeights(string):
    counter = 1
    for char in string:
        print char
        # text(char, (50*counter, 100))
        text(char, (100, 100))
        letterWidth, letterHeight = textSize(char)
        translate(letterWidth,0)
        print letterWidth
        # print textSize(char)
        # counter += 1
        
        # if letter doesn't exist, replace with n

testWeights(alpha)