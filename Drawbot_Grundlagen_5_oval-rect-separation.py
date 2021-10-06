for i in range(80):
    randomSize = randint(20,80)
    
    fill(None)
    stroke(0)
    strokeWidth(4)
    
    # zufällige Werte für x und y
    # Grösse von Seitengrösse abziehen, damit alle Elemente in der Fläche liegen
    xPos = randint(0, 1000-randomSize)
    yPos = randint(0, 1000-randomSize)
    
    # wenn y-Position grösser ist als die halbe Höhe, zeichne einen Kreis, sonst ein Quadrat
    if yPos > height()/2:
        oval(xPos, yPos, randomSize, randomSize)
    else:
        rect(xPos, yPos, randomSize, randomSize)

#saveImage("randomPosition.svg")       
        