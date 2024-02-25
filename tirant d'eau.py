from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from math import *
import cmath
from tkinter import messagebox
from tkinter import filedialog
from tkinter.simpledialog import askstring

window = Tk()
window.geometry("1200x1200")
window.title("Tirant d'eau")
window.configure(bg='white')
window.resizable(FALSE, FALSE)



def goto_Conduite_circulaire():
    # Hide page 1 and show page 2
    page1_frame.grid_forget()
    frame.grid(row=0, column=0, padx=20, pady=10)
    
def goto_Canal_trapezoidale():
    page1_frame.grid_forget()
    frame_canal.grid(row=0, column=0, padx=20, pady=10)     
   

def return_to_page1():
    # Hide page 2 and show page 1
    frame.grid_forget()
    frame_canal.grid_forget()
    page1_frame.grid(row=0, column=0, padx=20, pady=10)
    # Appeler la fonction pour effacer les champs d'entrée
    clear_input_fields()

def clear_input_fields():
    D_entry.delete(0, END)
    R_entry.delete(0, END)
    k_entry.delete(0, END)
    Pente_entry.delete(0, END)
    Q_entry.delete(0, END)
    Phi_entry.delete(0, END)
    Gamma_entry.delete(0, END)
    téta_rad_entry.delete(0, END)
    Q_10_entry.delete(0, END)
    Gamma_10_entry.delete(0, END)
    téta_10_rad_entry.delete(0, END)
    téta_deg_entry.delete(0, END)
    h_entry.delete(0, END)
    Q_10_entry.delete(0, END)
    Gamma_10_entry.delete(0, END)
    téta_10_deg_entry.delete(0, END)
    h_10_entry.delete(0, END)
    Matériaux_combobox.set('')  # Efface la sélection du matériau


# Creation de la page 1
page1_frame = Frame(window, width=1200, height=1200, bg='#222448')
page1_frame.grid(row=0, column=0, padx=20, pady=10)  # Affichage de la page 1

# Button on Page 1
click_me_button = Button(page1_frame,width=20, border=4, font=('arial', 20) ,text="Conduite circulaire", command=goto_Conduite_circulaire)
click_me_button.place(x=450, y=300)

canal_trapezoidale_button = Button(page1_frame,width=20, border=4, font=('arial', 20) ,text="Canal trapezoidale", command=goto_Canal_trapezoidale)
canal_trapezoidale_button.place(x=450, y=350)

# Creation de la page Conduite circulaire
frame = Frame(window, width=1200, height=1200, bg='white')  
# Définition de la taille du frame

# Placer le cadre rouge au milieu du frame
Conduite_circulaire = Frame(frame, width=500, height=900)
Conduite_circulaire.place(x=20, y=20)

# Déclaration globale de valeur_teta_deg
valeur_teta_deg = 0
valeur_teta_10_deg = 0 

def update_k_entry(event):
    selected_material = Matériaux_combobox.get()

    if selected_material == "PVC":
        k_entry.delete(0, END)
        k_entry.insert(0, "85")
    elif selected_material == "Béton neuf":
        k_entry.delete(0, END)
        k_entry.insert(0, "60")
    elif selected_material == "Béton usée":
        k_entry.delete(0, END)
        k_entry.insert(0, "55")
    else:
        k_entry.delete(0, END)

