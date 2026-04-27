from proyecto_matrices.entrada import ingresar_matriz, mostrar_matriz
from proyecto_matrices.menu import mostrar_menu
from proyecto_matrices.operaciones_matrices import (
    sumar_matrices,
    multiplicacion_matrices,
    productohadamard_matrices,
    productokronecker_matrices)

def ejecutar_programa():
    while True:
        opcion = mostrar_menu()

        if opcion == 5: # Salir
            print("¡Hasta luego!")
            break

        print("Datos para la Matriz A:")
        A = ingresar_matriz()

        if opcion == 1: # Suma de matrices
            print("Datos para la Matriz B (debe ser del mismo tamaño que A):")
            B = ingresar_matriz()
            resultado = sumar_matrices(A, B)
            print("\nResultado de la Suma:")
            mostrar_matriz(resultado)

        elif opcion == 2: # Multiplicación de matrices
            print("Datos para la Matriz B (filas de B deben ser iguales a columnas de A):")
            B = ingresar_matriz()
            resultado = multiplicacion_matrices(A, B)
            print("\nResultado de la Multiplicación:")
            mostrar_matriz(resultado)

        elif opcion == 3: # Producto de Hadamard
            print("Datos para la Matriz B (mismo tamaño que A):")
            B = ingresar_matriz()
            resultado = productohadamard_matrices(A, B)
            print("\nResultado del Producto de Hadamard:")
            mostrar_matriz(resultado)

        elif opcion == 4: # Producto de Kronecker
            print("Datos para la Matriz B:")
            B = ingresar_matriz()
            resultado = productokronecker_matrices(A, B)
            print("\nResultado del Producto de Kronecker:")
            mostrar_matriz(resultado)

