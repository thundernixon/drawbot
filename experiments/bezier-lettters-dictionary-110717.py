gridSize = 50

def path_a():
    letterWidth = 324
    path = BezierPath()
    path.moveTo((284, 410))
    path.curveTo((42, 324),(102, 140),(204, 140))
    path.curveTo((298, 140),(316, 250),(308, 426))
    path.lineTo((280, 144))
    path.lineTo((318, 194))
    return path, letterWidth
    
def path_c():
    letterWidth = 226
    path = BezierPath()
    path.moveTo((194, 324))
    path.curveTo((230, 341),(250, 430),(146, 430))
    path.curveTo((22, 430),(-22, 148),(130, 148))
    path.curveTo((240, 148),(190, 254),(194, 250))
    return path, letterWidth

def path_e():
    letterWidth = 192
    path = BezierPath()
    path.moveTo((42, 276))
    path.curveTo((216, 259),(250, 430),(146, 430))
    path.curveTo((22, 430),(-22, 148),(130, 148))
    path.curveTo((240, 148),(190, 254),(142, 204))
    return path, letterWidth

def missing_glyph():
    letterWidth = 192
    path = BezierPath()
    path.moveTo((66, 424))
    path.lineTo((66, 156))
    path.lineTo((166, 156))
    path.lineTo((166, 422))
    path.closePath()
    return path, letterWidth
    
fill(1,1,1)
stroke(1,0,0)
strokeWidth(10)
lineCap("round")
lineJoin("round")

fontPathDictionary = {
    "a": path_a(),
    "c": path_c(),
    "e": path_e(),
    }

def drawLetterPaths(txt):
    for char in txt:
        print char
        path = fontPathDictionary.get(char, missing_glyph())
        drawPath(path[0])
        translate(path[1],0)

drawLetterPaths("aced")