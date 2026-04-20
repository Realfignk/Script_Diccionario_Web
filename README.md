# Script Diccionario Web 

Script en Python para realizar una búsqueda de archivos en una url dado un archivo de texto con nombre comunes (diccionario).

## Características
- Facilidad de uso
- Portable
- Ejecución rápida.

## Requisitos
Es necesario tener instalado o contar con:
* Python 3
* Librería requests (instalar con pip install o el gestor de paquetes si se usa Linux).

## Instalación y Uso

1. Copia el script o extrae el zip.
2. Asegurate de tener creado el archivo de diccionario.
3. Ejecútalo: python3 nombre_script.py url

El diccionario solo debe de contener un nombre de archivo por linea. Se incluye un ejemplo del diccionario que puede modificarse, o puede crearse uno. Es importante que tenga el nomnbre "diccionario.txt" y que se encuentre en el mismo directorio del programa.

Ejemplo de contenido del diccionario:
   index.html
   login.php
   password.txt
   dashboard.php

## Estructura
├── diccionario.txt              # Archivo de texto con nombre comúnes de archivos comunes en urls.
├── README.md                    # Documentación principal
└── script_diccionario_web.py    # Script principal

## Ejemplo de Salida

------------------------------------------------
Iniciando búsqueda de archivos en la url...
------------------------------------------------
   Existe http://myurl.com/index.html
   Existe http://myurl.com/login.php
------------------------------------------------
Proceso de búsqueda de archivos finalizado.
------------------------------------------------