def function():
    valeur_D = float(D_entry.get())
    valeur_R = valeur_D / 2
    
    R_entry.delete(0, END)
    R_entry.insert(0, valeur_R)
    
    valeur_k = float(k_entry.get())
    valeur_Pente = float(Pente_entry.get())
    valeur_R = float(R_entry.get())

    # Calcul de Phi en fonction des paramètres
    valeur_Phi = valeur_k * (valeur_R ** (8/3)) * sqrt(valeur_Pente)

    # Mise à jour de l'entrée Phi
    Phi_entry.delete(0, END)
    Phi_entry.insert(0, valeur_Phi)
    
    valeur_Q = float(Q_entry.get())
    
    valeur_Gamma = (valeur_Q / valeur_Phi)**(3/5)
    
    # Mise à jour de l'entrée Gamma
    Gamma_entry.delete(0, END)
    Gamma_entry.insert(0, valeur_Gamma)
    
    # Récupération de la valeur de téta_rad
    valeur_teta_rad = float(téta_rad_entry.get())

    # Conversion de téta_rad en degrés
    valeur_teta_deg = valeur_teta_rad * (180 / pi)

    # Mise à jour de l'entrée téta_deg_entry
    téta_deg_entry.delete(0, END)
    téta_deg_entry.insert(0, valeur_teta_deg)
    
    # Calcul de h
    valeur_h = valeur_R*(1+cos(valeur_teta_rad))
    
    # Mise à jour de l'entrée h
    h_entry.delete(0, END)
    h_entry.insert(0, valeur_h)
    
    # Calcul de Q/10
    valeur_Q_10 = valeur_Q / 10
    
    # Mise à jour de l'entrée Q_10
    Q_10_entry.delete(0, END)
    Q_10_entry.insert(0, valeur_Q_10)
    
    # Calcul de Gamma/10
    valeur_Gamma_10 = (valeur_Q_10 / valeur_Phi)**(3/5)
    
    # Mise à jour de l'entrée Q_10
    Gamma_10_entry.delete(0, END)
    Gamma_10_entry.insert(0, valeur_Gamma_10)
    
    
    # Récupération de la valeur de téta_rad
    valeur_teta_10_rad = float(téta_10_rad_entry.get())

    # Conversion de téta_rad en degrés
    valeur_teta_10_deg = valeur_teta_10_rad * (180 / pi)
    
    # Mise à jour de l'entrée téta_deg_10_entry
    téta_10_deg_entry.delete(0, END)
    téta_10_deg_entry.insert(0, valeur_teta_10_deg)
    
    # Calcul de h/10
    valeur_h_10 = valeur_R*(1+cos(valeur_teta_10_rad))
    
    # Mise à jour de l'entrée h
    h_10_entry.delete(0, END)
    h_10_entry.insert(0, valeur_h_10)

ma_variable = StringVar()
ma_variable_k = StringVar()
ma_variable_Pente = StringVar()
ma_variable_R = StringVar()
ma_variable_Q = StringVar()
ma_variable_Phi = StringVar()
ma_variable_téta_rad = StringVar()
ma_variable_Q_10 = StringVar()
ma_variable_Gamma_10 = StringVar()
ma_variable_téta_rad_10 = StringVar()



image_path = 'conduite circulaire surface libre 2.png'
image_pil = Image.open(image_path)
image_tk = ImageTk.PhotoImage(image_pil)
label = Label(frame, image=image_tk, bg='white')
label.image = image_tk  # Gardez une référence pour éviter la suppression par le garbage collector
label.place(x=500, y=80)

button_retour = Button(frame, text="Retour", width=20, border=2, command=return_to_page1, bg="#222448", fg="white")
button_retour.place(x=1000, y=600)

D = Label(frame, text="D", bg='white', fg="black", font=("Arial", 15))
D.place(x=475, y=370)

D_entry = Entry(frame, width=10, border=2, textvariable=ma_variable)
D_entry.place(x=500, y=375)

Input_frame = LabelFrame(Conduite_circulaire, text="Input")
Input_frame.grid(row=0, column=0, padx=20, pady=10)

R = Label(Input_frame, text="R")
R.grid(row=0, column=0, pady=10)

R_entry = Entry(Input_frame, width=10, border=2, textvariable=ma_variable_R)
R_entry.grid(row=0, column=1, pady=10)

button = Button(frame, text="valider", command=function)
button.place(x=800, y=575)

Matériaux = Label(Input_frame, text="Matériaux")
Matériaux.grid(row=0, column=2)

Matériaux_combobox = ttk.Combobox(Input_frame, values=["PVC", "Béton neuf", "Béton usée"], width=15)
Matériaux_combobox.grid(row=0, column=3)
Matériaux_combobox.bind("<<ComboboxSelected>>", update_k_entry)

k = Label(Input_frame, text="k")
k.grid(row=1, column=0)

k_entry = Entry(Input_frame, width=10, border=2, textvariable=ma_variable_k)
k_entry.grid(row=1, column=1)

Pente = Label(Input_frame, text="Pente")
Pente.grid(row=1, column=2)

Pente_entry = Entry(Input_frame, textvariable=ma_variable_Pente, width=15, border=2)
Pente_entry.grid(row=1, column=3) 

Q = Label(Input_frame, text="Q hydro")
Q.grid(row=1, column=4)

Q_entry = Entry(Input_frame, width=10, border=2, textvariable=ma_variable_Q)
Q_entry.grid(row=1, column=5) 

