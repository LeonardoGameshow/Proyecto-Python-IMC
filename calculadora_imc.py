#Nombre del programa: calculadora de IMC
# Repositorio en GitHub: https://github.com/LeonardoGameshow/Proyecto-Python-IMC

print("=== CALCULADORA DE IMC ===")

print("Bienvenido al registro de usuarios")

nombre_usuario = input("Ingresa tu nombre: ")
apellido_paterno = input("Ingresa tu apellido paterno: ")
apellido_materno = input("Ingresa tu apellido materno: ")
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso: "))
estatura = float(input("Ingresa tu estatura: "))

# Aplicación de la fórmula del IMC
IMC = peso/(estatura)**2

# Casting de calculo de IMC
print(f"Hola {nombre_usuario.capitalize()} {apellido_paterno.capitalize()} {apellido_materno.capitalize()} con edad de {edad} años, tu indice de masa es: {IMC:.2f}")

input("\nPresiona Enter para salir...")
