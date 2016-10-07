import csv

print'menu de opciones'
print'1.- Leer'
print'2.- Incertar'
print'3.-salir'
op = raw_input("elige una opcion: ") 

if op=='1': 
      print "La lista contiene los sigientes valores"
      with open('data.csv','r')as file:
          data=csv.reader(file,delimiter='|')
          for line in data:
              print line
elif op=='2':
    print 'Incertar un nuevo valor'
    nombre = raw_input("Cual es el nombre: \n")
    emal = raw_input("Cual es su E-mail:\n")
    telefono = raw_input("cual es su telefono:\n")
    with open('data.csv','a')as file:
        data=csv.writer(file,delimiter='|')
        data.writerow([nombre,emal,telefono])
        
        print 'Dato agregado verificar los datos'
else:
    print'Saliste del sistema'
