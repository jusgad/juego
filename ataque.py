import random

# Realice un modulo en el cual se genera una ataque en especifico
def atk_enemy(num):
    if num == 1:
        dano = random.randrange(0,20,5) # hace daño de 0 a 20 y quita de 5 en 5
        return dano
    elif num == 2:
        dano = random.randrange(5,20,5)
        return dano
    else:
        dano = random.randrange(0,30,5)
        return dano


def atk(atk):
    if atk == 1:
        print("Elegiste un ataque fuerte")
        dano = random.randrange(20,70,10)
        return dano, False
    else:
        print("Elegiste el ataque normal")
        dano = random.randrange(10,40,10)
        return dano, True