import random
zgjedhjet=random.randint(1,100)
zgjedhja= int(input("zgjidhni nje numer nga 1-100: "))

vlera = True

while vlera:
    if zgjedhja < zgjedhjet:
        print("Provoni nje numer me te madh!")
        zgjedhja= int(input("zgjidhni nje numer nga 1-100: "))

    elif zgjedhja > zgjedhjet:
        print("Provoni nje numer me te vogel!")
        zgjedhja= int(input("zgjidhni nje numer nga 1-100: "))
    else:
        print("Urime ju e gjetet numrin")
        break
    