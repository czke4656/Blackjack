import random
from random import randint

jatekmod = int(input("Hány játékos van? (1,2):"))
if jatekmod == 1:
    print("Játékosok száma egy")
    jatekos = random.randint(2,11) + random.randint(2,11)
    robot = random.randint(2,11) + random.randint(2,11)
    print(f"te kártyáid: {jatekos}")
    print(f"az ellenség kártyái: {robot}")
    if jatekos > robot and jatekos <= 21 or robot > 21:
        print("Nyertél!")
    elif robot > jatekos and robot <= 21 or jatekos > 21:
        print("Vesztettél!")
    elif jatekos == robot:
        print("Döntetlen!")