Phi = Label(Input_frame, text="Phi")
Phi.grid(row=2, column=2)

Phi_entry = Entry(Input_frame, width=15, border=2, textvariable=ma_variable_Phi)
Phi_entry.grid(row=2, column=3) 

Gamma = Label(Input_frame, text="Gamma")
Gamma.grid(row=3, column=2)

Gamma_entry = Entry(Input_frame, width=15, border=2)
Gamma_entry.grid(row=3, column=3) 

for widget in Input_frame.winfo_children():
    widget.grid_configure(padx=2, pady=10) 
    
choix_de_teta= LabelFrame(Conduite_circulaire, text="Choix de téta")
choix_de_teta.grid(row=1, column=0, padx=20, pady=10)    

téta_rad = Label(choix_de_teta, text="téta(rad)")
téta_rad.grid(row=0, column=0, pady=10)
téta_rad_entry = Entry(choix_de_teta, width=10, border=2, textvariable=ma_variable_téta_rad)
téta_rad_entry.grid(row=0, column=1, pady=10)

téta_deg = Label(choix_de_teta, text="téta(deg)")
téta_deg.grid(row=0, column=2, pady=10)
téta_deg_entry = Entry(choix_de_teta, width=10, border=2)
téta_deg_entry.grid(row=0, column=3, pady=10) 

def function2():
    global valeur_teta_deg
    

    i = 1
    limite_iterations = 100
    tolerance = 1e-2
    valeur_Gamma = float(Gamma_entry.get())  # Ajout de l'initialisation de valeur_Gamma
    
    while i <= limite_iterations:
        nouvelle_valeur_teta_deg = pi + abs(cmath.asin(cmath.sin(valeur_teta_deg))) * abs(cmath.acos(cmath.cos(valeur_teta_deg))) - valeur_Gamma * (2 * (pi - valeur_teta_deg))**(2/5)
        
        if abs(nouvelle_valeur_teta_deg - valeur_teta_deg) <= tolerance:
            valeur_teta_deg = nouvelle_valeur_teta_deg
            messagebox.showinfo(title="Valeur de téta(deg)", message="La valeur finale de teta_deg : {}".format(valeur_teta_deg.real))

            # Recalcul de p et t à l'intérieur de la boucle pour refléter la mise à jour de valeur_teta_deg
            p = pi + abs(cmath.asin(cmath.sin(valeur_teta_deg))) * abs(cmath.acos(cmath.cos(valeur_teta_deg)))  
            t = (2*(pi - valeur_teta_deg))**(2/5)  
            
            return
        
        valeur_teta_deg = nouvelle_valeur_teta_deg
        i += 1
        
    messagebox.showinfo(title="Valeur de téta(deg)", message="La valeur finale de teta_deg : {}".format(valeur_teta_deg.real))   



# Il serait utile de recalculer p et t ici pour la première initialisation
p = pi + abs(cmath.asin(cmath.sin(valeur_teta_deg))) * abs(cmath.acos(cmath.cos(valeur_teta_deg)))  
t = (2*(pi - valeur_teta_deg))**(2/5)  

button2 = Button(choix_de_teta, text="Itération", command=function2)
button2.grid(row=1, column=3)

h = Label(choix_de_teta, text="h")
h.grid(row=2, column=2, pady=10)
h_entry = Entry(choix_de_teta, width=15, border=2)
h_entry.grid(row=2, column=3, pady=10)

for widget in choix_de_teta.winfo_children():
    widget.grid_configure(padx=2, pady=10) 

# Création de la 3eme frame label "AUTOCURAGE"    
Autocurage= LabelFrame(Conduite_circulaire, text="Autocurage")
Autocurage.grid(row=2, column=0, padx=20, pady=10) 

Q_10 = Label(Autocurage, text="Q/10")
Q_10.grid(row=0, column=0, pady=10)
Q_10_entry = Entry(Autocurage, width=10, border=2, textvariable=ma_variable_Q_10)
Q_10_entry.grid(row=0, column=1, pady=10)

Gamma_10 = Label(Autocurage, text="Gamma/10")
Gamma_10.grid(row=0, column=2, pady=10)
Gamma_10_entry = Entry(Autocurage, width=10, border=2, textvariable=ma_variable_Gamma_10)
Gamma_10_entry.grid(row=0, column=3, pady=10)

