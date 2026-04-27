def ingresar_matriz():
  while True:
    try:
     filas = int(input("Ingrese el número de filas: "))
     columnas = int(input("Ingrese el número de columnas: "))
     break
    except ValueError:
      print("Error: Debe ingresar un número entero")
  
  matriz = []
  for i in range(filas): 
    while True: 
      try:
       fila = list(map(float, input(f"Ingrese la fila {i+1} separada por espacios: ").split())) 
       if len(fila) != columnas: 
        print(f"Error: debe ingresar exactamente {columnas} valores.") 
       else: 
        matriz.append(fila) 
        break 
      except ValueError: 
        print("Error: Debe ingresar valores numericos")
  return matriz
  
def mostrar_matriz(A):
  for i in range(len(A)):
   print(A[i])
