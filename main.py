# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from BilancioMensile import BilancioMensile
from Enumerations import Tipo,Ricorrenza


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def test():
    print("--Test--")
    bilancio = BilancioMensile(mese=11, anno=2026)

    bilancio.add_entry("Stipendio", Tipo.ENTRATE, 1500.0,Ricorrenza.MENSILE_FISSO)
    bilancio.add_entry("Rimborso", Tipo.ENTRATE, 500.0, Ricorrenza.VARIABILE)

    bilancio.add_entry("Affitto", Tipo.USCITE, 500.0, Ricorrenza.MENSILE_FISSO)


    tot_entrate= bilancio.get_totale(Tipo.ENTRATE)
    tot_uscite = bilancio.get_totale(Tipo.USCITE)
    saldo = tot_entrate - tot_uscite

    print(f"Totale Entrate calcolato: {tot_entrate} € ")
    print(f"Totale Uscite calcolato:  {tot_uscite} € ")
    print(f"Saldo calcolato:          {saldo} € ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    test()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
