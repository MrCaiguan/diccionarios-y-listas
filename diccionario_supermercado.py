supermercado={}
producto=None
while producto!="":
    producto=input("ingrese nombre del producto (ENTER, para finalizar) : ")
    if producto=="":
        break
    cantidad=int(input("Ingrese cantidad del producto : "))
    supermercado[producto]=cantidad
x=int(input("Ingrese numero para multiplicar cantidad de producto : "))
print("Lista del supermercado : ")
for producto, cantidad in supermercado.items():
    multiplicado= cantidad*x
    print(f"{producto} y su  cantidad es: {multiplicado}")
