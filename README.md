|-----Escuela de Fútbol El Potrero – Soccer Web-----|
_______________________________________________________________________________________________________________________________________________
_______________________________________________________________________________________________________________________________________________
|-----Descripción-----|
_______________________________________________________________________________________________________________________________________________
Aplicación web desarrollada con Django para la gestión de inscripciones, programas, calendario de entrenamientos y administración de alumnos de la Escuela de Fútbol El Potrero. Incluye autenticación de usuarios, panel de administración personalizado, sincronización automática de datos entre inscripciones y usuarios, y un diseño visual híbrido deportivo.
_______________________________________________________________________________________________________________________________________________
|-----Funcionalidades principales-----|
_______________________________________________________________________________________________________________________________________________
Registro y autenticación de usuarios.

Formulario de inscripción de alumnos con validación y estado de aprobación.

Panel de administración con dashboard y métricas.

Sincronización automática de datos entre Alumno y User mediante señales.

Módulos independientes: alumnos, calendario, contacto, galería, logros, programas, usuarios.

Footer estilizado en negro/dorado con enlaces de contacto y redes sociales.
_______________________________________________________________________________________________________________________________________________
|-----Tecnologías utilizadas-----|
_______________________________________________________________________________________________________________________________________________
Backend: Django (Python 3.13)

Frontend: HTML, CSS, JavaScript

Base de datos: PostgreSQL(para desarrollo)

Servidor local (Windows): Waitress

Servidor producción (Linux): Gunicorn + Nginx

Control de versiones: GitHub
_______________________________________________________________________________________________________________________________________________
|-----Instalación y ejecución-----|
_______________________________________________________________________________________________________________________________________________
1. Clonar el repositorio

git clone https://github.com/tuusuario/soccer-web.git
cd soccer-web/elpotrero

2. Crear entorno virtual

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

3. Instalar dependencias

pip install -r requirements.txt

4. Migrar base de datos

python manage.py migrate

5. Crear superusuario

python manage.py createsuperuser

6. Ejecutar servidor local (Windows con Waitress)

waitress-serve --listen=127.0.0.1:8000 elpotrero.wsgi:application

Accede en: http://127.0.0.1:8000
_______________________________________________________________________________________________________________________________________________
|-----Estructura del proyecto-----|
_______________________________________________________________________________________________________________________________________________
SOCCER-WEB/
│
├── elpotrero/
│   ├── apps/
│   │   ├── alumnos/       # Inscripciones
│   │   ├── calendario/    # Eventos y entrenamientos
│   │   ├── contacto/      # Formulario de contacto
│   │   ├── core/          # Páginas principales y base.html
│   │   ├── galería/       # Fotos y videos
│   │   ├── logros/        # Trofeos y estadísticas
│   │   ├── programas/     # Programas deportivos
│   │   └── usuarios/      # Perfiles y roles
│   │
│   ├── elpotrero/         # Configuración global del proyecto
│   └── templates/
│       └── admin/         # Personalización del admin
│           ├── base_site.html
│           └── index.html
│
├── manage.py
├── requirements.txt
└── .gitignore
_______________________________________________________________________________________________________________________________________________
|-----Seguridad-----|
_______________________________________________________________________________________________________________________________________________
DEBUG=False en producción.

Configuración de ALLOWED_HOSTS con dominio o IP.

Uso de HTTPS recomendado (Certbot + Nginx en Linux).

Cookies seguras (CSRF_COOKIE_SECURE, SESSION_COOKIE_SECURE).
_______________________________________________________________________________________________________________________________________________
|-----Deployment-----|
_______________________________________________________________________________________________________________________________________________
Local (Windows): Waitress.

Producción (Linux VPS): Gunicorn + Nginx.

Alternativas rápidas: PythonAnywhere, Heroku, Render.
_______________________________________________________________________________________________________________________________________________
|-----Autor-----|
_______________________________________________________________________________________________________________________________________________
Cristian Laura – Desarrollador web en Django.Proyecto académico y profesional para la Escuela de Fútbol El Potrero.
_______________________________________________________________________________________________________________________________________________
|-----Contacto-----|
_______________________________________________________________________________________________________________________________________________
Email: soloacademico@prueba.com

Teléfono: +56 9xxxxxxxx

Redes sociales: Facebook | Instagram | X
_______________________________________________________________________________________________________________________________________________
|-----Licencia-----|
_______________________________________________________________________________________________________________________________________________
Este proyecto es de uso académico y personal.Todos los derechos reservados © 2026 Escuela de Fútbol El Potrero.
