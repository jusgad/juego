import sys
import ataque
import status

def inicio():
    print("Bienvenidos al juego")
    print("Antes de iniciar es necesario que elijas una dificultad")
    print("[1]. Facil [2]. Intermedio [3]. Dificil [#]. Salir")
    numero = int(input("=> "))
    return numero

def dificultad(num):
    if num == 1:
        print("Eligiste la dificultad Facil")
        print("Tu batalla sera contra un Paladin")
        return 100
    elif num == 2:
        print("Elkegiste la dificultad Intermedia")
        print("Tu batalla sera contra un Ogro")
        return 200
    elif num == 3:
        print("Elegiste la dificultad Dificil")
        print("Tu batalla sera contra un Dragon")
        return 300
    else:
        sys.exit()

def main():
    numero = inicio()
    hp_enemy = dificultad(numero)
    print('******')
    hp = 100
    turno = True
    print("***TU BATALLA INICIA***")
    while hp_enemy > 0 and hp > 0:
        ataque_enemigo = ataque.atk_enemy(numero)
        print("El ataque de tu enemigo fue de {}".format(ataque_enemigo))
        hp = hp - ataque_enemigo
        if hp > 0:
            if turno == True:
                status.status(hp,hp_enemy)
                print("Te toca atacar!")
                print("Elige entre dos ataques")
                print("El ataque FUERTE baja entre 20 y 60 de vida")
                print("El ataque NORMAL baja entre 10 y 30 de vida")
                print("[1]. Ataque Fuerte [#]. Ataque Normal")
                mi_ataque = int(input("=> "))
                elataque = ataque.atk(mi_ataque)
                mi_dano = elataque[0]
                turno = elataque[1]
                print("Tua ataque fue de {}".format(mi_dano))
                hp_enemy = hp_enemy - mi_dano
                if hp_enemy <= 0:
                    print("Derribaste a tu enemigo, GANASTE!!!")
                    sys.exit()
                else:
                    status.status(hp,hp_enemy)
                    pass

            else:
                turno = True
                pass

        else:
            print("Tu vida esta en 0")
            print("Haz muerto!!!, Perdiste")
            sys.exit()

if __name__== '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()