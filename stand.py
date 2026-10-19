class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo_base = prezzo_base

        self.disponibile = True
        self.espositore = None

    def calcola_prezzo(self):
        return self.prezzo_base

    def __lt__(self, other):
        if not isinstance(other, Stand):
            return NotImplemented

        return self.calcola_prezzo() < other.calcola_prezzo()

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = (
                f"Assegnato a {self.espositore.nome} "
                f"{self.espositore.cognome}"
            )

        return (
            f"{self.codice} | "
            f"{self.superficie} mq - "
            f"Padiglione {self.padiglione} - "
            f"Prezzo {self.calcola_prezzo():.2f}€ - "
            f"{stato}"
        )


class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.numero_prese = numero_prese

    def calcola_prezzo(self):
        return self.prezzo_base * (1 + 0.07 * self.numero_prese)

    def __str__(self):
        return (
            f"{super().__str__()} - "
            f"Prese aggiuntive: {self.numero_prese}"
        )

class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.posizione = posizione

    def calcola_prezzo(self):
        return self.prezzo_base * 1.30

    def __str__(self):
        return (
            f"{super().__str__()} - "
            f"Posizione: {self.posizione}"
        )