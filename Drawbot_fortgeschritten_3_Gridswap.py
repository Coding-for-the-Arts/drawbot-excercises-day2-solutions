colNumb = 4
colSize = width()/colNumb
ovalSize = colSize
posX, posY = 0, 0

for row in range(colNumb):
    posX = 0
    for col in range(colNumb):
        # wenn col geteilt durch 2 aufgeht, also keinen Rest ergibt und row auch …
        if col%2 == 0 and row%2 == 0:
            # … zeichne einen schwarzen Kreis 
            fill(0)
            oval(posX, posY, ovalSize, ovalSize)
            
        # … oder wenn col und row nicht durch 2 teilbar sind, also Rest 1 geben:
        elif col%2 and row%2 == 1:
            # … zeichne einen schwarzen Kreis
             oval(posX, posY, ovalSize, ovalSize)

        # andernfalls, also wenn beides nicht zutrifft:
        else:
        
        # zeichne ein schwarzes Quadrat
            rect(posX, posY, ovalSize, ovalSize)
        # und einen weissen Kreis und setze die Füllfarbe wieder auf Schwarz
            fill(1)
            oval(posX, posY, ovalSize, ovalSize)
            fill(0)
        print(col%2)
        
        posX += colSize
    posY += colSize
    
#saveImage("Raster-abwechselnd.svg")