téta_10_rad = Label(Autocurage, text="téta/10(rad)")
téta_10_rad.grid(row=1, column=0, pady=10)
téta_10_rad_entry = Entry(Autocurage, width=10, border=2, textvariable=ma_variable_téta_rad_10)
téta_10_rad_entry.grid(row=1, column=1, pady=10)

téta_10_deg = Label(Autocurage, text="téta/10(deg)")
téta_10_deg.grid(row=1, column=2, pady=10)
téta_10_deg_entry = Entry(Autocurage, width=10, border=2)
téta_10_deg_entry.grid(row=1, column=3, pady=10)

def function3():
    global valeur_teta_10_deg
    global valeur_teta_deg

    n = 1
    limite_iterations = 100
    tolerance = 1e-2
    valeur_Gamma_10 = float(Gamma_10_entry.get())
    
    while n <= limite_iterations:
        nouvelle_valeur_teta_10_deg = pi + abs(cmath.asin(cmath.sin(valeur_teta_10_deg))) * abs(cmath.acos(cmath.cos(valeur_teta_10_deg))) - valeur_Gamma_10 * (2 * (pi - valeur_teta_10_deg))**(2/5)
        
        if abs(nouvelle_valeur_teta_10_deg - valeur_teta_10_deg) <= tolerance:
            valeur_teta_10_deg = nouvelle_valeur_teta_10_deg
            messagebox.showinfo(title="Valeur de téta(deg)", message="La valeur finale de teta_deg : {}".format(valeur_teta_10_deg.real))

            # Recalcul de p et t à l'intérieur de la boucle pour refléter la mise à jour de valeur_teta_deg
            p2 = pi + abs(cmath.asin(cmath.sin(valeur_teta_10_deg))) * abs(cmath.acos(cmath.cos(valeur_teta_10_deg)))
                
            t2 = (2*(pi - valeur_teta_10_deg))**(2/5)  
            
            return
        
        valeur_teta_10_deg = nouvelle_valeur_teta_10_deg
        n += 1
        
    messagebox.showinfo(title="Valeur de téta(deg)", message="La valeur finale de teta_deg : {}".format(valeur_teta_10_deg.real))  

p2 = pi + abs(cmath.asin(cmath.sin(valeur_teta_10_deg))) * abs(cmath.acos(cmath.cos(valeur_teta_10_deg)))
t2 = (2*(pi - valeur_teta_10_deg))**(2/5) 

button3 = Button(Autocurage, text="Itération", command=function3)
button3.grid(row=2, column=3)

h_10 = Label(Autocurage, text="h/10")
h_10.grid(row=3, column=2, pady=10)
h_10_entry = Entry(Autocurage, width=15, border=2)
h_10_entry.grid(row=3, column=3, pady=10)

for widget in Autocurage.winfo_children():
    widget.grid_configure(padx=2, pady=10) 
    
    
    

# Creation de la page Canal trapezoidale
frame_canal = Frame(window, width=1200, height=1200)  
# Placer le cadre rouge au milieu du frame
Canal_trapezoidale = Frame(frame_canal, width=500, height=900, bg="red")
Canal_trapezoidale.place(x=20, y=20) 

# Affichage de l'image pour le canal trapezoidale
image_path_canal = 'canal trapezoidale.png'
image_pil_canal = Image.open(image_path_canal)
image_tk_canal = ImageTk.PhotoImage(image_pil_canal)
label_canal = Label(frame_canal, image=image_tk_canal, bg='white')
label_canal.image = image_tk_canal  # Gardez une référence pour éviter la suppression par le garbage collector
label_canal.place(x=600, y=100)

button_retour_2 = Button(frame_canal, text="Retour", width=10, border=2, command=return_to_page1)
button_retour_2.place(x=900, y=600)

mon_menu = Menu(window, bg="blue")

#sous onglet Fichier
fichier = Menu(mon_menu, tearoff=0)


mon_menu.add_cascade(label='Fichier', menu=fichier)

window.config(menu=mon_menu)

import os


