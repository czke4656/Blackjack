import random
from random import randint

jatekmod = int(input("Hány játékos van? (1,2):"))
if jatekmod == 1:
    print("Játékosok száma egy")
    jatekos = random.randint(2,11) + random.randint(2,11)
    robot = random.randint(2,11) + random.randint(2,11)
    print(f"Te kártyáid: {jatekos}")
    print(f"Az ellenség kártyái: {robot}")
    if jatekos > robot and jatekos <= 21 or robot > 21:
        print("Nyertél!")
    elif robot > jatekos and robot <= 21 or jatekos > 21:
        print("Vesztettél!")
    elif jatekos == robot:
        print("Döntetlen!")
elif jatekmod == 2:
    print("Játékosok száma kettő")
    jatekos1 = random.randint(2, 11) + random.randint(2, 11)
    jatekos2 = random.randint(2, 11) + random.randint(2, 11)
    print(f"Első játékos kártyái: {jatekos1}")
    print(f"Második játékos kártyái: {jatekos2}")
    if jatekos1 > jatekos2 and jatekos1 <= 21 or jatekos2 > 21:
        print("Első játékos nyert!")
    elif jatekos2 > jatekos1 and jatekos2 <= 21 or jatekos1 > 21:
        print("Második játékos nyert!")
    elif jatekos1 == jatekos2:
        print("Döntetlen!")