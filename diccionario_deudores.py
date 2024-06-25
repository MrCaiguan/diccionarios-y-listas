deudores={}
print("Ingrese rut y deuda de 5 personas")
for x in range(5):
    rut=input("Ingrese rut de la persona : ")
    deuda=int(input("Ingrese deuda de la persona : "))
    deudores[rut]=deuda

while True:
    rut=input("Ingrese rut de la persona para abonar  : ")
    if rut=="":
        break

    if rut in deudores:
        abonar=int(input(f"Ingrese monto que desea abonar a {rut}"))
        if abonar>=deudores[rut]:
            del deudores[rut]
        else:
            deudores[rut]=deudores[rut]-abonar
    

print("personas deudoras y saldos de deuda")
for rut, saldo in deudores.items():
    print(f"persona: {rut} - saldo de deuda: {saldo}")   