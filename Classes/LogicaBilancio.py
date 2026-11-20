from Enumerations import Tipo
from BilancioMensile import BilancioMensile
class LogicaBilancio:
    def __init__(self):
        righe = int
        colonne = int
        bilanciomensile = BilancioMensile()

    def get_totale_entrate(self)->float:
            totale = BilancioMensile.get_totale(self.bilanciomensile, Tipo.ENTRATE)
            return totale


    def get_totale_uscite(self)->float:

        totale = BilancioMensile.get_totale(BilancioMensile(), Tipo.USCITE)
        return totale

    def get_saldo(self,entrate:int, uscite:int)->float:
        saldo = entrate - uscite
        return saldo

    def percentuale(self, entrate:int, uscite:int)->float:
        entrate = self.get_totale_entrate()
        uscite = self.get_totale_uscite()
        if entrate ==0:
            return 0.0
        return entrate / uscite * 100