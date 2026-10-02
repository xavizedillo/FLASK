# Creación de listas en Python
# Una lista es una estructura de datos ordenada y mutable que puede contener elementos de diferentes tipos
colors = ['Azul', 'Verde', 'Rojo', 'Amarillo','Gris']  # Lista de colores
nums = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco']      # Lista de números en texto

# Insertar datos:

# 1. append(): Agrega un solo elemento al final de la lista
# colors.append('Violeta')  # Esto agregaría 'Violeta' al final

# 2. extend(): Agrega múltiples elementos al final de la lista (recibe otra lista)
# colors.extend(['Violeta', 'Naranja'])  # Esto agregaría ambos elementos al final

# 3. insert(): Inserta un elemento en una posición específica
#colors.insert(0, 'Naranja')  # Inserta 'Naranja' en la posición 0 (al inicio)





# ELIMINAR DATOS DE LISTAS:

# 1. pop(): Elimina y retorna el último elemento de la lista por defecto
# Útil cuando necesitas obtener el elemento eliminado para usarlo posteriormente
#salida = colors.pop()  # Elimina el último elemento ('Gris') y lo guarda en 'salida'
#print (salida)          
#print (colors)         

# 2. pop(indice): Elimina y retorna el elemento en una posición específica
#salida = colors.pop(1)  # Elimina el elemento en la posición 1 ('Verde') - COMAND
#print (salida)          
#print (colors)          

# 3. clear(): Elimina todos los elementos de la lista, dejándola vacía
# Útil cuando necesitas reutilizar la misma lista sin crear una nueva
#colors.clear()  - COMANDO       
#print (colors)          




# ORDENAR LISTAS:

# 1. sort(reverse=True): Ordena la lista en orden descendente (de mayor a menor)
# Modifica la lista original (no crea una nueva)
#colors.sort(reverse=True)  # Ordena: ['Verde', 'Rojo', 'Gris', 'Azul', 'Amarillo']
#print(colors)

# 2. sort(reverse=False): Ordena la lista en orden ascendente (de menor a mayor)
# Es el comportamiento por defecto de sort()
#colors.sort(reverse=False) # Ordena: ['Amarillo', 'Azul', 'Gris', 'Rojo', 'Verde']
#print(colors)

# 3. reverse(): Invierte el orden de los elementos de la lista
# No ordena alfabéticamente, solo invierte la posición actual
#colors.reverse()           # Invierte: ['Gris', 'Amarillo', 'Rojo', 'Verde', 'Azul']
#print(colors)
    

# COPIAR Y ANIDAR LISTAS:

# copy(): Crea una copia superficial de la lista
# Importante: la copia es independiente de la original, modificar una no afecta a la otra
#copy0fcolors = colors.copy()  # Crea una copia independiente de colors

# Las listas pueden contener otras listas (listas anidadas)
# Esto permite estructuras de datos más complejas
#colors.append([[1], [1,2,3,4]])  # Agrega una lista que contiene dos listas

#print(colors)         # Muestra la lista original con la lista anidada agregada
#print(copy0fcolors)   # Muestra la copia sin la modificación (demuestra que son independientes)






#for num in nums:
 #   print (num)

for num in nums:
    if (num == 'Cinco'):
       nums[4] = 5
        
print(nums)