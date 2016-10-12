import csv
def __init__():
    print 'Elaborado por: Francisco Javier Heredia Tellez'
def hacer_a():
    print "Datos registrados \n"
    with open('data.csv','r')as file:
        data=csv.reader(file,delimiter='|')
        for line in data:
            print line
def haser_b():
    print 'Ingresa nuevo valor \n'
    nombre = raw_input("Cual es el nombre: \n")
    emal = raw_input("Cual es su E-mail:\n")
    telefono = raw_input("cual es su telefono:\n")
    with open('data.csv','a')as file:
        data=csv.writer(file,delimiter='|')
        data.writerow([nombre,emal,telefono])
        print 'Dato agregado verificar los datos'    

def haser_c():
    print 'Deseas salir preciona 3:\n'
def menu():
    op=0
    while(op!=4):
        print'1.- Leer'
        print'2.- Incertar'
        print'3.- Salir'
        op = int (raw_input("Elige una de las opcion: "))
        if(op==1):
            hacer_a()
            haser_c()
        if(op==2):
            haser_b()
            haser_c()
        if (op==3):
            __init__()
            print 'Saliste del sistema'
            break
            
menu()
