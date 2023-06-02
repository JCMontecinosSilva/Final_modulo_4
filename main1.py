from clases import Vehiculo, Automovil

instancias=[]

n = int(input("Cuantos Vehiculos desea insertar: ")) #Input hace que aparezca mensaje pidiendo datos

for i in range(n):
    print(f"Datos del automovil {i+1} ")
    marca= input ("Inserte la marca del automóvil: ")
    modelo= input ("Inserte el modelo del automóvil: ")
    nroruedas= int (input("Inserte el número de ruedas del automóvil: "))
    velocidad = int (input("Inserte la velocidad en km/h: "))
    cilindrada= int (input("Inserte el cilindraje en cc: "))
    print("")
    auto=Automovil(marca,modelo,nroruedas,velocidad,cilindrada)
    instancias.append(auto)
    
print("Imprimiendo por pantalla los Vehiculos: ")

for index,item in enumerate(instancias):
    print(f"Datos del automovil {index + 1} : Marca {item.marca}, Modelo {item.modelo}, {item.nroruedas} ruedas, {item.velocidad} Km/h, {item.cilindrada} cc")
    
