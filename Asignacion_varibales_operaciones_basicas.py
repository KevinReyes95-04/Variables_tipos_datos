#-------------------------------
# Taller: Variables, tipos de datos y operaciones básicas
#-------------------------------

#Asignación de variables
Nombre_estacion = "Páramo_de_Santurbán"
Latitud = 7.2514
Longitud = -72.9069
Elevación_metros = 3350
Esta_activa = True
print(Nombre_estacion, Latitud, Longitud, Elevación_metros, Esta_activa)


#Creacion de lista de variables
Variables_estacion = [Nombre_estacion, Latitud, Longitud, Elevación_metros, Esta_activa]
print(Variables_estacion)

#Creacion de diccionario de variables
metadatos_estacion = {
    "Nombre": Nombre_estacion,
    "Coordenadas": [Latitud, Longitud],  # Lista (Base 0)
    "Elevación_metros": Elevación_metros,
    "Esta_activa": Esta_activa
}

print(metadatos_estacion)


#Estraccion de informacion: Longitud
Longitud_estacion = metadatos_estacion["Coordenadas"][1]
print("La longitud de la estación es:", Longitud_estacion)

# Elavacion subio 12.25 metros
Elevacion_actualizada = Elevación_metros + 12.25
print("La elevación actualizada de la estación es:", Elevacion_actualizada)

#Mensaje dinamico usando la interpolacion de texto 
Mensaje = f"La estación {Nombre_estacion} se encuentra operativa en la longitud {Longitud_estacion} y latitud {Latitud} a una altura actualizada de {Elevacion_actualizada} msnm."
print(Mensaje)
