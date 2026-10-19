from stand import Stand, StandPreseExtra, StandPremium

class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.stand = None

    def __str__(self):
        if self.stand is None:
            stato = "Nessuno stand assegnato"
        else:
            stato = f"Stand assegnato: {self.stand.codice}"

        return f"{self.codice}: {self.nome} {self.cognome} - {stato}"



class LingottoFiere:
    def __init__(self, nome):
        self.nome = nome
        self.stand = {}
        self.espositori = {}
    """Aggiungere setter e getter se necessari"""

    def __str__(self):
        return (
            f"{self.nome} - "
            f"Stand: {len(self.stand)} - "
            f"Espositori: {len(self.espositori)}"
        )

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path, "r", encoding="utf-8-sig") as file:
            for riga in file:
                riga = riga.strip()

                if not riga:
                    continue

                campi = riga.split(",")
                codice = campi[0]
                if codice.startswith("ES"):
                    nome = campi[1]
                    cognome = campi[2]

                    espositore = Espositore(codice, nome, cognome)
                    self.espositori[codice] = espositore

                elif codice.startswith("ST"):
                    superficie = float(campi[1])
                    padiglione = int(campi[2])
                    prezzo_base = float(campi[3])

                    if len(campi) == 4:
                        stand = Stand(
                            codice, superficie, padiglione, prezzo_base
                        )

                    else:
                        caratteristica = campi[4].strip()

                        if caratteristica.isdigit():
                            numero_prese = int(caratteristica)

                            stand = StandPreseExtra(
                                codice, superficie, padiglione,
                                prezzo_base, numero_prese
                            )

                        else:
                            posizione = caratteristica

                            stand = StandPremium(
                                codice, superficie, padiglione,
                                prezzo_base, posizione
                            )

                    self.stand[codice] = stand

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self.stand:
            raise ValueError("Lo stand indicato non esiste.")

        if codice_espositore not in self.espositori:
            raise ValueError("L'espositore indicato non esiste.")

        stand = self.stand[codice_stand]
        espositore = self.espositori[codice_espositore]
        if not stand.disponibile:
            raise ValueError("Lo stand è già occupato.")

        if espositore.stand is not None:
            raise ValueError("L'espositore ha già uno stand assegnato.")

        stand.disponibile = False
        stand.espositore = espositore
        espositore.stand = stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        if not self.espositori:
            print("Non sono presenti espositori.")
            return

        for espositore in self.espositori.values():
            print(espositore)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.stand.values())
