yPos = 0
rectNumb = 5
rectSize = width()/rectNumb

for row in range(rectNumb): # für jede Zeile …
    xPos = 0
    
    for column in range(rectNumb): # für jede Spalte …
        with savedState():
            stroke(1)
            strokeWidth(5)
            
            """ rotieren um: Iterationsvariable column +1, damit nicht bei 0 begonnen wird, * 25 Grad * Iterationsvariable row +1, damit auch für die Zeilen nicht bei 0 begonnen wird.
            Damit erhält jedes Rasterfeld einen anderen Rotationswert"""
            rotate((column+1)*25*(row+1), (xPos+rectSize/2, yPos+rectSize/2))
            print((column+1)*25*(row+1))
            
            rect(xPos, yPos, rectSize, rectSize)
    
            xPos += rectSize
    yPos += rectSize
    
#saveImage("rotating-squares.svg")