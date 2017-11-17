def path_k():
    letterWidth = 200
    def shapes():
        polygon((90, 296), (120, 330), (152, 216), (120, 180), close=True)
        polygon((138, 370), (120, 330), (194, 342), (214, 382), close=True)
        polygon((70, 188), (50, 150), (144, 138), (168, 178), close=True)
        polygon((174, 282), (144, 250), (230, 174), (262, 202), close=True)
        polygon((296, 140), (310, 178), (230, 174), (214, 138), close=True)
        polygon((174, 282), (188, 318), (292, 316), (266, 280), close=True)
    return shapes(), letterWidth

# def path_a():
#     letterWidth = 192
#     def shapes():
#         polygon((150, 326), (190, 358), (160, 208), (120, 180), close=True)
#         polygon((98, 186), (68, 152), (144, 138), (168, 178), close=True)
#         polygon((274, 356), (190, 358), (210, 396), (296, 394), close=True)
#         polygon((274, 356), (298, 208), (260, 180), (240, 316), close=True)
#         polygon((324, 132), (252, 136), (260, 180), (336, 178), close=True)
#         polygon((166, 246), (196, 282), (248, 264), (224, 228), close=True)
#     return shapes(), letterWidth
    
def missing_glyph():
    letterWidth = 192
    path = BezierPath()
    path.moveTo((66, 424))
    path.lineTo((66, 156))
    path.lineTo((166, 156))
    path.lineTo((166, 422))
    path.closePath()
    return path, letterWidth
    
fontPathDictionary = {
    # "a": path_a(),
    "k": path_k(),
    }
    
# def drawLetterPaths(txt):
#     for char in txt:
#         print char
#         path = fontPathDictionary.get(char) # missing_glyph())
#         # drawPath(path[0])
#         print path[1]
        
#         print path[0]
#         print translate(path[1],0)
        
# drawLetterPaths("akak")
# print path_k()[1]