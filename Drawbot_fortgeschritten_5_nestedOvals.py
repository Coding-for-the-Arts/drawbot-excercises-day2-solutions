cellNumb = 4
cellSize = width()/cellNumb
fill(None)
stroke(0)
strokeWidth(7)

# eine Funktion, in welcher 4 Kreise gezeichnet werden
def drawFourOvals():
    oSize = cellSize
    for o in range(4):
        with savedState():
            offset = 10 # das ist ein trial- and error-Wert, hängt von div. Faktoren ab 
            translate(offset*o, offset*o) # Kreise immer mehr verschieben
            oval(0,0,oSize, oSize)   
            oSize -= 50 
        
def rotateNeg90():
    rotate(-90, (cellSize/2, cellSize/2))
    
def rotate90():
    rotate(90, (cellSize/2, cellSize/2))
    
def rotate180():
    rotate(180, (cellSize/2, cellSize/2))

for row in range(cellNumb):
    for col in range(cellNumb):
        with savedState():
            translate(col * cellSize, row * cellSize)
            # je nach Zufallswert wird die Arbeitsfläche um 90°, -90° oder 180° oder nicht rotiert
            if random()<0.25:
                rotateNeg90()    
            elif random()<.5:        
                rotate180()
            elif random()<.75:        
                rotate90()
            drawFourOvals()
    
#saveImage("nested-ovals.svg")