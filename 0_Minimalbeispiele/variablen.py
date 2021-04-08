# Alles hinter einem "#" ist ein Kommentar, und wird vom Computer nicht beachtet

# Zuweisung: = 
# [Name der Variable] = [Wert]
mein_string = "Hallo"   # Der Name der Variable ist mein_string und sein Wert "Hallo".
name = "Patrick"        # Der Name der Variable ist name und sein Wert "Patrick".


### Strings (str): eine Aneinanderreihung von Zeichen
# sind umgeben von "" oder ''


# Konkatenation mit + (bei Strings)
# [string] + [string]
mein_string = "Hallo" + " Welt!"    # neuer Wert: "Hallo Welt".
anrede = mein_string + " " + name   # Wert: ???

# Typumwandlung zu String (Casting)
zahl = 42
zahl_als_string = str(zahl) # Wert: "42"


### Integer (int): Ganze Zahlen
### Floating Point (float): Dezimalzahlen . statt ,
zahl = 42
pi = 3.14

# einfache Rechenoperationen:
# + - * /
ergebnis = zahl * 2     # Wert: 84 (42*2)

zahl = zahl + 18        # neuer Wert: 60
#Abkürzung:
zahl += 18              # addiert auf den Wert von zahl 18 dazu, auch: -= *= /=


### Boolean (bool): Wahrheitswert
# entweder True (wahr) oder False (falsch)
die_wahrheit = True

# Vergleichsoperatoren
# <  (kleiner) 
# >  (größer) 
# == (gleich)
# <= (kleiner-gleich)
# >= (größer gleich)
# != (ungleich) 
die_wahrheit = 0 < 5        # Wert: True, weil 0 kleiner 5
die_wahrheit = 7.5 == 9.1   # Wert: False, da 7,5 und 9,1 nicht gleich sind

#logische Verknüpfungen 
# x and y (True, wenn x und y True)
# x or y  (True, wenn x oder y True)
# not x   (True, wenn x False)
die_wahrheit = 0 < 5 and 4 != 7 # True da sowohl 0 kleiner 5 als auch 4 ungleich 7 wahr ist