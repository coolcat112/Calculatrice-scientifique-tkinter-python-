
import tkinter as tk  # Importe le module tkinter pour l'interface graphique
from math import sin, cos, tan, pi, sqrt  # Importe les fonctions mathématiques nécessaires

class Calculatrice(tk.Tk):  # Définition de la classe Calculatrice qui hérite de la classe Tkinter
    def __init__(self):
        super().__init__()  # Initialise la classe parent Tkinter
        self.title("Calculatrice")  # Définit le titre de la fenêtre
        self.geometry("440x800")  # Définit la taille par défaut de la fenêtre

        # Ajoute un label pour le titre
        titre_label = tk.Label(self, text="Calculatrice", font=12,)  # Crée un label avec le texte "Calculatrice"
        titre_label.grid(row=0, column=0, columnspan=6, pady=(30, 30))  # Place le label dans la grille de la fenêtre

        self.entry = tk.Entry(self, font=('Arial', 20), justify='right', relief="sunken", borderwidth=20)  # Crée une zone de saisie
        self.entry.grid(row=1, column=0, columnspan=6, pady=(20, 30))  # Place la zone de saisie dans la grille de la fenêtre

        # Crée les boutons dans des carrés avec un espacement
        boutons = [
            ('1', 2, 0, '#FFD700'), ('2', 2, 1, '#FFD700'), ('3', 2, 2, '#FFD700'), ('+', 2, 3, '#00CED1'),
            ('4', 3, 0, '#FFD700'), ('5', 3, 1, '#FFD700'), ('6', 3, 2, '#FFD700'), ('-', 3, 3, '#00CED1'),
            ('7', 4, 0, '#FFD700'), ('8', 4, 1, '#FFD700'), ('9', 4, 2, '#FFD700'), ('*', 4, 3, '#00CED1'),
            ('=', 5, 0, "#DC143C"), ('0', 5, 1, '#FFD700'), ('.', 5, 2, '#FFD700'), ('/', 5, 3, '#00CED1'),
            ('sin', 2, 5, '#32CD32'), ('cos', 3, 5, '#32CD32'), ('tan', 4, 5, '#32CD32'), ('pi', 5, 5, '#32CD32'),
            ('√', 6, 3, '#00CED1'), ('C', 6, 0, "#DC143C"),('(', 6, 1, '#FFD700'),(')', 6, 2, '#FFD700'),
            ('pi²', 6, 5, '#32CD32')
        ]

        for (text, row, column, color) in boutons:
            button = tk.Button(self, text=text, font=('Arial', 15), command=lambda t=text: self.appuyer_sur_un_bouton(t),bg=color)  # Crée un bouton avec du texte et un fond coloré
            button.grid(row=row, column=column, padx=10, pady=10)  # Place le bouton dans la grille de la fenêtre
            button.config(relief="raised", borderwidth=20)  # Configure le relief et la largeur de la bordure du bouton

        #Création du label historique
        titre_label = tk.Label(self, text="Historique", font=12,)  # Crée un label avec le texte "Calculatrice"
        titre_label.grid(row=0, column=6, columnspan=6)  # Place le label dans la grille de la fenêtre
        
        
        
        
        # Historique des opérations
        self.historique_listbox = tk.Listbox(self, font=('Arial', 15), selectbackground="yellow", selectmode=tk.SINGLE, height=10)
        self.historique_listbox.grid(row=1, rowspan=120, column=6, columnspan=6)
        self.historique_listbox.config(width=30, height=29)


        #Création du bouton de l'historique
        historique_button = tk.Button(self, text='Historique', font=('Arial', 15), command=self.affich_histo,bg='#FFA500')  # Crée un bouton avec du texte et un fond coloré
        historique_button.grid(row=7, column=0, columnspan=6, pady=15)  # Place le bouton dans la grille de la fenêtre
        historique_button.config(relief="raised", borderwidth=10)  # Configure le relief et la largeur de la bordure du bouton


        # Centre la fenêtre au milieu de l'écran
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() - width) // 2
        y = (self.winfo_screenheight() - height) // 2
        self.geometry(f'{width}x{height}+{x}+{y}')

    

    def affich_histo(self): #méthode qui change la taille de la fenêtre tkinter pour afficher ou non l'historique caché sur la droite
        width = self.winfo_width()
        height = self.winfo_height()
        if width == 440:
            self.geometry("790x800")
        else:
            self.geometry("440x800")



    # Fonction appelée lorsqu'un bouton est cliqué
    def appuyer_sur_un_bouton(self, value):
        self.historique = []
    # La fonction est appelée lorsqu'un bouton est cliqué dans l'interface.

        if value == "=":
            # Si le bouton cliqué est "=", cela signifie que l'utilisateur souhaite évaluer l'expression.

            try:
                # On récupère l'expression avant qu'elle soit delete pour pouvoir la stocker dans l'historique
                expression=self.entry.get()
                # Essaie d'évaluer l'expression dans l'entrée.
                result = eval(expression)

                # Efface le contenu de l'entrée et y insère le résultat obtenu.
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                
                # Ajoute l'opération et le résultat à l'historique.
                operation = f"{expression} = {result}"
                self.historique.append(operation)

                # Ajoute également l'opération à la listebox de l'historique.
                self.historique_listbox.insert(tk.END, operation)

            except Exception as e:
                # En cas d'erreur lors de l'évaluation, affiche "Erreur" dans l'entrée.
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erreur")

        
        elif value == "C":
            # Effacement complet de l'entrée
            self.entry.delete(0, tk.END)
            # Suppression du contenu de l'historique et de la liste d'historique
            
            
        # Gestion des fonctions trigonométriques
        elif value == "sin":
            self.entry.insert(tk.END, 'sin(')
        elif value == "cos":
            self.entry.insert(tk.END, 'cos(')

        elif value == "tan":
            self.entry.insert(tk.END, 'tan(')

        # Gestion des constantes mathématiques
        elif value == "pi²":
            # Insertion de la valeur de pi² dans l'entrée
            self.entry.insert(tk.END, pi*pi)

        elif value == "pi":
            # Insertion de la valeur de pi dans l'entrée
            self.entry.insert(tk.END, pi)
        # Gestion de la racine carrée
        elif value == "√":
            self.entry.insert(tk.END, 'sqrt(')

        else:
            # Insertion de la valeur du bouton dans l'entrée
            self.entry.insert(tk.END, value)


if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()
