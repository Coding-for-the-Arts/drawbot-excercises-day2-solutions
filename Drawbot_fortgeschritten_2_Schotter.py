rectNumb = 7
rectSize = width()/rectNumb
fill(None)
stroke(0)

for row in range(rectNumb):
    
    # die y-Position für jede Zeile um die Rasterfeldgrösse erhöhen
    # 0*Rechteckgr. | 1*Rechteckgr. | 2*Rechteckgr. | 3*Rechteckgr. u.s.w.
    yPos = row * rectSize # rectSize entspricht der Rasterfeldgrösse
    
    for col in range(rectNumb):
        # x-Position für jedes Rechteck verschieben 
        xPos = col * rectSize
        
        # den Zustand der Arbeitsfläche speichern, also Standard, ohne Rotation
        with savedState(): 
            zufallswert = randint(-5,5) # zufälliger Rotationswert, im oder gegen den Uhrzeigersinn
            
            # die Arbeitsfläche um den zufälligen Wert rotieren, dieser wird nach unten grösser
            # Mittelpunkt der Rotation ist der Rasterzellenmittelpunkt (langes Wort … ;) )
            rotate(zufallswert * (rectNumb - row), (xPos + rectSize/2, yPos + rectSize/2))

            rect(xPos, yPos, rectSize, rectSize)
    
#saveImage("schotter.svg")