#import API.User as User
#if __name__ == "__main__":
#    pass

lista_Viajes=[]

f = open("DatosViajes.txt")
linea = f.readline()

while (linea != ""):
    if("Viaje:" in linea):

        lista_destinosTemp=[]
        lista_pasajerosTemp=[]
        
        linea = f.readline()
        Pasajeros=linea
        Pasajeros=Pasajeros.replace('\n','')
        Pasajeros=Pasajeros.replace(' ','')
        Pasajeros=Pasajeros.replace('Pasajeros:','')
        lista_pasajerosTemp=Pasajeros.split(",")
        
        linea = f.readline()
        Usuario=linea
        Usuario=Usuario.replace('\n','')
        Usuario=Usuario.replace(' ','')
        Usuario=Usuario.replace('Usuario:','')
        
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