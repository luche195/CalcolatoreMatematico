import math
import sympy as sp

from firma import firma

firma("HACKINGLAB", "195")

def menu_principale():
    """Mostra il menu principale del programma"""
    print("\n" + "=" * 50)
    print("CALCOLATORE TRIGONOMETRICO E DERIVATE")
    print("=" * 50)
    print("1. Calcoli Trigonometrici")
    print("2. Calcolo Derivate")
    print("3. Calcolo Logaritmi")
    print("4. Esci")
    print("=" * 50)


def menu_trigonometria():
    """Menu per i calcoli trigonometrici"""
    print("\n--- CALCOLI TRIGONOMETRICI ---")
    print("1. Seno (sin)")
    print("2. Coseno (cos)")
    print("3. Tangente (tan)")
    print("4. Arcoseno (arcsin)")
    print("5. Arcocoseno (arccos)")
    print("6. Arcotangente (arctan)")
    print("7. Torna al menu principale")


def calcola_trigonometria():
    """Gestisce i calcoli trigonometrici"""
    while True:
        menu_trigonometria()
        scelta = input("\nScegli un'operazione (1-7): ")

        if scelta == '7':
            break

        if scelta not in ['1', '2', '3', '4', '5', '6']:
            print("Scelta non valida!")
            continue

        try:
            angolo = float(input("Inserisci l'angolo (in gradi): "))
            radianti = math.radians(angolo)

            if scelta == '1':
                risultato = math.sin(radianti)
                print(f"sin({angolo}°) = {risultato:.6f}")
            elif scelta == '2':
                risultato = math.cos(radianti)
                print(f"cos({angolo}°) = {risultato:.6f}")
            elif scelta == '3':
                risultato = math.tan(radianti)
                print(f"tan({angolo}°) = {risultato:.6f}")
            elif scelta == '4':
                if -1 <= angolo <= 1:
                    risultato = math.degrees(math.asin(angolo))
                    print(f"arcsin({angolo}) = {risultato:.6f}°")
                else:
                    print("Errore: il valore deve essere tra -1 e 1")
            elif scelta == '5':
                if -1 <= angolo <= 1:
                    risultato = math.degrees(math.acos(angolo))
                    print(f"arccos({angolo}) = {risultato:.6f}°")
                else:
                    print("Errore: il valore deve essere tra -1 e 1")
            elif scelta == '6':
                risultato = math.degrees(math.atan(angolo))
                print(f"arctan({angolo}) = {risultato:.6f}°")

        except ValueError as e:
            print(f"Errore: inserisci un numero valido ({e})")
        except Exception as e:
            print(f"Errore nel calcolo: {e}")


def menu_logaritmi():
    """Menu per i calcoli logaritmici"""
    print("\n--- CALCOLO LOGARITMI ---")
    print("1. Logaritmo naturale (ln)")
    print("2. Logaritmo base 10 (log10)")
    print("3. Logaritmo base 2 (log2)")
    print("4. Logaritmo base arbitraria")
    print("5. Antilogaritmo (e^x)")
    print("6. Torna al menu principale")


def calcola_logaritmi():
    """Gestisce i calcoli logaritmici"""
    while True:
        menu_logaritmi()
        scelta = input("\nScegli un'operazione (1-6): ")

        if scelta == '6':
            break

        if scelta not in ['1', '2', '3', '4', '5']:
            print("Scelta non valida!")
            continue

        try:
            if scelta == '1':
                numero = float(input("Inserisci il numero: "))
                if numero > 0:
                    risultato = math.log(numero)
                    print(f"ln({numero}) = {risultato:.6f}")
                else:
                    print("Errore: il logaritmo è definito solo per numeri positivi")

            elif scelta == '2':
                numero = float(input("Inserisci il numero: "))
                if numero > 0:
                    risultato = math.log10(numero)
                    print(f"log₁₀({numero}) = {risultato:.6f}")
                else:
                    print("Errore: il logaritmo è definito solo per numeri positivi")

            elif scelta == '3':
                numero = float(input("Inserisci il numero: "))
                if numero > 0:
                    risultato = math.log2(numero)
                    print(f"log₂({numero}) = {risultato:.6f}")
                else:
                    print("Errore: il logaritmo è definito solo per numeri positivi")

            elif scelta == '4':
                numero = float(input("Inserisci il numero: "))
                base = float(input("Inserisci la base: "))
                if numero > 0 and base > 0 and base != 1:
                    risultato = math.log(numero, base)
                    print(f"log_{base}({numero}) = {risultato:.6f}")
                else:
                    print("Errore: numero e base devono essere positivi, base diversa da 1")

            elif scelta == '5':
                esponente = float(input("Inserisci l'esponente: "))
                risultato = math.exp(esponente)
                print(f"e^{esponente} = {risultato:.6f}")

        except ValueError as e:
            print(f"Errore: inserisci un numero valido ({e})")
        except Exception as e:
            print(f"Errore nel calcolo: {e}")


def calcola_derivate():
    """Gestisce il calcolo delle derivate"""
    print("\n--- CALCOLO DERIVATE ---")
    print("Variabile predefinita: x")
    print("Esempi di funzioni:")
    print("  - x**2 + 3*x + 1")
    print("  - sin(x) + cos(x)")
    print("  - exp(x) * x**2")
    print("  - log(x)")

    while True:
        funzione_str = input("\nInserisci la funzione (o 'menu' per tornare): ")

        if funzione_str.lower() == 'menu':
            break

        try:
            x = sp.Symbol('x')
            funzione = sp.sympify(funzione_str)

            print(f"\nFunzione: f(x) = {funzione}")

            # Calcola la derivata prima
            derivata = sp.diff(funzione, x)
            print(f"Derivata prima: f'(x) = {derivata}")

            # Chiedi se calcolare derivate successive
            ordine = input("\nCalcolare derivate di ordine superiore? (s/n): ")
            if ordine.lower() == 's':
                n = int(input("Fino a che ordine? "))
                for i in range(2, n + 1):
                    derivata_n = sp.diff(funzione, x, i)
                    print(f"Derivata {i}ª: f^({i})(x) = {derivata_n}")

            # Valutazione in un punto
            valuta = input("\nValutare la derivata in un punto? (s/n): ")
            if valuta.lower() == 's':
                punto = float(input("Inserisci il valore di x: "))
                valore = derivata.subs(x, punto)
                print(f"f'({punto}) = {float(valore):.6f}")

        except sp.SympifyError:
            print("Errore: funzione non valida. Controlla la sintassi.")
        except Exception as e:
            print(f"Errore: {e}")


def main():
    """Funzione principale del programma"""
    print("Benvenuto nel Calcolatore Trigonometrico e Derivate!")

    while True:
        menu_principale()
        scelta = input("\nScegli un'opzione (1-4): ")

        if scelta == '1':
            calcola_trigonometria()
        elif scelta == '2':
            calcola_derivate()
        elif scelta == '3':
            calcola_logaritmi()
        elif scelta == '4':
            print("\nGrazie per aver usato il calcolatore. Arrivederci!")
            break
        else:
            print("Scelta non valida! Riprova.")


if __name__ == "__main__":
    main()