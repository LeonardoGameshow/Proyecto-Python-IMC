# Nombre del programa: Calculadora de IMC
# Repositorio en GitHub: https://github.com/LeonardoGameshow/Proyecto-Python-IMC

print("=== CALCULADORA DE IMC ===")
print("Bienvenido al registro de usuarios\n")

# --- Validaciones de Nombres y Apellidos ---
nombre_usuario = input("Ingresa tu nombre: ").strip()
while nombre_usuario == "":
    print(" Error: Este campo no puede quedar vacío.")
    nombre_usuario = input("Ingresa tu nombre: ").strip()

apellido_paterno = input("Ingresa tu apellido paterno: ").strip()
while apellido_paterno == "":
    print(" Error: Este campo no puede quedar vacío.")
    apellido_paterno = input("Ingresa tu apellido paterno: ").strip()

apellido_materno = input("Ingresa tu apellido materno: ").strip()
while apellido_materno == "":
    print(" Error: Este campo no puede quedar vacío.")
    apellido_materno = input("Ingresa tu apellido materno: ").strip()


# --- Validación de Edad (Número entero positivo) ---
edad_input = input("Ingresa tu edad: ").strip()
while edad_input == "" or not edad_input.isdigit() or int(edad_input) <= 0:
    if edad_input == "":
        print(" Error: El campo de edad no puede quedar vacío.")
    else:
        print(" Error: Debes ingresar una edad válida en números (ej. 24).")
    edad_input = input("Ingresa tu edad: ").strip()

edad = int(edad_input)


# --- Validación de Peso (Número con o sin decimales) ---
peso_input = input("Ingresa tu peso en kg (ej. 70.5): ").strip()
# .replace(".", "", 1) quita el punto decimal solo una vez para verificar si el resto son números
while peso_input == "" or not peso_input.replace(".", "", 1).isdigit() or float(peso_input) <= 0:
    if peso_input == "":
        print(" Error: El campo de peso no puede quedar vacío.")
    else:
        print(" Error: Ingresa un peso válido en números (ej. 68.5).")
    peso_input = input("Ingresa tu peso en kg (ej. 70.5): ").strip()

peso = float(peso_input)


# --- Validación de Estatura (Número decimal en metros) ---
estatura_input = input("Ingresa tu estatura en metros (ej. 1.75): ").strip()
while estatura_input == "" or not estatura_input.replace(".", "", 1).isdigit() or float(estatura_input) <= 0:
    if estatura_input == "":
        print(" Error: El campo de estatura no puede quedar vacío.")
    else:
        print(" Error: Ingresa una estatura válida en números (ej. 1.75).")
    estatura_input = input("Ingresa tu estatura en metros (ej. 1.75): ").strip()

estatura = float(estatura_input)


# --- Cálculo y despliegue del IMC ---
IMC = peso / (estatura ** 2)

print("\n" + "="*40)
print(f"Hola {nombre_usuario.capitalize()} {apellido_paterno.capitalize()} {apellido_materno.capitalize()} con edad de {edad} años.")
print(f"Tu Índice de Masa Corporal (IMC) es: {IMC:.2f}")
print("="*40)

input("\nPresiona Enter para salir...")