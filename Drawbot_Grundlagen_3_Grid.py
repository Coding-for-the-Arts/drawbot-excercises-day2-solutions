colNumbWidth = 5 # Anzahl Spalten
colWidth = width()/colNumbWidth # Berechnung der Spaltenbreite

colNumbHeight = 3 # Anzahl Zeilen
colHeight = height()/colNumbHeight # Berechnung der Zeilenhöhe

posY = 0
posX = 0

for row in range(colNumbHeight):
    posX = 0
    for col in range(colNumbWidth):
        fill(random())
        rect(posX, posY, colWidth, colHeight)
        posX += colWidth # Verschiebung der x-Position
    posY += colHeight # Verschiebung der y-Position
    
#saveImage("Raster-1.svg")