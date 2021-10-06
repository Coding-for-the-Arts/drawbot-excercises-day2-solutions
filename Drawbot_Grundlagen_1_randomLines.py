anzahlLinien = 30

for i in range(anzahlLinien):
    lineCap("round")
    strokeWidth(randint(1,50)) # zufällige Strichstärke zwischen 1 und 50
    stroke(0)
    # Linien von der Mitte an einen zufälligen Endpunkt zwischen 50 und 950
    line((500, 500), (randint(50,950), (randint(50,950) )) )

