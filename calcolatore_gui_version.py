import tkinter as tk
import sympy as sp

from firma import firma

firma("HACKINGLAB", "195")

class CalcolatoreMatematico:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcolatore Matematico")
        self.root.geometry("600x700")
        self.root.configure(bg='#2c3e50')

        # Blocca il ridimensionamento della finestra
        self.root.resizable(False, False)

        # Variabile per l'equazione
        self.equazione = tk.StringVar()

        # Crea l'interfaccia
        self.crea_interfaccia()

    def crea_interfaccia(self):
        # Frame principale
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(expand=True, fill='both', padx=10, pady=10)

        # Display per l'equazione
        display_frame = tk.Frame(main_frame, bg='#34495e', bd=2, relief='solid')
        display_frame.pack(fill='x', pady=(0, 10))

        self.display = tk.Entry(
            display_frame,
            textvariable=self.equazione,
            font=('Arial', 20),
            bg='#ecf0f1',
            fg='#2c3e50',
            justify='right',
            bd=0
        )
        self.display.pack(fill='x', padx=5, pady=5, ipady=10)

        # Area risultati
        risultati_frame = tk.Frame(main_frame, bg='#34495e', bd=2, relief='solid')
        risultati_frame.pack(fill='both', pady=(0, 10))

        self.risultato_label = tk.Label(
            risultati_frame,
            text="Risultato: ",
            font=('Arial', 12, 'bold'),
            bg='#34495e',
            fg='#ecf0f1',
            anchor='w'
        )
        self.risultato_label.pack(fill='x', padx=5, pady=5)

        self.derivata_label = tk.Label(
            risultati_frame,
            text="",
            font=('Arial', 11),
            bg='#34495e',
            fg='#3498db',
            anchor='w',
            wraplength=580
        )
        self.derivata_label.pack(fill='x', padx=5, pady=(0, 5))

        # Frame tastiera
        tastiera_frame = tk.Frame(main_frame, bg='#2c3e50')
        tastiera_frame.pack(expand=True, fill='both')

        # Definizione pulsanti
        funzioni = [
            ['sin(', 'cos(', 'tan(', 'log(', 'ln('],
            ['asin(', 'acos(', 'atan(', 'sqrt(', 'π'],
            ['7', '8', '9', '/', '^'],
            ['4', '5', '6', '*', '('],
            ['1', '2', '3', '-', ')'],
            ['0', '.', 'e', '+', 'x'],
        ]

        # Crea pulsanti funzioni matematiche
        for i, riga in enumerate(funzioni):
            for j, testo in enumerate(riga):
                if testo in ['sin(', 'cos(', 'tan(', 'asin(', 'acos(', 'atan(']:
                    colore = '#e74c3c'  # Rosso per trigonometria
                elif testo in ['log(', 'ln(', 'sqrt(']:
                    colore = '#9b59b6'  # Viola per logaritmi
                elif testo in ['π', 'e', 'x']:
                    colore = '#16a085'  # Verde per costanti
                elif testo in ['+', '-', '*', '/', '^', '(', ')']:
                    colore = '#f39c12'  # Arancione per operatori
                else:
                    colore = '#34495e'  # Grigio per numeri

                btn = tk.Button(
                    tastiera_frame,
                    text=testo,
                    font=('Arial', 14, 'bold'),
                    bg=colore,
                    fg='white',
                    bd=0,
                    command=lambda t=testo: self.gestisci_pulsante(t)
                )
                btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)

        # Pulsanti di controllo
        controlli = [
            ('CALCOLA', '#27ae60', self.calcola),
            ('DERIVATA', '#3498db', self.calcola_derivata),
            ('CANCELLA', '#c0392b', self.cancella),
            ('←', '#95a5a6', self.backspace)
        ]

        riga_controlli = len(funzioni)
        for j, (testo, colore, comando) in enumerate(controlli):
            btn = tk.Button(
                tastiera_frame,
                text=testo,
                font=('Arial', 12, 'bold'),
                bg=colore,
                fg='white',
                bd=0,
                command=comando
            )
            # Distribuisci i pulsanti: CALCOLA e DERIVATA occupano 2 colonne
            if j < 2:
                btn.grid(row=riga_controlli, column=j * 2, columnspan=2, sticky='nsew', padx=2, pady=2)
            else:
                btn.grid(row=riga_controlli, column=j + 2, sticky='nsew', padx=2, pady=2)

        # Configura il ridimensionamento
        for i in range(len(funzioni) + 1):
            tastiera_frame.grid_rowconfigure(i, weight=1)
        for j in range(5):
            tastiera_frame.grid_columnconfigure(j, weight=1)

    def gestisci_pulsante(self, carattere):
        """Gestisce il click sui pulsanti, con logica speciale per log"""
        if carattere == 'log(':
            base = self.chiedi_base_logaritmo()
            if base is not None:
                self.aggiungi_carattere(f'log{base}(')
        else:
            self.aggiungi_carattere(carattere)

    def chiedi_base_logaritmo(self):
        """Apre una finestra per chiedere la base del logaritmo"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Base Logaritmo")
        dialog.geometry("320x150")
        dialog.configure(bg='#34495e')
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.resizable(False, False)

        tk.Label(
            dialog,
            text="Inserisci la base del logaritmo:",
            font=('Arial', 12),
            bg='#34495e',
            fg='white'
        ).pack(pady=10)

        tk.Label(
            dialog,
            text="(deve essere > 0 e ≠ 1)",
            font=('Arial', 9),
            bg='#34495e',
            fg='#95a5a6'
        ).pack()

        entry = tk.Entry(dialog, font=('Arial', 14), justify='center')
        entry.pack(pady=10, padx=20, fill='x')
        entry.focus()

        error_label = tk.Label(dialog, text="", fg='#e74c3c', bg='#34495e', font=('Arial', 9))
        error_label.pack()

        risultato = [None]

        def conferma():
            try:
                base = float(entry.get())
                if base <= 0:
                    error_label.config(text="La base deve essere positiva!")
                elif base == 1:
                    error_label.config(text="La base non può essere 1!")
                else:
                    risultato[0] = base
                    dialog.destroy()
            except ValueError:
                error_label.config(text="Inserisci un numero valido!")

        def annulla():
            dialog.destroy()

        frame_btn = tk.Frame(dialog, bg='#34495e')
        frame_btn.pack(pady=5)

        tk.Button(
            frame_btn,
            text="OK",
            command=conferma,
            bg='#27ae60',
            fg='white',
            font=('Arial', 10, 'bold'),
            width=10
        ).pack(side='left', padx=5)

        tk.Button(
            frame_btn,
            text="Annulla",
            command=annulla,
            bg='#c0392b',
            fg='white',
            font=('Arial', 10, 'bold'),
            width=10
        ).pack(side='left', padx=5)

        entry.bind('<Return>', lambda e: conferma())
        dialog.bind('<Escape>', lambda e: annulla())

        self.root.wait_window(dialog)
        return risultato[0]

    def aggiungi_carattere(self, carattere):
        """Aggiunge un carattere all'equazione"""
        if carattere == 'π':
            carattere = 'pi'
        elif carattere == '^':
            carattere = '**'

        valore_attuale = self.equazione.get()
        self.equazione.set(valore_attuale + carattere)
        self.display.icursor(tk.END)

    def cancella(self):
        """Cancella tutto"""
        self.equazione.set('')
        self.risultato_label.config(text="Risultato: ")
        self.derivata_label.config(text="")

    def backspace(self):
        """Cancella l'ultimo carattere"""
        valore_attuale = self.equazione.get()
        self.equazione.set(valore_attuale[:-1])

    def calcola(self):
        """Calcola il valore dell'espressione"""
        try:
            expr = self.equazione.get()

            # Gestisci logaritmi con base personalizzata (es: log2(x) -> math.log(x, 2))
            import re
            expr_calc = re.sub(r'log(\d+\.?\d*)\(([^)]+)\)', r'math.log(\2, \1)', expr)

            # Sostituisci le funzioni per il calcolo numerico
            expr_calc = expr_calc.replace('ln', 'log').replace('^', '**')
            expr_calc = expr_calc.replace('asin', 'math.asin')
            expr_calc = expr_calc.replace('acos', 'math.acos')
            expr_calc = expr_calc.replace('atan', 'math.atan')
            expr_calc = expr_calc.replace('sin', 'math.sin')
            expr_calc = expr_calc.replace('cos', 'math.cos')
            expr_calc = expr_calc.replace('tan', 'math.tan')
            expr_calc = expr_calc.replace('sqrt', 'math.sqrt')
            expr_calc = expr_calc.replace('log', 'math.log')
            expr_calc = expr_calc.replace('pi', 'math.pi')
            expr_calc = expr_calc.replace('e', 'math.e')

            # Se c'è x, chiedi il valore
            if 'x' in expr:
                valore_x = self.chiedi_valore_x()
                if valore_x is not None:
                    expr_calc = expr_calc.replace('x', str(valore_x))
                else:
                    return

            risultato = eval(expr_calc)
            self.risultato_label.config(text=f"Risultato: {risultato:.6f}")

        except Exception as e:
            self.risultato_label.config(text=f"Errore: {str(e)}")

    def calcola_derivata(self):
        """Calcola la derivata dell'espressione"""
        try:
            expr = self.equazione.get()

            # Gestisci logaritmi con base personalizzata per sympy (es: log2(x) -> log(x)/log(2))
            import re
            expr_sympy = re.sub(r'log(\d+\.?\d*)\(([^)]+)\)', r'(log(\2)/log(\1))', expr)

            # Converti per sympy
            expr_sympy = expr_sympy.replace('^', '**')

            x = sp.Symbol('x')
            funzione = sp.sympify(expr_sympy)
            derivata = sp.diff(funzione, x)

            self.derivata_label.config(text=f"Derivata: f'(x) = {derivata}")

            # Calcola anche il valore se possibile
            if 'x' in expr:
                valore_x = self.chiedi_valore_x()
                if valore_x is not None:
                    valore_derivata = float(derivata.subs(x, valore_x))
                    testo_attuale = self.derivata_label.cget("text")
                    self.derivata_label.config(
                        text=f"{testo_attuale}\nf'({valore_x}) = {valore_derivata:.6f}"
                    )

        except Exception as e:
            self.derivata_label.config(text=f"Errore derivata: {str(e)}")

    def chiedi_valore_x(self):
        """Apre una finestra per chiedere il valore di x"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Valore di x")
        dialog.geometry("300x120")
        dialog.configure(bg='#34495e')
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.resizable(False, False)

        tk.Label(
            dialog,
            text="Inserisci il valore di x:",
            font=('Arial', 12),
            bg='#34495e',
            fg='white'
        ).pack(pady=10)

        entry = tk.Entry(dialog, font=('Arial', 14), justify='center')
        entry.pack(pady=5, padx=20, fill='x')
        entry.focus()

        risultato = [None]

        def conferma():
            try:
                risultato[0] = float(entry.get())
                dialog.destroy()
            except:
                tk.Label(
                    dialog,
                    text="Valore non valido!",
                    fg='red',
                    bg='#34495e'
                ).pack()

        def annulla():
            dialog.destroy()

        frame_btn = tk.Frame(dialog, bg='#34495e')
        frame_btn.pack(pady=10)

        tk.Button(
            frame_btn,
            text="OK",
            command=conferma,
            bg='#27ae60',
            fg='white',
            font=('Arial', 10, 'bold'),
            width=10
        ).pack(side='left', padx=5)

        tk.Button(
            frame_btn,
            text="Annulla",
            command=annulla,
            bg='#c0392b',
            fg='white',
            font=('Arial', 10, 'bold'),
            width=10
        ).pack(side='left', padx=5)

        entry.bind('<Return>', lambda e: conferma())
        dialog.bind('<Escape>', lambda e: annulla())

        self.root.wait_window(dialog)
        return risultato[0]


def main():
    root = tk.Tk()
    app = CalcolatoreMatematico(root)
    root.mainloop()


if __name__ == "__main__":
    main()