cellNumb = 4 # Anzahl Rasterzellen
cellSize = width()/cellNumb # Berechnung der Zellengrösse

posY = 0

for row in range(cellNumb):
    posX = 0 # x-Position auf 0 zurücksetzen
    
    for col in range(cellNumb):
        # Zufallswert für die Kreisgrösse, mindestens 10, maximal Grösse der Rasterzelle
        ovalSize = randint(10, cellSize) 
        
        # Versatz berechnen, um den Kreises einzumitten (Mitte der Zellengrösse - Radius)
        centerPos = cellSize/2-ovalSize/2 
        
        # ein Kreis an die x- und y-Position im Raster + Versatz
        oval(posX + centerPos, posY + centerPos, ovalSize, ovalSize)
        
        posX += cellSize
    posY += cellSize
    
#saveImage("dots-in-grid.svg")