import sys


if len(sys.argv) == 3:
    nota1 = float(sys.argv[1])
    nota2 = float(sys.argv[2])
    
    if nota1>=7 and nota2>=7:
        print("Promocionado")
    elif nota1>=4 and nota2>=4:
        print("Aprobado")
    elif (nota1<4 or nota2<4) and (not (nota1<4 and nota2<4)):
        if nota1<4:
            print("recupera el primer parcial")
        else:
            print("recupera el segundo parcial")
    else:
        print("desaprobo los 2 parciales")
else:
    print("Error, debe ingresar 2 notas")