Tercera pre- entrega Agustin Aballay 
La página arranca desde http://127.0.0.1:8000/inicio/ donde se observa un template con navegación en el margen superior derecho. Este template se encuentra dentro de la app 'Registros' bjao el nombre 'inicio'.
'inicio' hereda de 'padre' el formato y se reemplaza la barra de navegación bajo el block barrasnav

Dentro de la navegación se puede ir a 'Comprador', 'Producto' , 'Vendedor' y 'Buscar'
Cuando se selecciona alguno de estos botones, se redirecciona al usuario a cada template. 
En el Template 'Comprador', se ingresa a la base de datos Nombre y Apellido del comprador bajo dos campos de caracteres de un máximo de 30. 
En el Template 'Vendedor', se ingresa a la base de datos Nombre y Apellido del vendedor bajo dos campos de caracteres de un máximo de 30. 
En el Template 'Producto', se ingresa a la base de datos Nombre y Cantidad del producto comprado bajo un campo de caracteres de un máximo de 30 para el Nombre y un campo de números para la cantidad sin máximo.
En el Template 'Buscar', se solicita ingresar un valor de caracteres con un máximo de 30. Luego, se busca en la base de datos ese valor y se devuelve la cantidad comprada por cada comprador. 

Los modelos definidos para esta entrega son Comprador (campos: Nombre y Apellido), Producto(campos: Nombre y Cantidad) y Vendedor(campos: Nombre y Apellido).

Valores precargados en la BD
Comprador: Agustin Aballay/ Agustin Aballay/Agustin Perez/Jorge Benitez 
Producto: Iphone 3512/ Iphone 3512 / Telefono 5432 / Pelota 1234
Vendedor: Roman Riquelme/
