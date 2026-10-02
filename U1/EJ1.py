def agg():
    cantidad = int(input("¿Cuántos elementos quieres agregar? "))
    lista = []
    for i in range(cantidad):
        elemento = input(f"Ingrese el elemento {i+1}: ")
        lista.append(elemento)
    return lista    



xavi_lista = agg()
print(xavi_lista)
