# SmartHome - Watchapp
[![Codacy Badge](https://www.codacy.com/project/badge/c9f2b84663734ce1b820b2abce3b81e0)](https://www.codacy.com)
[![Build Status](https://magnum.travis-ci.com/imTachu/SmartHome.svg?token=FXoqSPyhGxTJyV3aAbkJ&branch=master)](https://magnum.travis-ci.com/imTachu/SmartHome)
### Introducción
Watchapp es una aplicación que busca controlar los sensores y actuadores instalados en un inmueble desde un navegador o desde dispositivos móviles. 

### Equipo
Integrante  | Rol
------------- | -------------
Ricardo Restrepo  | Team Leader
Lorena Salamanca  | Product Owner
Fredy Wilches  | Architecture Owner
German Bernal  | Integration Leader
Juan Vallejo  | Testing Leader

### Aplicaciones

Watchapp se puede ejecutar desde cada ambiente en:

Producción:   http://watchapp-prod.herokuapp.com/watchapp

Pruebas:      http://watchapp-test.herokuapp.com/watchapp

Desarrollo:   http://watchapp-dev.herokuapp.com/watchapp

### Para desarrolladores

Se debe tener un virtual environment y un workspace para ejecutar la aplicación, se deben seguir estos pasos:

`mkdir py && cd py`

`mkdir workspace`

`mkdir venv && cd venv`

`virtualenv watchapp`

`. watchapp/bin/activate`

Estando en el virtual environment, se debe hacer clone a este repositorio dentro de la carpeta workspace y ya ubicandose en /workspace/SmartHome/ se crea un archivo .env en el que deben ir las variables de entorno (las mismas que se configuran en Heroku), el archivo .env luce como sigue:

DJANGO_SETTINGS_MODULE=smarthome.settings

PYTHONUNBUFFERED=true

EMAIL_HOST_USER=watchapp.latam@gmail.com

EMAIL_HOST_PASSWORD=miso4101

DATABASE_URL=postgres://postgres:postgres@localhost:5432/watchapp

PATH="/Library/PostgreSQL/9.3/bin/:$PATH"

* La última línea debe relacionar la instalación de PostgreSQL

* El archivo .env no debe aparecer NUNCA en el repositorio.

Ya con el archivo .env configurado ejecutamos

`foreman start`

`foreman run pip install -r requirements.txt`

Basicamente para el entorno local se debe ejecutar `foreman run` y agregarle cualquier comando usual de Django, ejemplo:
`foreman run python manage.py runserver`

Para correr los comandos de Django sobre heroku se usa algo como:
`heroku run python manage.py syncdb -a watchapp-dev`

### Fixtures

Los fixtures son datos iniciales para cargar en la base de datos generada por Django, los cuales pueden ser generados mediante el siguiente comando:

`foreman run python manage.py dumpdata --indent 4 --exclude=admin --exclude=watchapp.Event > watchapp/fixtures/initial_data.json`

La base de datos se debe limpiar con el comando `foreman run python manage.py flush`

Y se deben cargar los datos del fixture así: `foreman run python manage.py loaddata watchapp/fixtures/initial_data.json`


### Despliegue

Watchapp se despliega automaticamente en cada una de las aplicaciones en Heroku cada vez que se hace push:
* El master es el ambiente de desarrollo
* test es el ambiente de pruebas
* prod es el ambiente de producción

Antes de realizar el despliegue en Heroku, se hace integración continua con Travis CI, lo que verifica que el pull request o push que se hizo pueda ser generado correctamente. El estado de la integración continua se puede ver en el badge "build" en este documento, que siempre debe estar en estado "passing". 

Cada vez que se haga un "buen push" (es decir, un push que Travis CI apruebe) en el ambiente test, se puede pasar el cambio a prod. Esta notificación la hará Travis CI automaticamente al equipo de operaciones mediante un correo electrónico. Asimismo, tan pronto el equipo de operaciones haga un cambio que Travis CI apruebe en producción, el stakeholder (Jonathan Alarcon) será notificado mediante un correo electrónico.

### Datos de prueba
Login>>> lorena:lorena
