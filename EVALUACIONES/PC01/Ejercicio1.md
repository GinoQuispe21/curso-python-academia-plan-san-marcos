## Gestor de empleados

Pepito, el propietario de una pollería, se ha dado cuenta de que necesita una forma más eficiente de mantener un registro de sus empleados y sus salarios. Él requiere sus servicios como desarrollador de software para que lo apoye creando un programa que le permita ingresar y actualizar la información de sus empleados de manera fácil y segura.

### Definamos el programa:

#### 1. Ingreso de datos del usuario

El usuario de su programa debe poder registrar empleados la cantidad de veces que el usuario lo requiera. Los datos que debe pedir para el registro de cada empleado son: id, nombre completo, DNI, teléfono, tiempo trabajando y cargo. (Recomendación: usar un diccionario anidado a la llave id para guardar la información del usuario en el diccionario: registro_empleados). Además, agregar el salario del empleado según el cargo que se introdujo en el registro, es decir, la información salarial no es un dato de entrada para el usuario, este se agregará dependiendo del cargo, el cual si es un dato de entrada. Estos son los salarios que paga Pepito por el tipo de cargo en la pollería a sus trabajadores:

|     Cargo     |    Salario    |
|---------------|-------------- |
| Limpieza      | S/ 1,025      |
| Mesero        | S/ 1,500      |
| Cajero        | S/ 1,500      |
| Vigilante     | S/ 1,400      |
| Gerente       | S/ 2,500      |

La solicitud de datos debe verse de esta manera:

```
Creando un nuevo usuario:
- Id: 1
- Nombre completo: Gino Quispe Calixto
- Dni: 74275222
- Telefono: 976903370
- Tiempo trabajando (meses): 7
- Cargo: cajero
```

Para detener la solicitud de datos del empleado al usuario, el programa posterior a un registro debe preguntar al usuario si desea ingresar un nuevo empleado, permitiéndole escribir si o no según la opción que decida. Si el usuario escribe Si, se volverá a mostrar el mensaje de registro de empleado solicitando los datos correspondientes. Por otro lado, si el usuario marca no, se terminara el registro de empleados y el programa procederá a mostrar el meú principal. 
NOTA: Las selección de una opción no deben verse afectadas por mayusculas o minúsculas en la respuesta del usuario. Ademas, debe mostrar dicho mensaje de esta manera:

```
> Quiere ingresar un nuevo empleado al registro? (Si/ No)
```

#### 2. Mostrar menú del gestor de empleados

Posterior al culminar la solicitud de datos de su programa al usuario, debe mostrar un menú con 4 opciones. El menú deberá mostrarse de esta manera:

```
====================== Gestion de Empleados ========================
|| 1. Visualizar informacion de un empleado.                      ||
|| 2. Mostrar empleado cuyo tiempo en la empresa sea el menor     ||
|| 3. Actualizar salario de un empleado                           ||
|| 4. Terminar programa                                           ||
====================================================================
```

El usuario debe poder ingresar el número de la opción que desee realizar, para ello debes pedirle como un input su respuesta, manejando una gestión de excepciones por si el usuario se equivoca al ingresar su opción. Puedes usar este mensaje para leer la información del usuario:

```
> Elija la opcion que desee realizar (1/2/3/4): 
```

Además, si el usuario ingresa una opción valida, se ejecuta la acción solicitada (se indica en los siguientes puntos) y cuando se culmine la funcionalidad solicitada, se debe volver a mostrar el mensaje pidiéndole al usuario que seleccione una opción a realizar. El programa solo termina si el usuario selecciona la cuarta opción.

#### 3. Visualizar información del empleado

Define una función visualizar_informacion_empleado donde se le solicite al usuario ingresar el id del empleado a ser buscado, la solicitud podría verse de esta manera:

```
>>> ========== Visualizar Información ==========
>>> Ingrese el Id del empleado: 1
```

Si el usuario ingresa un valor incorrecto, muestre un mensaje de error realizando gestión de excepciones. Posterior a la validación del input, la función debe mostrar en pantalla la información del usuario, usted decida como es la mejor manera de mostrar la información del usuario. Además, si no se encuentra un empleado con el id ingresado en el diccionario registro_empleados, debe mostrar un mensaje como output al usuario, puede usar este mensaje:

```
>>> Lo sentimos, no se encontró un empleado con ese Id.
```

#### 4. Mostrar empleado o empleados cuyo tiempo en la empresa sea el menor

Define una función mostrar_empleado_minimo_tiempo, donde se calcule cual es el empleado o los empleados con el menor tiempo en la empresa. El resultado debería verse de una de estas maneras, dependiendo si solo es un empleado cuyo tiempo es el menor, o si son más de un empleado los que tienen el menor tiempo en la empresa:

```
>>> ========== Empleado con menor tiempo en la empresa ==========
>>> Id: 1
>>> Nombre: Gino Quispe Calixto
>>> Tiempo trabajando (meses): 7
```

```
>>> ========== Empleados con menor tiempo en la empresa ==========
>>> Id: 1
>>> Nombre: Gino Quispe Calixto
>>> Tiempo trabajando (meses): 7
>>> Id: 2
>>> Nombre: Italo Sabrera Paucar
>>> Tiempo trabajando (meses): 7
```

RECOMENDACIÓN: Cree un diccionario auxiliar que le ayude a almacenar directamente como llave el Id del empleado y su valor sea la horas trabajadas, posterior puede usar los métodos del diccionario para obtener solo los valores y usando funciones predefinidas de Python calcule el valor mínimo. NOTA: Esta no es la solución directamente, ni es la única manera de plantear la solución, es solo una recomendación que puede ayudarlo y guiarse para poder resolver el ejercicio. 

#### 5. Actualizar salario de un empleado

Define una función actualiar_salario_empleado, donde se le solicite al usuario ingresar el id del empleado que se vera beneficiado del aumento de su sueldo. Debe manejar una gestión de excepciones para los datos que ingresara el usuario para ejecutar esta funcionalidad del programa, como lo es el id y el valor del aumento del sueldo. Considera que el valor que se solicitara al usuario no es el nuevo sueldo, sino el aumento en soles. El ingreso de la información debería verse de esta manera:

```
>>> ========== Actualizar salario de un empleado ==========
>>> Ingrese el Id del empleado: 2
>>> Ingrese el aumento que recibira el empleado en soles: 200.00
```

Maneje el mensaje de error por si la información ingresada es incorrecto o si no se encontró a un empleado con el id ingresado.

#### 6. Terminar el programa

Cuando el usuario ingrese la opción 6, debe terminar la ejecución del programa, puede mostrar un mensaje diciendo que se termino la ejecución del programa.

### Rubrica de evaluación:

|     Funcionalidades     |    Puntos    |
|---------------|-------------- |
| Lectura de datos para registro de empleados en el programa.      | 4 pts     |
| Desarrollo del menú del programa y correcto funcionamiento en el manejo de las opciones que el usuario elige.        | 4 pts      |
| Desarrollo de la funcionalidad de visualización de la información de un empleado por su id.	        | 3 pts      |
| Desarrollo de la funcionalidad de cálculo de empleado/empleados con menor tiempo en la empresa.	     | 6 pts      |
| Desarrollo de la funcionalidad de actualizar salario de un empleado ingresando el aumento que le corresponde junto a su id.       | 3 pts     |
