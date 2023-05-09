# Libraria
import random

# Opciones del juego
opciones = ['piedra', 'papel', 'tijera']

# Selección de opción por parte de la computadora
opcion_pc = random.choice(opciones)

# Selección de opción por parte del usuario
opcion_usr = input('Escoge entre: piedra, papel, tijera: ')
opcion_usr = opcion_usr.lower()

# Loop While en caso que usuario mal indique la opción. Se ejecutará hasta que se indique de manera correcta
while opcion_usr not in opciones:
    print('Escriba correctamente su opción')
    opcion_usr = input('Escoge entre: piedra, papel, tijera: ')
    opcion_usr = opcion_usr.lower()

# Condición if para el desarrollo del juego
if opcion_pc == opcion_usr:
    print('El computado a escogido', opcion_pc,' y tu has escogido', opcion_usr, 'por lo tanto hay un Empate')
elif opcion_pc == 'piedra':
    if opcion_usr == 'papel':
        print('El computador escogió',opcion_pc,'y tu has escogido',opcion_usr,'. Por lo tanto. Has ganado')
    else:
        print('El computador escogió',opcion_pc,'y tu has escogido',opcion_usr,'. Por lo tanto. Has perdido')
elif opcion_pc == 'papel':
    if opcion_usr == 'tijera':
        print('El computador escogió',opcion_pc,'y tu has escogido',opcion_usr,'. Por lo tanto. Has ganado')
    else:
        print('El computador escogió',opcion_pc,'y tu has escogido',opcion_usr,'. Por lo tanto. Has perdido')
else:
    if opcion_usr == 'piedra':
        print('El computador escogió',opcion_pc,'y tu has escogido',opcion_usr,'. Por lo tanto. Has ganado')
    else:
        print('El computador escogió',opcion_pc,'y tu has escogido',opcion_usr,'. Por lo tanto. Has perdido')


