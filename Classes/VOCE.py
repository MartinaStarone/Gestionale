import Enumerations
from dataclasses import dataclass
import datetime
from Enumerations import *
@dataclass
class VOCE:
    descrizione: str
    tipo: Enumerations.Tipo
    importo: float
    mese: datetime.date
    ricorrenza: Enumerations.Ricorrenza = Ricorrenza.VARIABILE


