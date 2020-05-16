#import API.User as User
#if __name__ == "__main__":
#    pass


from General.Viaje import Viaje as Viaje
from General.Viatgers import Viatgers as Viatgers
from General.Destinos import Destinos as Destinos



lista_Viajes=[]

f = open("DatosViajes.txt")
linea = f.readline()


while (linea != ""):
    if("Viaje:" in linea):
        
        id_viaje_t=linea
        id_viaje_t=id_viaje_t.replace('Viaje: ','')
        id_viaje_t=id_viaje_t.replace('\n','')
        
        lista_destinosTemp=[]
        lista_pasajerosTemp=[]
        
        #Viajeros OBJ
        
        linea = f.readline()
        Pasajeros=linea
        Pasajeros=Pasajeros.replace('\n','')
        Pasajeros=Pasajeros.replace(' ','')
        Pasajeros=Pasajeros.replace('Pasajeros:','')
        lista_pasajerosTemp=Pasajeros.split(",")
        
        Viatgers_Obj_temp = Viatgers()
        for i in lista_pasajerosTemp:
            infoPasajerosTemp=i.split("-")
            id_t = infoPasajerosTemp[0]
            nombre_t = infoPasajerosTemp[1]
            apellidos_t = infoPasajerosTemp[2]
            dni_t = infoPasajerosTemp[3]
            edad = infoPasajerosTemp[4]
            Viatgers_Obj_temp.add_viatger(nombre_t,apellidos_t,dni_t,edad)
            
            
            
            
        #Usuario (User) ID ONLY
        
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
			
            Dest=Dest.replace('\n','')
            Dest=Dest.replace(' ','')
            lista_destinosTemp.append(Dest.split(","))  
						
            linea = f.readline()

    
        Destinos_Obj_temp = Destinos()
        for j in lista_destinosTemp:
            id_destino_t = j[0]
            id_vuelo_t = j[1]
            id_hotel_t = j[2]
            
            Destinos_Obj_temp.add_destino(id_destino_t,id_vuelo_t,id_hotel_t)
            if(len(j)==4):
                id_coche_t = j[3]
                Destinos_Obj_temp.set_vehiculo(id_coche_t)
            
    
        lista_Viajes.append(Viaje(id_viaje_t,Viatgers_Obj_temp,Destinos_Obj_temp,Usuario))
        

linea = f.readline()


f.close()

for x in lista_Viajes:    
    print (x.get_id_viaje())
    print (x.get_id_user())
    print (x.get_precio())
    print (x.get_viatgers())
    for xx in x.get_destinos():
        print(xx.get_id())
        print(xx.get_vuelo())
        print(xx.get_hotel())
        print(xx.get_vehiculo())
    print ("\n")