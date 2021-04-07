from kivymd.app import MDApp

class Ticket:
    __grundpreis = 7.60

    def __init__(self, titel: str):
        self.__titel = titel
        self.__anzahl = 0

    def preis_berechnen(self):
        return self.__grundpreis
    
    def ticket_hinzufuegen(self):
        self.__anzahl += 1

    def ticket_entfernen(self):
        if self.__anzahl > 0:
            self.__anzahl -= 1
    
    def anzahl_tickets(self):
        return self.__anzahl
    
    def film_titel(self):
        return self.__titel


class TicketApp(MDApp):

    ticket1 = Ticket("Wall-E")
    ticket2 = Ticket("Per Anhalter durch die Galaxis")
    
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
        



TicketApp().run()