import pyfiglet
from colorama import Fore, Style, init


def firma (testo1, testo2 = "",  font='slant', colore_testo=Fore.MAGENTA, colore_bordo=Fore.RED, colore_linea=Fore.CYAN):

    init(autoreset=True)

    # Genera le parti
    parte1 = pyfiglet.figlet_format(testo1, font=font)

    if testo2:
        parte2 = pyfiglet.figlet_format(testo2, font=font)
        linee1 = parte1.split('\n')
        linee2 = parte2.split('\n')

        # Unisci orizzontalmente
        linee_unite = []
        max_linee = max(len(linee1), len(linee2))

        for i in range(max_linee):
            linea1 = linee1[i] if i < len(linee1) else ""
            linea2 = linee2[i] if i < len(linee2) else ""
            linee_unite.append(linea1 + " " + linea2)

        linee = linee_unite
    else:
        linee = parte1.split('\n')

    # Calcola larghezza
    larghezza_max = max(len(linea) for linea in linee if linea.strip())

    # Bordi
    bordo_top = colore_bordo + "+" + colore_linea + "=" * (larghezza_max + 2) + colore_bordo + "+"
    bordo_bottom = colore_bordo + "+" + colore_linea + "=" * (larghezza_max + 2) + colore_bordo + "+"

    # Stampa
    print(bordo_top)
    for linea in linee:
        if linea.strip():
            linea_colorata = ""
            for char in linea:
                if char != ' ':
                    linea_colorata += colore_testo + char
                else:
                    linea_colorata += char
            print(colore_bordo + Style.RESET_ALL + " " + linea_colorata.ljust(larghezza_max) + " " + colore_bordo)
    print(bordo_bottom)


