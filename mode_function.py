"""
Készíts egy függvényt, ami egy számokat tartalmazó listát
kap. A függvény adja vissza (return)
a lista móduszát.
"""

def lista_modusz(szam):
    szamok = []
    
    for elem in szam:
        if elem not in szamok:
            szamok.append(elem)
    
    print(szamok)
    
    stat = []
    for elem in szamok:
        db = 0
        for elem2 in szam:
            if elem == elem2:
                db += 1
        stat.append(db)
        
    print(stat)
    legnagyobb = max(stat)
    
    for elem, db in zip(szamok, stat):
        if db == legnagyobb:
            print(elem)

lista_modusz([2,3,3,4,4,5,5,5,6])
