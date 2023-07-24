# Libraria



def fn_opciones_juego():
    import random
    # Opciones del juego
    opciones = ('piedra', 'papel', 'tijera')

    # Selección de opción por parte de la computadora
    opcion_pc = random.choice(opciones)


    # Selección de opción por parte del usuario
    opcion_usr = input('Escoge entre: piedra, papel, tijera: \n')
    print('\n')
    opcion_usr = opcion_usr.lower()
    # Loop While en caso que usuario mal indique la opción. Se ejecutará hasta que se indique de manera correcta
    while opcion_usr not in opciones:
        print('Escriba correctamente su opción')
        opcion_usr = input('Escoge entre: piedra, papel, tijera: ')
        print('\n')
        opcion_usr = opcion_usr.lower()
    return opcion_pc, opcion_usr
    

def fn_reglas_juego(opcion_pc, opcion_usr, win_pc, win_usr):
    # Condición if para el desarrollo del juego
    if opcion_pc == opcion_usr:
        print('El computador a escogido', opcion_pc,' y tú has escogido', opcion_usr, '\nPor lo tanto, hay un Empate!!')
    elif opcion_pc == 'piedra':
        if opcion_usr == 'papel':
            print('El computador escogió',opcion_pc,'y tú has escogido',opcion_usr,'\nPor lo tanto, has ganado')
            win_usr+=1
        else:
            print('El computador escogió',opcion_pc,'y tú has escogido',opcion_usr,'\nPor lo tanto, has perdido')
            win_pc+=1
    elif opcion_pc == 'papel':
        if opcion_usr == 'tijera':
            print('El computador escogió',opcion_pc,'y tú has escogido',opcion_usr,'\nPor lo tanto, has ganado')
            win_usr+=1
        else:
            print('El computador escogió',opcion_pc,'y tú has escogido',opcion_usr,'\nPor lo tanto, has perdido')
            win_pc+=1
    else:
        if opcion_usr == 'piedra':
            print('El computador escogió',opcion_pc,'y tú has escogido',opcion_usr,'\nPor lo tanto, has ganado')
            win_usr+=1
        else:
            print('El computador escogió',opcion_pc,'y tú has escogido',opcion_usr,'\nPor lo tanto, has perdido')
            win_pc+=1
    return win_pc, win_usr


def fn_jugar():
    win_pc = 0
    win_usr = 0  
    Juego = 1
    while True:
        print('*' * 40)
        print('Juego', Juego)
        print('*' * 40)

        Juego+=1
        opcion_pc, opcion_usr = fn_opciones_juego()
        win_pc, win_usr = fn_reglas_juego(opcion_pc, opcion_usr, win_pc, win_usr)

        print('\n- Cantidad de victorias del Computador:', win_pc)
        print('- Cantidad de victorias del usuario:', win_usr)
        print('\n')
        if win_pc == 3:
            print('EL GANADOR DE ESTE JUEGO ES LA COMPUTADORA\n')
            break

        if win_usr == 3:
            print('EL GANADOR DE ESTE JUEGO ERES TÚ\n')
            break
 
fn_jugar()
