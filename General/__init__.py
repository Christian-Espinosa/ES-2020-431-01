#import API.User as User
#if __name__ == "__main__":
#    pass

import Viaje as Viaje
import Viatgers as Viatgers

lista_Viajes=[]

f = open("DatosViajes.txt")
linea = f.readline()

while (linea != ""):
    if("Viaje:" in linea):

        lista_destinosTemp=[]
        lista_pasajerosTemp=[]
        
        #Viajeros
        
        linea = f.readline()
        Pasajeros=linea
        Pasajeros=Pasajeros.replace('\n','')
        Pasajeros=Pasajeros.replace(' ','')
        Pasajeros=Pasajeros.replace('Pasajeros:','')
        lista_pasajerosTemp=Pasajeros.split(",")
        
        Viatgers_Obj_temp = Viatgers.Viatgers();
        for i in lista_pasajerosTemp:
            i=i.replace('\n','')
            infoPasajerosTemp=i.split("-")
            id_t = infoPasajerosTemp[0]
            nombre_t = infoPasajerosTemp[1]
            apellidos_t = infoPasajerosTemp[2]
            dni_t = infoPasajerosTemp[3]
            edad = infoPasajerosTemp[4]
            Viatgers_Obj_temp.add_viatger(nombre_t,apellidos_t,dni_t,edad)
            
            
            
            
        #Usuario (User)
        
        linea = f.readline()
        Usuario=linea
        Usuario=Usuario.replace('\n','')
        Usuario=Usuario.replace(' ','')
        Usuario=Usuario.replace('Usuario:','')
        
        
        
        
        #Destino
        
        linea = f.readline()
        Destino=linea
        Dest=Destino.replace('Destino:','')
        Dest=Dest.replace('\n','')
        Dest=Dest.replace(' ','')
        lista_destinosTemp.append(Dest.split(","))  
        
        linea = f.readline()
        while ("Destino:" in linea):
            Destino=linea
            Dest=Destino.replace('Destino:','')
			
			#vueloTempD=Flights.getFlight()
            Dest=Dest.replace('\n','')
            Dest=Dest.replace(' ','')
            lista_destinosTemp.append(Dest.split(","))  
			
            #lista_destinosTemp.append(Destino.Destino())
			
            linea = f.readline()

    #self.lista_Viajes.append(User_ini.User_ini(nombre,DNI,calle,tel,email))
        lista_Viajes.append(lista_pasajerosTemp)
        lista_Viajes.append(Usuario)
        lista_Viajes.append(lista_destinosTemp)
        
linea = f.readline()


f.close()

print (lista_Viajes)