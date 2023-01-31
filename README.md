# Prueba Tecnica armatuvaca

### Tecnologias Usadas:

- Python 3.11.1 = Lenguaje de programación
- Django 4.1.5 = Framework Web
- Stripe 5.0.0 = Pasarela de pagos
- Mysql = gestor de base de datos

###  Instalación del proyecto

Para iniciar, se debe clonar el proyecto del repositorio de github en una carpeta de su preferencia. Esto puede hacerse abriendo la consola justamente en la carpeta seleccionada y escribiendo el siguiente comando

`$ git clone https://github.com/MiguelASG/Prueba_tecnica_armatuvaca.git`

se continua entrando con la consola a la carpeta clonada

`$ cd Prueba_tecnica_armatuvaca`

alli se debe crear el entorno virtual; si no se posee ese paquete con pip se descargara con el siguiente comando

`$ pip install virtualenv`

al terminar de descargarse se continua creando un entorno virtual con el comando

`$ virtualenv -p python env`

luego se activara el entorno con el comando

`$ .\env\Scripts\activate`

se instalan los paquetes requeridos, en este caso son

`$ pip install Django`
`$ pip install mysqlclient pymsql`
`$ pip install stripe`

en este punto ya se tiene lo necesario en cuestion de paquetes, se continuaria con la configuracion base de datos. 

###  Configuración de la base de datos(MySQL)

La base de datos esta configurada para correr por el puerto 3306, pero, si se requiere cambiar solo hay que cambiar en "settings.py" que deberia encontrarse en la carpeta Prueba_tecnica_armatuva\Payment\Payment

tambien en ese archivo puede cambiarse el usuario, nombre de la base de datos donde se guardara y si se necesita la contraseña, eliminando el simbolo # con el esta comentada y asignando la respectiva contraseña.

Con ello hecho ya solo faltaria encender la base de datos.

###Prender proyecto 

una vez la base de datos esta encendida, se entra en la carpeta payment ya con el entorno encendido, alli se enciende el proyecto con el comando

`$ python manage.py runserver`

estara corriendo en el endpoint [localHost](http://localhost:8000/api/payment/) y con postman podran enviarse peticiones POST
que constaran de la siguiente estructura JSON

```javascript
	{
		"name": "Miguel",
		"surname": "Sanchez",
		"card_number": "1234 5678 9101 1121",
		"card_cvv": 274,
		"total_value": 100000,
		"extra_description": "Mensaje de prueba"
	}
```
alli se pueden cambiar los valores de cada atributo, y los datos quedaran guardados en la base de datos.

### Stripe

La pasarela de pagos usada para este proyecto puede ser configurada solo cambiando la clave publica y secreta en el mismo archivo donde se configuro la base de datos en las variables 

```javascript 
	SECRET_KEY
	PUBLISHABLE_KEY
```
alli en los registros en la parte de desarrolladores se encontraran las peticiones, y sus respectivos estados.

### End
