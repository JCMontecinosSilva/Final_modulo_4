import csv

class Vehiculo():
    def __init__(self,marca,modelo,nroruedas):
        self.marca =marca
        self.modelo = modelo
        self.nroruedas= nroruedas
    
   
    
    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv","a",newline="") as archivo:
                datos=[(self.__class__,self.__dict__)]
                archivo_csv= csv.writer(archivo)
                archivo_csv.writerows(datos)                
        except FileNotFoundError:
            print("No existe el archivo vehiculo.csv")
        except Exception as e:
            print ("Error reportado: ",e)
            
    def leer_datos_csv(self):
        try:
            with open("vehiculo.csv","r") as archivo:
                vehiculos=csv.reader(archivo)
                print(f"Lista de Vehiculos {type(self).__name__}")
                
                for item in vehiculos:
                    vehiculo_tipo= str(self.__class__)
                    if vehiculo_tipo in item[0]:
                        print(item[1])
                print("")                         
        except FileNotFoundError:
            print("No existe el archivo vehiculo.csv")
        except Exception as e:
            print ("Error reportado: ",e)
    
            
    
class Automovil(Vehiculo):
    def __init__(self,marca,modelo,nroruedas, velocidad,cilindrada ):
        super().__init__(marca,modelo,nroruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return Vehiculo().__str__(self) + f" {self.velocidad} Km/h, {self.cilindrada} cc"
    

    
class Particular(Automovil):
    def __init__(self,marca,modelo,nroruedas, velocidad,cilindrada,nropuestos):
        super().__init__(marca,modelo,nroruedas,velocidad,cilindrada)
        self.nropuesto = nropuestos
        
    def get_nropuestos(self):
        return self.nropuesto
            
    def set_nropuestos(self,nropuesto_new):
        self.nropuesto=nropuesto_new  
          
    def __str__(self):
        return Automovil().__str__(self) + f" Puestos: {self.nropuesto}"



class Carga(Automovil):
    def __init__(self,marca,modelo,nroruedas, velocidad,cilindrada,capcarga):
        super().__init__(marca,modelo,nroruedas,velocidad,cilindrada)
        self.capcarga = capcarga
        
    def get_capcarga(self):
        return self.capcarga
            
    def set_capcarga(self,capcarga_new):
        self.capcarga=capcarga_new  
          
    def __str__(self):
        return Automovil().__str__(self) + f" Capacidad de carga {self.capcarga} kilos"
    
    

class Bicicleta(Vehiculo):
    def __init__(self,marca,modelo,nroruedas,tipo):
        super().__init__(marca,modelo,nroruedas)
        self.tipo=tipo
        
    def __str__(self):
        return Vehiculo.__str(self + f" tipo: {self.tipo}")
    
class Motocicleta (Bicicleta):
    def __init__(self, marca, modelo, nroruedas, tipo, nroradio, cuadro, motor):
        super().__init__(marca, modelo, nroruedas, tipo)
        self.nroradio=nroradio
        self.cuadro=cuadro
        self.motor=motor
                              
    def get_nroradio(self):
            return self.nroradio
        
    def get_cuadro(self):
            return self.cuadro
        
    def get_motor(self):
            return self.motor
        
    def set_nroradio(self,nroradio_new): 
        self.nroradio = nroradio_new
     
    def set_cuadro(self,cuadro_new):    
        self.cuadro = cuadro_new
        
    def set_motor(self,motor_new):
        self.motor = motor_new
          
    def __str__(self):
        return Bicicleta().__str__(self) + f"{self.nroradio},{self.cuadro},{self.motor}"
          