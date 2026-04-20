import requests

lista_palabras="diccionario.txt"

url=input("Ingresa la url (con puerto si aplica): ")

try:
    with open("diccionario.txt", 'r', encoding='utf') as archivo:
        for linea in archivo:
            r=requests.get(url.rstrip('\n') + "/" + linea.rstrip('\n'))
            if r.status_code < 400:
                print(f"    Existe {url}/{linea}")
except FileNotFoundError:
    print("No se puede abrir el diccionario.")

#print(r)
#print(dir(r))
#print(help(r))
#print(r.text)
#print(r.status_code)
#print(r.headers)
