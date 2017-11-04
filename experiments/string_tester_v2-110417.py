Variable([
    dict(name="customString", ui="TextEditor"),
    dict(name="matchXHeights", ui="CheckBox"),
    dict(name="fontSize1", ui="Slider",
            args=dict(
                value=100,
                minValue=75,
                maxValue=125)),
    dict(name="fontSize2", ui="Slider",
            args=dict(
                value=100,
                minValue=75,
                maxValue=125)),
    dict(name="fontSize3", ui="Slider",
            args=dict(
                value=100,
                minValue=75,
                maxValue=125)),
    dict(name="fontColor1", ui="ColorWell"),
    dict(name="fontColor2", ui="ColorWell"),
    dict(name="fontColor3", ui="ColorWell"),
    ], globals())

defaultFontColor1 = [.75,0,.75]

size('A3')

fontSize(100)
fallbackFont("Arial")

counter = 1


################# 😺 Trying Frederik's suggested method of targeting missing glyphs 😺 #################

import AppKit
import CoreText

from fontTools.ttLib import TTFont
from fontTools.misc.py23 import unichr

def fontPath(fontName):
    font = CoreText.CTFontDescriptorCreateWithNameAndSize(fontName, 10)
    if font:
        url = CoreText.CTFontDescriptorCopyAttribute(font, CoreText.kCTFontURLAttribute)
        if url:
            return url.path()
    else:
        # warn if font doest not exists
        pass
        
    return None

def listFontGlyphNames(fontName):
    path = fontPath(fontName)
    if path is None:
        return []      
    try:
        fontToolsFont = TTFont(path, lazy=True, fontNumber=0)
    except TTLibError:
        # warn if fontTools cannot read the file
        return []        
    characters = []
    glyphNames = fontToolsFont.getGlyphNames()
    fontToolsFont.close()
    if ".notdef" in glyphNames:
        glyphNames.remove(".notdef")
    return glyphNames



fontName = "bilak-typecooker Regular"
glyphNames = listFontGlyphNames(fontName)

print glyphNames

t = FormattedString(font=fontName)
t.appendGlyph(*glyphNames)

textBox(t, (0, 0, width(), height()))

# ? for glyph in glyphNames, check if char matches ANY glyph in the list, and set a value to true
# if value is false, make fill gray

def checkIfGlyphExists(char):
    for glyph in glyphNames:
        if char in glyphNames:
            glyphMatch = 1
        else:
            glyphMatch = 0
    if glyphMatch == 0:
        return fill(0.8,0,0)
    else:
        return fill(fontColor1)

################# 😺 TRIPLES LETTERS IN YOUR STRING, THEN SETS THEM AS TEXT 😺 #################
def testWeights(string, fontName1, fontName2, fontName3):
    counter = 1
    lineCount = 1
    textWidth = 0
    starterPosX = 50
    starterPosY = 120
    positionX = starterPosX
    positionY = height()-150
    newString = ""
    for char in string:
        newString += char*3
    
    for char in newString:
        if counter % 3 == 0:
            # checkIfGlyphExists(char)
            fill(fontColor3)
            fontSize(fontSize3)
            font(fontName3)

            if matchXHeights:
                fontSize(newFontSize3)

        elif (counter + 1) % 3 ==0:
            # checkIfGlyphExists(char)
            fill(fontColor2)
            fontSize(fontSize2)
            font(fontName2)

            if matchXHeights:
                fontSize(newFontSize2)

        else:
            # fill(fontColor1)
            checkIfGlyphExists(char)
            for glyph in glyphNames:
                if char in glyphNames:
                    glyphMatch = 1
                else:
                    glyphMatch = 0
            if glyphMatch == 0:
                fill(0.8,0.8,0.8)
            else:
                fill(fontColor1)
            fontSize(fontSize1)
            font(fontName1)
        
        text(char, (positionX, positionY))
        letterWidth, letterHeight = textSize(char)
        
        textWidth += letterWidth
        positionX += letterWidth
        
        if counter % 3 == 0:
            letterWidth, letterHeight = textSize(" ")
            positionX += letterWidth + 10
        
        if counter % 9 == 0:
            lineCount += 1
            positionX = starterPosX
            positionY -= starterPosY

        counter += 1
        
                
        
def calcNewSize(targetFontName, targetFontSize):
    # source font (font1)
    fontSize(fontSize1)
    font(fontName1)
    xHeight1 = fontXHeight()
    print fontXHeight()
    
    # target font
    fontSize(targetFontSize)
    font(targetFontName)
    xHeight2 = fontXHeight()

    return targetFontSize * (xHeight1 / xHeight2)

################# ✅ You can add custom fonts here ✅ #################
import string
alpha = string.lowercase

fontName1, fontName2, fontName3 = "bilak-typecooker Regular", "Verdana", "Times New Roman"

print "font size 1 is " + str(fontSize1) + " pt"

if matchXHeights:
    newFontSize2 = calcNewSize(fontName2, fontSize2)
    newFontSize3 = calcNewSize(fontName3, fontSize3)

    print "new font size 2 is %s pt" %newFontSize2
    print "new font size 3 is %s pt" %newFontSize3

else:
    print "font size 2 is " + str(fontSize2) + " pt"
    print "font size 3 is " + str(fontSize3) + " pt"

if customString != "":
    testWeights(customString, fontName1, fontName2, fontName3) # use your string as an argument
else:
    testWeights(alpha, fontName1, fontName2, fontName3)


#### to do: if letter doesn't exist in the supplied font, replace with "n" or some other user-defined string. possible method(?):
# if fontXheight is equal to fallback font x height (51.85546875 for Arial)
# make character light gray
# and maybe substitute with rectangle / asterisk / U+25A1 (white square) □


################# 😺 SAVE AS A PDF IF YOU'D LIKE TO PRINT 😺 #################
# saveImage("give-it-a-title.pdf")