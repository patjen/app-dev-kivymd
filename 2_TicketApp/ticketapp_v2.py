from kivymd.app import MDApp

class Film:
    def __init__(self, titel: str, ist_3d: bool, fsk: int):
        self.__titel = titel
        self.__ist_3d = ist_3d
        self.__fsk = fsk

    def get_titel(self):
        return self.__titel
    
    def ist_3d(self):
        return self.__ist_3d

    def get_fsk(self):
        return self.__fsk

class Ticket:
    __grundpreis = 7.60
    __aufpreis_3d = 3.00

    def __init__(self, film: Film):
        self.__film = film
        self.__anzahl = 0

    def preis_berechnen(self):
        preis = self.__grundpreis
        if self.__film.ist_3d() == True:
            preis = preis + self.__aufpreis_3d
        return preis
    
    def ticket_hinzufuegen(self):
        self.__anzahl += 1

    def ticket_entfernen(self):
        if self.__anzahl > 0:
            self.__anzahl -= 1
    
    def anzahl_tickets(self):
        return self.__anzahl



class TicketApp_v2(MDApp):

    film1 = Film("Wall-E", True, 6)
    film2 = Film("Per Anhalter durch die Galaxis", False, 12)

    ticket1 = Ticket(film1)
    ticket2 = Ticket(film2)
    
    def hinzufuegen(self, ticket: Ticket):
        ticket.ticket_hinzufuegen()
        self.aktualisieren()
    
    def entfernen(self, ticket: Ticket):
        ticket.ticket_entfernen()
        self.aktualisieren()

    def aktualisieren(self):
        self.root.ids.ticket1_anzahl.text = str(self.ticket1.anzahl_tickets()) + " x"
        self.root.ids.ticket2_anzahl.text = str(self.ticket2.anzahl_tickets()) + " x"
        
        gesamtpreis = self.ticket1.preis_berechnen() * self.ticket1.anzahl_tickets() + self.ticket2.preis_berechnen() * self.ticket2.anzahl_tickets()
        self.root.ids.label_preis.text = "Preis insgesamt: " + str(gesamtpreis) + " Euro"
        



TicketApp_v2().run()