<div aling="center">
    <img src="/img/Banner.jpg">
</div>

# Entrega Final de Proyecto Talento Tech


Alumna: Dovis Yesica Lorena

Docente: Torreblanca Maximiliano

Tutor: Tarabusi Sofia

Comisión: C24221 | Programación Inicial con Python | Martes | 20h

___

## Consigna

"El objetivo es crear una aplicación en Python capaz de gestionar el inventario de una pequeña tienda. Esta aplicación funcionará desde la terminal y hará uso de una base de datos, permitiendo que los datos se guarden de forma permanente."

___

## Funcionalidad básica de la aplicación

Tu aplicación debe permitir a la persona que lo utiliza efectuar:

- [x] Registro de productos: Ingresar nuevos productos al inventario, solicitando nombre, descripción, cantidad disponible, precio y categoría.
- [x] Consulta de productos: Consultar el inventario y ver la información detallada de cada producto, como stock disponible y precio.
- [x] Actualización de productos: Modificar la cantidad disponible de un producto específico.
- [x] Eliminación de productos: Permitir eliminar productos del inventario.
- [x] Listado Completo: Generar un listado completo del inventario.
- [x] Reporte de Bajo Stock: Mostrar un reporte de productos con bajo stock.

___

### Registro de productos: 

+ La función registrar_producto agrega un nuevo producto al diccionario lista_de_productos, asignándole un identificador único generado automáticamente mediante la variable global index_global, que se incrementa en 1 cada vez que se llama la función. El producto, representado como un diccionario (datos_producto), se almacena en el inventario utilizando el nuevo identificador como clave.


`Codigo` 

<div aling="center">
    <img src="/img/1.jpg">
</div>


`Debug` 

<div aling="center">
    <img src="/img/1a.jpg">
</div>

___



### Consulta de productos:

+ La función mostrar_productos imprime en pantalla una lista de los productos almacenados en el diccionario lista_de_productos. Cada producto se muestra junto con su identificador (key) y sus datos. Al final, espera que el usuario presione Enter para continuar.


`Codigo` 

<div aling="center">
    <img src="/img/2a.jpg.jpg">
</div>


`Debug` 

<div aling="center">
    <img src="/img/2b.jpg">
</div>

___

### Actualización de productos:

+ La función actualizar_producto permite modificar los detalles de un producto en lista_de_productos. Al recibir el identificador del producto (key_producto), verifica si existe en el inventario. Si el producto se encuentra, muestra sus datos actuales y solicita al usuario nuevos valores para el nombre, precio, stock y categoría. Para asegurar que los valores ingresados para el precio y el stock sean numéricos, utiliza el método isdigit(), que verifica si una cadena de texto contiene solo dígitos. Aunque al principio me resultó complicado entender cómo usar isdigit(), con la ayuda de la documentación pude aclarar su funcionamiento, y al final logré implementarlo correctamente. Si ambos valores son válidos, actualiza el producto con los nuevos datos; de lo contrario, muestra un mensaje de error. Si el producto no se encuentra, informa al usuario que el producto no existe.

`Codigo` 

<div aling="center">
    <img src="/img/3.jpg">
</div>


`Debug` 

<div aling="center">
    <img src="/img/3b.jpg">
</div>

___

### Eliminación de productos: 


+ La función eliminar_producto permite eliminar un producto de lista_de_productos usando su identificador único (index). Si el producto existe en el inventario, lo elimina mediante el método pop() y muestra un mensaje confirmando la eliminación, junto con los detalles del producto eliminado. Si el producto no se encuentra, muestra un mensaje indicando que no se encontró el producto. Después de realizar la operación, espera que el usuario presione Enter para continuar.

`Codigo` 

<div aling="center">
    <img src="/img/4.jpg">
</div>


`Debug` 

<div aling="center">
    <img src="/img/4a.jpg">
</div>


___

### Listado Completo:

+ La función buscar_producto permite buscar un producto en lista_de_productos utilizando su identificador único (index). Si el producto existe en el inventario, muestra sus detalles, como nombre, precio, stock y categoría. Si el producto no se encuentra, informa al usuario que el producto no existe. Después de mostrar los detalles o el mensaje de error, la función espera que el usuario presione Enter para continuar.

`Codigo` 

<div aling="center">
    <img src="/img/5.jpg">
</div>


`Debug` 

<div aling="center">
    <img src="/img/5a.jpg>
</div>
___


### Reporte de Bajo Stock:

+ La función reporte_bajo_stock genera un reporte de los productos en lista_de_productos cuyo stock es menor o igual al valor proporcionado en el parámetro limite. Utiliza una lista por comprensión para filtrar los productos que cumplen con esta condición. Si se encuentran productos con bajo stock, los imprime en pantalla; si no, muestra un mensaje indicando que no se encontraron productos con bajo stock. Al final, espera que el usuario presione Enter para continuar.

`Codigo` 

<div aling="center">
    <img src="/img/6.jpg">
</div>


`Debug` 

<div aling="center">
    <img src="/img/6a.jpg">
</div>


<div aling="center">
    <img src="/img/6b.jpg">
</div>
___

### Cierre Menu:

+ Estructura de control if-elif-else que se utiliza para gestionar las opciones seleccionadas por un usuario en un menú. Si la opción ingresada es "7", se imprime el mensaje "Vuelva prontossss.", indicando una despedida. Si la opción no corresponde a ninguna de las previstas, el bloque else captura cualquier otro valor y muestra el mensaje "Opción no encontrada. Intente de nuevo.", sugiriendo que el usuario intente con otra opción válida. Este tipo de estructura es común en menús interactivos para manejar diferentes respuestas y errores

`Debug` 

<div aling="center">
    <img src="/img/salida.jpg">
</div>

<div aling="center">
    <img src="/img/mensajeopcionerronea.jpg">
</div>

<div aling="center">
    <img src="/img/x.jpg">
</div>

___


<div aling="center">
    <img src="/img/bannerdown.jpg">
</div>

**    ©     [DOVIS YESICA]   2024  . Todos los derechos reservados.   Gracias TOTALES / Goal achieved!!!!   **

___
