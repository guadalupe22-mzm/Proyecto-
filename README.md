Este repositorio trata sobre el proyecto del primer curso "Desarrollo y control de versiones GitHub SOV0"

Profesora: Stephanie Delgado Brenes 
Estudiante: Maria Gudaldupe Mora Zuñiga
Curso: Desarrollo y control de versiones GitHub SOV0

Fecha de elaboracion: Se empezo el 24 de coctubre del 2024

Codigo adjunto: Promedio de estudiante

Como primera instancia, en este repositorio se encuentra el código realizado en la parte 1 de la tarea. El código trata sobre el cálculo de los promedios de un profesor. Al inicio, aparece un mensaje solicitando ingresar la cantidad de exámenes realizados, con un máximo de tres exámenes. En caso de que se ingrese una cantidad mayor, aparecerá un mensaje indicando que no es posible realizar la calificación. Si se ingresan tres exámenes o menos, el código continuará y aparecerá un mensaje solicitando que se digiten las notas obtenidas. El programa sumará las notas para luego dividirlas entre la cantidad de exámenes, obteniendo así el promedio.

Explicación del código:
Este programa solicita al usuario la cantidad de exámenes que ha realizado y, según el número de exámenes ingresados (con un máximo de tres), calcula el promedio de las notas introducidas. Dependiendo del promedio obtenido, el programa mostrará un mensaje indicando si el usuario ha aprobado, necesita realizar una ampliación o ha reprobado

Mensaje de bienvenida 
Se muestra un mensaje inicial que indica el propósito del programa.

![Captura de pantalla (46)](https://github.com/user-attachments/assets/f98bc26f-d4e6-4c74-bb51-ced48de61745)


Entrada de la cantidad de exámenes y verificación de la cantidad de exámenes:
Aquí se solicita al usuario que ingrese el número de exámenes que ha realizado.
Si el usuario introduce una cantidad mayor a 3, el programa muestra un mensaje de error y no procede con el cálculo del promedio.

![Captura de pantalla (47)](https://github.com/user-attachments/assets/d131e91d-2877-4b53-be46-90c9f1ef6e25)


Solicitud de notas: 
Si la cantidad de exámenes es válida (3 o menos), el programa pedirá al usuario que ingrese las notas correspondientes.
Se solicitan las notas dependiendo del número de exámenes realizados. Si el usuario ha realizado solo dos exámenes, la tercera nota se asigna como 0 para no interferir con el cálculo del promedio.

![Captura de pantalla (48)](https://github.com/user-attachments/assets/4ac9a344-8113-46d9-91db-96af0b68f5b0)

Cálculo del promedio y evaluación del resultado:
Se suman las notas ingresadas y se dividen entre la cantidad de exámenes para obtener el promedio. El resultado se muestra al usuario.
 Dependiendo del promedio obtenido, el programa mostrará uno de los siguientes mensajes:

Aprobado: Si el promedio es mayor o igual a 70.
Ampliación: Si el promedio está entre 60 y 69.
Reprobado: Si el promedio es menor a 60.

![Captura de pantalla (49)](https://github.com/user-attachments/assets/0a9aaf81-ac2f-465b-943b-e8e7c0d29d5b)

