#Diferencias entre Python y Javascript

#Tipos de datos en Python

'''1. Booleanos - bool: Valores de verdad y falso

        Ejemplo: b = True'''

'''2. Entero - int: Números enteros
        Ejemplo: x = 10'''

'''3. Flotante - float: Números de punto flotante
        Ejemplo: y = 3.14'''

'''4. Complejo - complex: Números complejos
        Ejemplo: z = 3 + 4j'''

'''5. Cadena - str: Cadenas de texto, se utiliza comillas simples o triples
        Ejemplo: s = 'Python' '''

'''6. Tupla - tuple: 
        Ejemplo: (1,3,5)'''

'''7. Lista - list: 
        Ejemplo: ['Chrome', 'Firefox']'''

'''8. Conjunto - set: 
        Ejemplo: set([2, 4, 6])'''

'''9. Diccionario - dict: 
        Ejemplo: {'Chrome': 'v79' , 'Firefox': 'v71'}'''


#Tipos de datos en Javascript

'''1. Números - number: Los enteros y flotantes se consideran como tipo number, lo que quiere decir que los dos se encuentran en un mismo tipo sin diferenciarlos.
        Ejemplo: let x = 10;
                 let y = 10.5;'''

'''2. Cadenas de texto - strings: Van con comillas simples o dobles.
        Ejemplo: let s = "Hola, Java!" '''

'''3. Arrays: Los arrays son objetos similares a una lista cuyo prototipo proporciona métodos para efectuar operaciones de recorrido y de mutación. 
        Ejemplo: 

        Crar un array
let frutas = ["Manzana", "Banana"];
console.log(frutas.length);
//2

        Acceder a un elemento de Array mediante su índice
let primero = frutas[0];
// Manzana

let ultimo = frutas[frutas.length - 1];
// Banana

'''

'''4. Objetos: Un objeto es una colección de propiedades, y una propiedad es una asociación entre un nombre (o clave) y un valor. 
        Ejemplo: El objeto es "myCar" y lo que lo acompaña son las propiedades
var myCar = new Object();
myCar.make = "Ford";
myCar.model = "Mustang";
myCar.year = 1969;
'''

'''5. Boolenanos: True , False'''

'''6. Null: El valor null es un literal de Javascript que representa intencionalmente un valor nulo o "vacío" 
        Ejemplo: let n = null'''

'''7. Undefined: Una variable a la que no se le ha asignado valor es de tipo undefined. '''

'''6.7 Diferencia entre null y undefined:
typeof null; // object (bug en ECMAScript, debería ser null)
typeof undefined; // undefined
null === undefined; // false
null == undefined; // true
'''

'''8. Symbol: Se garantiza que cada llamada a Symbol() devuelve un único Symbol. 
        Ejemplo: let sym1 = Symbol();'''

#Conclusión

'''Tipos Numéricos:

1. Python distingue entre int, float y complex.
2. JavaScript usa un único tipo number para enteros y flotantes, y BigInt para números enteros grandes.'''

'''Estructuras de Datos:

1. Python tiene listas (list), tuplas (tuple), y conjuntos (set).
2. JavaScript tiene arreglos (Array), y no tiene un tipo nativo de conjunto, aunque se puede usar Set introducido en ES6.'''

'''Diccionarios vs Objetos:

1. Python usa diccionarios (dict) para pares clave-valor.
2. JavaScript usa objetos (Object) para pares clave-valor.'''

'''None vs Null/Undefined:

1. Python tiene None para representar la ausencia de un valor.
2. JavaScript tiene null y undefined, donde undefined indica una variable no asignada y null es un valor explícitamente asignado.'''

'''Template Literals:

1. Python usa f-strings (f"string") para formateo de cadenas.
2. JavaScript usa backticks (template literals) para lo mismo.'''

'''Mutabilidad:

1. Python distingue entre tipos mutables (listas, diccionarios, conjuntos) e inmutables (tuplas, cadenas, enteros).
2. En JavaScript, los objetos y arreglos son mutables, pero los tipos primitivos (números, cadenas, booleanos, null, undefined, symbols) son inmutables.'''

#Diferenica en general entre ambos

'''1. JavaScript usa las llaves para definir bloques de código'''
'''2. JavaScript se enfoca en la interacción con el navegador y la manipulación del DOM (Document Object Model).'''

'''Sintaxis de Python:
        def greet(name):
        print(f"Hello, {name}!")

        greet("Alice")
'''

'''Sintaxis de JavaScript:
        function greet(name) {
           console.log(`Hello, ${name}!`);
        }

        greet("Alice");
'''