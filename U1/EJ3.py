

def imprimir(lista, diccionario):
    print("--- ELEMENTOS DE LA LISTA ---")
    for elemento in lista:
        print(elemento)
        
    print("\n--- ELEMENTOS DEL DICCIONARIO ---")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")



xavi_Lista = [1, 2, 3, 4, 5]
xavi_Dic = {"nombre": "Xavi", "edad": 19, "ciudad": "Cuernavaca"}
imprimir(xavi_Lista, xavi_Dic)