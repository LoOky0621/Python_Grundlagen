#Kopfrechnen Spiel Teil13
#While Schleife mit Fehler Abfrage

import random

#Zufallsgenerator initialisieren
random.seed()               #Die Funktion seed() führt dazu, dass der Zufallsgenerator mit der aktuellen Systemzeit
                            #Initialisiert wird, Andernfalls könnte es passieren, das anstelle einer zufälligen Auswahl 
                            #Immer wieder die gleiche Zahlen geliefert wird.

#Zufallswete und Berechnung

a = random.randint(1, 10)   #variable a wird eine zufällige Zahl zugewiesen
b = random.randint(1, 10)   #variable b wird eine zufällige Zahl zugewiesen
                            #Die Funktion randint() des Moduls random liefert eine ganze Zufallszahl im
                            #Eingabebereich von 1 bis 10
#Berechnung

c = a + b                   #Formel zu berechung von Addition
print("Die Aufgabe:", a, "+", b)    #Zeigt die Aufgabe an

zahl = c + 1
versuch = 0

#Eingabe
while zahl != c:

    versuch = versuch + 1

    print("Bitte geben sie Ihr Ergebniss ein:")
    z = input()

    try:
        zahl = int(z)

    except:
        print("Sie haben keine Zahl eingegeben")
        continue    

    if c==z:

        print(z, "ist richitg!")

    else:
        
        print(z, "ist falsch")           #Zeigt das Ergebinis an

print("Ergebni: ", c)
print("Anzahl Versuche: ", versuch)        