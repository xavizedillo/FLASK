# Definición de una lista con días de la semana
week = ['Lunes','Martes','Miercoles', 'Jueves', 'Viernes', 'Sabado'] 

# Variable string que contiene información separada por " | "
misDatos = "Xavier Alejandro | 4A | Azul"
print(misDatos)

# PRIMER EJERCICIO: Slicing negativo
# [-4:] significa "toma los últimos 4 caracteres"
# Resultado: "Azul"
print(misDatos [-4: ])

# SEGUNDO EJERCICIO: División de string en lista
# split(" | ") divide el string donde encuentra " | "
# Resultado: ['Xavier Alejandro', '4A', 'Azul']
out = misDatos.split(" | ")
print(out)

# TERCER EJERCICIO: Invertir lista in-place
# reverse() modifica la lista original y devuelve None
# Después de esto: ['Azul', '4A', 'Xavier Alejandro']
out.reverse()
print(out)

# CUARTO EJERCICIO: Invertir string con slicing
# [::-1] es un slicing que invierte el string completo
# Resultado: "luzA | A4 | ordnajelA reivaX"
out = misDatos[::-1]
print(out)

# QUINTO EJERCICIO: Condicionales y valores de verdad
# En Python, 1 es True y 0 es False
# Cualquier string no vacío se considera True

if (1):
    print("True")  # Se ejecuta porque 1 es verdadero

if (0):
    print("True")  # NO se ejecuta porque 0 es falso

if ("A"):
    print("True")  # Se ejecuta porque "A" es un string no vacío (verdadero)

if (1 or 1):
    print("True")  # Se ejecuta porque 1 or 1 = True (or devuelve True si al menos uno es True)

# SEXTO EJERCICIO: Operador lógico OR con else
# or devuelve True si al menos uno de los operandos es True
# 0 or 0 = False, por lo que se ejecuta el else

if (0 or 0):
    print ("T")  # NO se ejecuta porque 0 or 0 = False
else:
    print("F")   # Se ejecuta porque la condición es falsa

# SÉPTIMO EJERCICIO: Verificación de tipo con tupla
# La sintaxis (a, str) crea una tupla, no una verificación de tipo
# Las tuplas no vacías se consideran True
# Para verificar tipo correctamente se usa isinstance(a, str)

a = "ABC"
if (a, str):
    print ("T")  # Se ejecuta porque la tupla (a, str) no está vacía (verdadera)
else:
    print("F")