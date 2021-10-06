colNumb = 4
colSize = width()/colNumb

posX = 0
posY = 0
gap = 40 # Spalten- und Zeilenabstand
ovalSize = colSize-gap # Kreisgrösse ist Zellengrösse minus Abstand

fill(None)
stroke(0)
strokeWidth(16)

for row in range(colNumb):
    posX = 0
    for col in range(colNumb):
        
        # wenn random grösser ist als 0.5, zeichne einen Kreis …
        if random() > 0.5: 
            oval(posX + gap/2, posY + gap/2, ovalSize, ovalSize)
            
        # … und sonst ein Rechteck
        else:
            rect(posX + gap/2, posY + gap/2, ovalSize, ovalSize)
            
        posX += colSize
    posY += colSize
    
    
#saveImage("rect-or-oval.svg")