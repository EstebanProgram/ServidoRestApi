import requests;

url = "http://localhost:8080"
respuesto = ""

print("*******Menu*******")
print("1- Poblacion de un municipio")
print("2- Lista de municipios")

option = int(input("Seleccione una opcion valida: "))

if (option == 1):
    municipio = input("Que municipio le gustaria buscar: ")
    url = url + "/api/get/" + municipio
    datos = requests.get(url)
    if (datos.status_code == 404):
        print("Municipio inecxistente")
    else:
        print("El municipio " + municipio + " tiene un total de " + datos.text)
elif (option == 2):
    url = url+"/api/list"
    datos = requests.get(url)
    jsonText = datos.json()
    for municipio in jsonText:
        print(municipio)
else:
    print("Elija una opcion valida")