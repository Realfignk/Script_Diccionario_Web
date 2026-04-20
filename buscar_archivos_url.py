import requests

lista_palabras="diccionario.txt"

url=input("Ingresa la url (con puerto si no es ek por defecto [80]): ")

print("""
------------------------------------------------
Iniciando búsqueda de archivos en la url...
------------------------------------------------
""")

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    with open("diccionario.txt", 'r', encoding='utf') as archivo:
        for linea in archivo:       
            respuesta = requests.get(url.rstrip('\n') + "/" + linea.rstrip('\n'), headers=headers)
            if respuesta.status_code == 200:
                print(f"    Existe {url}/{linea}")
            elif respuesta.status_code == 403:
                print(f"    Prohibido {url}/{linea}")
    print("""
    ------------------------------------------------
    Proceso de búsqueda de archivos finalizado.
    ------------------------------------------------
    """)
except FileNotFoundError:
    print("No se puede abrir el diccionario, verifique que exista.")
except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la página: {e}")
