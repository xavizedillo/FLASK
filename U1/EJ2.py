def aggDic():
    dic = {}
    cantidad = int(input("¿Cuántos elementos quieres agregar?"))

    for i in range (cantidad):
        clave = input (f"Ingrese la clave {i+1}: ")
        valor = input (f"Ingrese el valor para la '{clave}': ")
        dic[clave] = valor
    
    return dic

xaviDic = aggDic()
print(xaviDic)
