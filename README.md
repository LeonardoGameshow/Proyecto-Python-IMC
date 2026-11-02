# Calculadora de Índice de Masa Corporal (IMC)

Programa interactivo desarrollado en Python para calcular el Índice de Masa Corporal (IMC) de un usuario a partir de sus datos personales y antropométricos, asegurando la robustez y la validación estricta de las entradas.

---

## Descripción del Programa

La **Calculadora de IMC** recopila de forma segura el nombre completo, la edad, el peso y la estatura de un usuario. A partir de estos datos, procesa la información aplicando la fórmula estándar del Índice de Masa Corporal:

IMC = peso / (estatura ^ 2)

### Características principales:
- **Validación anti-campos vacíos:** Utiliza el método `.strip()` para evitar que el programa avance si el usuario presiona Enter sin ingresar datos o deja espacios en blanco.
- **Prevención de colapsos (Crashes):** Implementa validaciones lógicas mediante métodos de cadenas como `.isdigit()` y control de puntos decimales para asegurar que los datos numéricos sean correctos antes de realizar conversiones de tipo (`int` o `float`).
- **Control de rangos lógicos:** Verifica que los valores numéricos ingresados sean estrictamente mayores a cero.
- **Formato limpio y amigable:** Capitaliza automáticamente los nombres y muestra el resultado del IMC redondeado a dos decimales.

---

## Instrucciones de Ejecución

### Requisitos previos
- Tener instalado **Python 3.x** en tu sistema.

### Pasos para ejecutar:
1. Clona este repositorio o descarga el archivo `calculadora_imc.py`:
   git clone [https://github.com/LeonardoGameshow/Proyecto-Python-IMC.git](https://github.com/LeonardoGameshow/Proyecto-Python-IMC.git)

Reflexión Personal Proyecto U-camp
Durante el desarrollo de este proyecto, profundicé en la importancia de diseñar software robusto que no falle ante el comportamiento
impredecible del usuario. Al enfrentar el reto de evitar que el programa colapsara con entradas erróneas, investigué y estructuré una forma más eficiente de
validar la información utilizando bucles while, condicionales if y métodos nativos de manipulación de cadenas en Python (como .strip() y .isdigit()).
Este proceso me permitió comprender que un buen programa no solo debe resolver un problema matemático, sino también guiar al usuario de manera amigable,
validando cada entrada para garantizar la estabilidad y confiabilidad del sistema desde las bases de la programación estructurada.
