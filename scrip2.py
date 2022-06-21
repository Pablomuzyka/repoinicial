import sys

#realizar un scrip que imprima una palabra una cant de veces determinada
#imprima hola 5


if len(sys.argv) != 3 :
    print("error, necesito 2 argumentos")
else :
    for i in range (int(sys.argv[2])):
        print(sys.argv[1])

#[nombresscrip,parametro1,parametro2]            

