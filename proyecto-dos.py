# Clase 8: Proyecto 2 - Calculadora Simple
# Descripción: Crear una calculadora que pueda sumar, restar, multiplicar y dividir.

def calculadora():
    print("Selecciona operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    eleccion = input("Elige una opción (1/2/3/4): ")
    
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    if eleccion == '1':
        print(f"Resultado: {num1 + num2}")
    elif eleccion == '2':
        print(f"Resultado: {num1 - num2}")
    elif eleccion == '3':
        print(f"Resultado: {num1 * num2}")
    elif eleccion == '4':
        print(f"Resultado: {num1 / num2}")
    else:
        print("Opción no válida")

calculadora()
