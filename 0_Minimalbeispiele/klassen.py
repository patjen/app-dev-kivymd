### Klassen

class Haustier:
    __anzahl = 0    # Klassenvariable, gilt für die gesamte Klasse
                    
    ###Konstruktor: Besondere Methode, die Aufgerufen wird, wenn ein neues Objekt instanziiert wird
    # Alle Variablen die hier definiert werden, sind Objekt/Instanzvariablen und können für jedes Objekt unterschiedlich sein
    def __init__(self, name: str, tierart: str, alter: int) # Diese Parameter müssen beim initiieren einer Instanz angegeben werden!
        self.name = name            
        self.__tierart = tierart    # Variablen mit zwei Unterstrichen am Anfang sind nur in der Klasse und für Instanzen
        self.__alter = alter        # sichtbar und nur diese können auf diese zugreifen oder ändern

        Haustier.__anzahl += 1     # Ein Konstruktor kann auch mehr machen als nur die Objektvariablen setzen

    # So kann außerhalb der Klasse auf ein geschützes Attribut zugegriffen werden
    def gib_tierart(self):
        #mit dem Schlüsselwort reutrn wird ein Wert zurückgegeben
        return __tierart


### Instanziierung von Objekten mit den Parametern, die der Konstruktor der Klasse benötigt
mein_haustier = Haustier("Bello", "Hund", 3)

#So werden ungeschütze Attribute aufgerufen:
print(mein_haustier.name)

# print(mein_haustier.__tierart) !!! Das geht nicht, weil dieses Attribut geschützt ist !!!

# So werden Methoden aufgerufen:
print(mein_haustier.gib_tierart())



