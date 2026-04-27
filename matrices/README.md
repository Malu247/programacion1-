PROYECTO DE MATRICES - PROGRAMACION 1
Este proyecto en Python utiliza modulos para desarollar operaciones matriciales. El codigo permite realizar calculos (Suma, Multiplicación, Hadamard y Kronecker) entre matrices ingresadas por el usuario. El programa se divide en cuatro modulos principales:

main.py
Ejecuta el programa principal, donde se importan los modulos con sus funciones, se gestiona el flujo y se presenta el menu para elegir que operacion ejecutar segun lo elegido por el usuario.

entrada.py
Solicita los datos de la matriz (numero de filas y columnas) y pide ingresar cada elemento de la matriz. El programa permite errores al mmento de ingresar los numeros y no se termina.

operaciones_matrices.py
Se definen las funciones con los algoritmos para la suma, la multiplicacion, el producto de Hadamard y el producto Kronecker. Algunas operaciones presentan limitaciones (como el mismo numero de filas) con el fin de que se puedan realizar de manera correcta.

menu.py
Se estructura la interfaz visual del menu donde se exponen las opciones disponibles para que el ususario elija la operacion que desea realizar. Este vuelve a aparecer despues de que se termine de ejecutar la opcion ingresada. 

INSTRUCCIONES DE EJECUCION
Para correr el programa, el usuario debe contar con un intérprete de Python instalado en su sistema. El primer paso es abrir una terminal y dirigirse al directorio donde se encuentran alojados los archivos. Despues, se debe ejecutar el archivo principal utilizando el comando python main.py .
Al iniciar, el programa mostrara un menu con cinco opciones numeradas. El usuario simplemente debe ingresar el numero correspondiente a la operacion que desea realizar. El sistema le solicitara las dimensiones y los elementos de las matrices necesarias, validando en cada paso que la información sea correcta. Al finalizar una operacin, el programa mostrara el resultado y regresara automaticamente al menu principal. Para cerrar el programa, el usuario solo debe seleccionar la opcion número 5.

NOMBRE: Maria Lucia Higuera Angarita
INSTITUCION: Universidad Industrial de Santander
