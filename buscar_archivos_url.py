import requests

lista_palabras="diccionario.txt"

url=input("Ingresa la url (con puerto si no es ek por defecto [80]): ")

print("""
------------------------------------------------
Iniciando búsqueda de archivos en la url...
------------------------------------------------
""")
try:
    with open("diccionario.txt", 'r', encoding='utf') as archivo:
        for linea in archivo:
            r=requests.get(url.rstrip('\n') + "/" + linea.rstrip('\n'))
            if r.status_code < 400:
                print(f"    Existe {url}/{linea}")

    print("""
    ------------------------------------------------
    Proceso de búsqueda de archivos finalizado.
    ------------------------------------------------
    """)
except FileNotFoundError:
    print("No se puede abrir el diccionario, verifique que exista.")
