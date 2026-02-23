#-------------------------------
# Trabajando con datos strings 
#-------------------------------

#Creacion de variables string
registro_crudo = "   sAnTuaRio de fAuna Y flora iGuaQue   "

#Limpiar el string: eliminar espacios en blanco
registro_sin_espacios = registro_crudo.strip()
print("Registro limpio:", registro_sin_espacios)

# registros sin espacio a formato de titulo
registro_formateado = registro_sin_espacios.title()
print("Registro formateado:", registro_formateado)

# Cambio de Y por y minuscula
registro_final = registro_formateado.replace("Y", "y")
print("Registro final:", registro_final)

# Pequeño reporte con caracteres de escape
reporte = f"Reporte de Limpieza Toponímica:\n\
Registro original:\t{registro_crudo}\n\
Registro limpio:\t\t{registro_sin_espacios}\n\
Registro formateado:\t{registro_formateado}\n\
Registro final:\t\t{registro_final}\n\
Estado:\t\t\tListo para cruce espacial."
print(reporte)

