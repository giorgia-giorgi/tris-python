# -*- coding: utf-8 -*-
"""
Created on Wed May 29 21:09:48 2024

@author: giogi
"""
tabella = [
    [" ", " ", " "], 
    [" ", " ", " "], 
    [" ", " ", " "]
]

def main():
    turno = "x"
    while piena() == False and vincitore() == None:
        gioca(turno)
        stampa_tabella()
        
        if turno == "x":
            turno = "o"
        else:
            turno = "x"
            
    ha_vinto = vincitore()
    if (ha_vinto == None):
        print("Pareggio!")
    else:
        print("Ha vinto ", ha_vinto)
        
#y identifica la riga della tabella, la x identifica la colonna della tabella
# 2, 0   1, 1    0, 2
#questa funzione restituisce il segno del vincitore altrimenti None.
def vincitore():
    # righe
    for riga in tabella:
        diverso = False
        
        primo = riga[0]
        
        for segno in riga:
            if primo == " " or primo != segno:
                diverso = True # ho incontrato un segno diverso dal primo... break
                break

        if (diverso == False):
            return primo
    
    numero_righe = len(tabella) # 3
    numero_colonne = len(tabella[0]) # 3
    
    #colonne
    for x in range(numero_righe):
        diverso = False
        primo = tabella[0][x]
        for y in range(numero_colonne):
            elemento = tabella[y][x]
            if elemento != primo or elemento == " ":
                diverso = True
                break 
            
        if diverso == False:
            return primo # ho vinto
        
    #diagonali
    diverso = False 
    
    primo = tabella[0][0]

    for indice in range(3):
        elemento = tabella[indice][indice]
        
        if primo != elemento or elemento == " ":
            diverso = True
            break
    
    if diverso == False:
        return primo
    
    primo = tabella[2][0]

    for x in range(3):
        # lo schema è: y=2 x=0, y=1 x=1, y=0 x=2 
        # y = 2 - x 
        #- 2 + y = -x
        # x = 2 - y
        
        # in questo ciclo ho x... come ottengo y?
        y = 2 - x
        elemento = tabella[y][x]
        if elemento != primo or primo == " ":
            return None
        
    return primo

#questa funzione chiede all'utente di inserire x e y, ovvero la posizione
#nella quale vuole inserire il segno.
def gioca(segno):
    while True:        
        inserito = input("Gioca l'utente: " + segno) 
        lista = inserito.split(" ")
        x = int(float(lista[0]))
        y = int(float(lista[1]))
        
        if tabella[y][x] == " ":
            break
        
    inserisci(x, y, segno)
    
#inserisci la posizione ed il segno.
def inserisci(x, y, segno):
    tabella[y][x] = segno
    
#questa funzione controlla che non ci siano spazi nella tabella e perciò
#se così fosse è piena.
def piena():
    for riga in tabella:
        for segno in riga:
            if segno == " ":
                return False  
    return True        

#questa funzione stampa la tabella in console.
def stampa_tabella():
    for riga in tabella:
        for elemento in riga:
            print(elemento, end = "")
        print("\n")  
    
def svuota_tabella():
    for x in range(3):
        for y in range(3):
            tabella[y][x] = " "
            
            # elemento = tabella[y][x]
            # elemento = " " questo non funziona! sto cambiando il valore della variabile elemento, non il valore della tabella agli indici y x!
    
main()