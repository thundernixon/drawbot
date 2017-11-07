gridSize = 50

# class letterPath:
#     def letter_a_path():
#         path = BezierPath()
#         path.moveTo(100,100)
#         path.curveTo((100,200),(200,200),(200,100))
#         path.lineTo((400,400))
#         drawPath(path)
#     def missing_glyph_path():
#         path = BezierPath()
#         path.moveTo(100,100)
#         path.curveTo((100,200),(200,200),(200,100))
#         path.lineTo((400,400))
#         drawPath(path)


path_a = BezierPath()
path_a.moveTo((200, 650))
path_a.curveTo((100,200),(200,200),(200,100))
path_a.lineTo((400,400))

path_e = BezierPath()
path_e.moveTo((100, 650))
path_e.curveTo((100,200),(200,200),(200,100))
path_e.lineTo((400,400))

missing_glyph_path = BezierPath()
missing_glyph_path.moveTo((200, 650))
missing_glyph_path.curveTo((100,200),(200,200),(200,100))
missing_glyph_path.lineTo((400,400))


fontPathDictionary = {
    "a": path_a,
    # "e": letter_e_path,
    }

def drawLetterPaths(txt):
    for char in txt:
        print char
        path = fontPathDictionary.get(char, missing_glyph_path)
        drawPath(path)
        translate(7*gridSize,0)

drawLetterPaths("ae")