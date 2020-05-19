#import API.User as User
#if __name__ == "__main__":
#    pass


#import Viaje
#import Viatgers
#import Destinos

#import API.User as User
#if __name__ == "__main__":
#    pass


from Viaje import Viaje
from Viatgers import Viatgers
from Destinos import Destinos

from API.Coche import Rentalcars as Rentalcars
from API.Airhopping import Booking as Booking
from API.Vuelos import Skyscanner as Skyscanner

from API.Vuelos import Flights as Flights
from API.Airhopping import Hotels as Hotels
from API.Coche import Cars as Cars

from API.Airhopping import User as User

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

        User_Obj_temp = User.User()
        Usuario_Obj_temp = User_Obj_temp.getDatosUser(Usuario)


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
            t_hotel_t = j[2]

            t_hotel_t.split("-")

            id_hotel_t = t_hotel_t[0]
            dias_hotel_t = t_hotel_t[1]
            numHab_hotel_t = t_hotel_t[2]
            numHostes_hotel_t = t_hotel_t[3]

            sc_dic=Skyscanner.Skyscanner().buscar_vuelo(id_vuelo_t)
            v_obj_t=Flights.Flights(sc_dic[0],sc_dic[2])#id, precio

            bk_dic=Booking.Booking().buscar_hotel(id_hotel_t)
            h_obj_t=Hotels.Hotels(dias_hotel_t, id_hotel_t, numHab_hotel_t, numHostes_hotel_t, bk_dic[1])
            h_obj_t.setPrecio(bk_dic[2])#precio

            #Destinos_Obj_temp.add_destino(id_destino_t,id_vuelo_t,id_hotel_t)
            Destinos_Obj_temp.add_destino(id_destino_t,v_obj_t,h_obj_t)
            if(len(j)==4):
                t_coche_t = j[3]

                t_coche_t.split("-")

                id_coche_t = t_coche_t[0]
                dias_coche_t = t_coche_t[1]

                car_dic=Rentalcars.Rentalcars().buscar_coche(id_coche_t)

                precio_coche_t = car_dic[2]

                car_obj_t=Cars.Cars(id_coche_t, precio_coche_t, dias_coche_t)

                if Destinos_Obj_temp.get_destino(id_destino_t) != None:
                    Destinos_Obj_temp.get_destino(id_destino_t).set_vehiculo(car_obj_t)


        lista_Viajes.append(Viaje(id_viaje_t,Viatgers_Obj_temp,Destinos_Obj_temp,Usuario_Obj_temp))


linea = f.readline()


f.close()

for x in lista_Viajes:
    print (x.get_id_viaje())
    print (x.get_user())
    print (x.get_precio())
    print (x.get_viatgers())
    for xx in x.get_destinos():
        print(xx.get_id())
        print(xx.get_vuelo())
        print(xx.get_hotel())
        print(xx.get_vehiculo())
    print ("\n")

#
# lista_Viajes=[]
#
# f = open("DatosViajes.txt")
# linea = f.readline()
#
#
# while (linea != ""):
#     if("Viaje:" in linea):
#
#         id_viaje_t=linea
#         id_viaje_t=id_viaje_t.replace('Viaje: ','')
#         id_viaje_t=id_viaje_t.replace('\n','')
#
#         lista_destinosTemp=[]
#         lista_pasajerosTemp=[]
#
#         #Viajeros OBJ
#
#         linea = f.readline()
#         Pasajeros=linea
#         Pasajeros=Pasajeros.replace('\n','')
#         Pasajeros=Pasajeros.replace(' ','')
#         Pasajeros=Pasajeros.replace('Pasajeros:','')
#         lista_pasajerosTemp=Pasajeros.split(",")
#
#         Viatgers_Obj_temp = Viatgers.Viatgers()
#         for i in lista_pasajerosTemp:
#             infoPasajerosTemp=i.split("-")
#             id_t = infoPasajerosTemp[0]
#             nombre_t = infoPasajerosTemp[1]
#             apellidos_t = infoPasajerosTemp[2]
#             dni_t = infoPasajerosTemp[3]
#             edad = infoPasajerosTemp[4]
#             Viatgers_Obj_temp.add_viatger(nombre_t,apellidos_t,dni_t,edad)
#
#
#
#
#         #Usuario (User) ID ONLY
#
#         linea = f.readline()
#         Usuario=linea
#         Usuario=Usuario.replace('\n','')
#         Usuario=Usuario.replace(' ','')
#         Usuario=Usuario.replace('Usuario:','')
#
#
#
#
#         #Destino
#
#         linea = f.readline()
#         Destino=linea
#         Dest=Destino.replace('Destino:','')
#         Dest=Dest.replace('\n','')
#         Dest=Dest.replace(' ','')
#         lista_destinosTemp.append(Dest.split(","))
#
#
#
#         linea = f.readline()
#         while ("Destino:" in linea):
#             Destino=linea
#             Dest=Destino.replace('Destino:','')
#
#             Dest=Dest.replace('\n','')
#             Dest=Dest.replace(' ','')
#             lista_destinosTemp.append(Dest.split(","))
#
#             linea = f.readline()
#
#
#         Destinos_Obj_temp = Destinos.Destinos()
#         for j in lista_destinosTemp:
#             id_destino_t = j[0]
#             id_vuelo_t = j[1]
#             id_hotel_t = j[2]
#
#             Destinos_Obj_temp.add_destino(id_destino_t,id_vuelo_t,id_hotel_t)
#             if(len(j)==4):
#                 id_coche_t = j[3]
#                 if Destinos_Obj_temp.get_destino(id_destino_t) != None:
#                     Destinos_Obj_temp.get_destino(id_destino_t).set_vehiculo(id_coche_t)
#
#
#         lista_Viajes.append(Viaje.Viaje(id_viaje_t,Viatgers_Obj_temp,Destinos_Obj_temp,Usuario))
#
#
# linea = f.readline()
#
#
# f.close()
#
# for x in lista_Viajes:
#     print (x.get_id_viaje())
#     print (x.get_id_user())
#     print (x.get_precio())
#     print (x.get_viatgers())
#     for xx in x.get_destinos():
#         print(xx.get_id())
#         print(xx.get_vuelo())
#         print(xx.get_hotel())
#         print(xx.get_vehiculo())
#     print ("\n")
