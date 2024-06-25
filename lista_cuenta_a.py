lista=[]
palabra=input("Ingrese una palabra (ENTER, para finalizar) :")
while palabra!="":
    lista.append(palabra)
    palabra=input("Ingrese una palabra (ENTER, para finalizar):")
    
print("lista de palabras :")
print(lista)
def contador_a(palabra):
    contar_a=0
    for letra in palabra.lower():
        if letra == "a":
            contar_a+= 1
    return contar_a
print("lista de palabras y conteo")
for palabra in lista:
    a = contador_a(palabra)
    print(f"{palabra} tiene {a} a")

