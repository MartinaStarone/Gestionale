from dataclasses import dataclass,field
from VOCE import VOCE
from Enumerations import Tipo, Ricorrenza
@dataclass

class BilancioMensile:
    mese: int
    anno: int
    entrate: list[VOCE] = field(default_factory=list)
    uscite: list[VOCE] = field(default_factory=list)


    def add_entry(self, descrizione: str, tipo:Tipo,
    importo:float,
    ricorrenza:Ricorrenza)->VOCE:
        nuova_voce = VOCE( descrizione, tipo, float(importo), self.mese, ricorrenza)
        colonna = self.entrate if tipo == Tipo.ENTRATE else self.uscite
        for riga in colonna:
            if riga.descrizione.lower()==descrizione.lower():
                riga.importo = float(importo)
                riga.ricorrenza = ricorrenza
                return riga
        colonna.append(nuova_voce)
        return nuova_voce

    def remove_entry(self, descrizione:str, tipo: Tipo)->bool:
        colonna = self.entrate if tipo == Tipo.ENTRATE else self.uscite
        for riga in colonna:
            if riga.descrizione.lower()==descrizione.lower():
                colonna.remove(riga)
                return True
        return False


    def get_entry(self):
        return self.entrate
    def get_uscite(self):
        return self.uscite

    def get_colonna(self, tipo: Tipo, retrun=None)->list[VOCE]:
        var = self.entrate if tipo == Tipo.ENTRATE else self.uscite
        return var
  
    def get_totale(self, tipo: Tipo)->float:
        colonna = self.get_colonna(tipo)
        return sum(v.importo for v in colonna)
        