def enregistrer_donnees():
    # Récupérer les données des champs d'entrée et autres endroits
    # Vous pouvez les stocker dans une structure de données ou les récupérer directement des widgets

    # Par exemple, récupérer les données depuis les Entry widgets
    valeur_D = D_entry.get()
    valeur_R = R_entry.get()
    valeur_k = k_entry.get()
    valeur_Pente = Pente_entry.get()
    valeur_Q = Q_entry.get()
    valeur_Phi = Phi_entry.get()
    valeur_Gamma = Gamma_entry.get()
    valeur_teta_rad = téta_rad_entry.get()
    valeur_Q_10 = Q_10_entry.get()
    valeur_Gamma_10 = Gamma_10_entry.get()
    valeur_teta_rad_10 = téta_10_rad_entry.get()

    # Demander à l'utilisateur de spécifier l'emplacement et le nom du fichier
    chemin_fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])

    # Vérifier si l'utilisateur a spécifié un nom de fichier
    if chemin_fichier:
        # Écrire les données dans le fichier texte
        with open(chemin_fichier, "w") as fichier:
            fichier.write("Données enregistrées :\n")
            fichier.write(f"D : {valeur_D}\n")
            fichier.write(f"R : {valeur_R}\n")
            fichier.write(f"k : {valeur_k}\n")
            fichier.write(f"Pente : {valeur_Pente}\n")
            fichier.write(f"Q : {valeur_Q}\n")
            fichier.write(f"Phi : {valeur_Phi}\n")
            fichier.write(f"Gamma : {valeur_Gamma}\n")
            fichier.write(f"teta_rad : {valeur_teta_rad}\n")
            fichier.write(f"Q_10 : {valeur_Q_10}\n")
            fichier.write(f"Gamma_10 : {valeur_Gamma_10}\n")
            fichier.write(f"teta_rad_10 : {valeur_teta_rad_10}\n")

            messagebox.showinfo("Enregistrement", f"Les données ont été enregistrées avec succès dans {chemin_fichier}")

 

        
fichier.add_command(label="Enregistrer", command=enregistrer_donnees)  

def ouvrir_fichier():
    chemin_initial = os.path.join(os.path.expanduser("~"), "Bureau", "spyder python")
    chemin_fichier = filedialog.askopenfilename(initialdir=chemin_initial, title="Sélectionner le fichier",
                                                 filetypes=(("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")))
    
    if chemin_fichier:
        with open(chemin_fichier, "r") as fichier:
            # Lire les données du fichier et les traiter
            lignes = fichier.readlines()
            for ligne in lignes:
                # Vérifier si le séparateur est présent dans la ligne
                if " : " in ligne:
                    cle, valeur = ligne.strip().split(" : ")
                    
                    # Mettre à jour les champs d'entrée correspondants
                    if cle == "D":
                        D_entry.delete(0, END)
                        D_entry.insert(0, valeur)
                    elif cle == "R":
                        R_entry.delete(0, END)
                        R_entry.insert(0, valeur)
                    elif cle == "k":
                        k_entry.delete(0, END)
                        k_entry.insert(0, valeur)
                    elif cle == "Pente":
                        Pente_entry.delete(0, END)
                        Pente_entry.insert(0, valeur)
                    elif cle == "Q":
                        Q_entry.delete(0, END)
                        Q_entry.insert(0, valeur)
                    elif cle == "Phi":
                        Phi_entry.delete(0, END)
                        Phi_entry.insert(0, valeur)
                    elif cle == "Gamma":
                        Gamma_entry.delete(0, END)
                        Gamma_entry.insert(0, valeur)
                    elif cle == "teta_rad":
                        téta_rad_entry.delete(0, END)
                        téta_rad_entry.insert(0, valeur)
                    elif cle == "Q_10":
                        Q_10_entry.delete(0, END)
                        Q_10_entry.insert(0, valeur)
                    elif cle == "Gamma_10":
                        Gamma_10_entry.delete(0, END)
                        Gamma_10_entry.insert(0, valeur)
                    elif cle == "teta_rad_10":
                        téta_10_rad_entry.delete(0, END)
                        téta_10_rad_entry.insert(0, valeur)
                else:
                    # Si le séparateur n'est pas trouvé, afficher un avertissement
                    print(f"La ligne suivante n'a pas le bon format : {ligne.strip()}")

        messagebox.showinfo("Fichier ouvert", "Les données ont été chargées avec succès !")
    else:
        messagebox.showwarning("Fichier introuvable", "Le fichier données_enregistrees.txt n'existe pas.")

# Ajoutez cette fonction à votre menu
fichier.add_command(label="Ouvrir", command=ouvrir_fichier) 

         
window.mainloop()









