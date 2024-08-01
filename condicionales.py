#Condicionales simples

'''temperature = 40

if temperature > 35:
    print('Aviso por alta temperatura')

else:
    print('Parámetros normales')'''

#Condicionales anidadas

'''temperature = 28

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperature < 30:
        print('Nivel naranja')
    else:
        print('Nivel rojo')'''

#Asignación de condicionales

'''temperature = 35

if temperature < 30:
    fire_risk = 'LOW'
else:
    fire_risk = 'HIGH'

fire_risk'''

'''fire_risk = 'LOW' if temperature < 30 else 'HIGH' '''

#Operadores de comparación

'''value = 8

value == 8

value != 8

value < 12

value <= 7

value > 4

value >= 9'''

#Operadores logicos 

'''x = 8

x > 4 or x > 12  # True or False

x < 4 or x > 12  # False or False

x > 4 and x > 12  # True and False

x > 4 and x < 12  # True and True

not(x != 8)  # not False'''

#Match-case

'''color = '#FF0000'

match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')'''

#Operador Morsa 

'''radius = 4.25
perimeter = 2 * 3.14 * radius
if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)'''