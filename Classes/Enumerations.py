from enum import Enum

class Tipo(str,Enum):
    ENTRATE = "entrate"
    USCITE = "uscite"

class Ricorrenza(str,Enum):
    ANNUALE_FISSO = "annuale_fisso"
    MENSILE_FISSO = "mensile_fisso"
    VARIABILE = "variabile"

class Categoria(str,Enum):
    STIPENDIO = "Stipendio"
    CASA = "Casa"
    IMPOSTE = "Imposte"
    ASSICURAZIONE = "Assicurazione"
    ALTRE = "Altre"
    AFFITTI = "Affiti"
    RIMBORSI = "Riborsi"

