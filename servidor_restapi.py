from http.server import HTTPServer, ThreadingHTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import unquote

municipios = {
  "Alcalá de los Gazules": 5227,
  "Alcalá del Valle": 4982,
  "Algar": 1433,
  "Algeciras": 122368,
  "Algodonales": 5504,
  "Arcos de la Frontera": 30953,
  "Barbate": 22872,
  "Los Barrios": 24069,
  "Benalup-Casas Viejas": 7160,
  "Benaocaz": 685,
  "Bornos": 7607,
  "El Bosque": 2209,
  "Cádiz": 113066,
  "Castellar de la Frontera": 3043,
  "Chiclana de la Frontera": 87493,
  "Chipiona": 19592,
  "Conil de la Frontera": 23497,
  "Espera": 3820,
  "El Gastor": 1699,
  "Grazalema": 2005,
  "Jerez de la Frontera": 212730,
  "Jimena de la Frontera": 6681,
  "La Línea de la Concepción": 63271,
  "Medina Sidonia": 11739,
  "Olvera": 7974,
  "Paterna de Rivera": 5451,
  "Prado del Rey": 5647,
  "El Puerto de Santa María": 89435,
  "Puerto Real": 41963,
  "Puerto Serrano": 6971,
  "Rota": 29491,
  "San Fernando": 94120,
  "San José del Valle": 4453,
  "San Martín del Tesorillo": 2797,
  "San Roque": 33018,
  "Sanlúcar de Barrameda": 69727,
  "Setenil de las Bodegas": 2675,
  "Tarifa": 18564,
  "Torre Alháquime": 803,
  "Trebujena": 7010,
  "Ubrique": 16383,
  "Vejer de la Frontera": 12656,
  "Villaluenga del Rosario": 462,
  "Villamartín": 12095,
  "Zahara de la Sierra": 1371
}

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = unquote(self.path)
        m = url.split("/")

        if "/"+m[1]+"/"+m[2] == "/api/get" and municipios.__contains__(m[3]):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            jsontext = json.dumps(str(municipios.get(m[3])))
            self.wfile.write(jsontext.encode())
        
        elif self.path == "/api/list":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            jsontext = json.dumps(municipios)
            self.wfile.write(jsontext.encode())
        
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            pagina = "<html><body><h1 style=\"color:red\">Error 404 - Inutil</h1><body/><html/>"
            self.wfile.write(pagina.encode())

    def do_POST(self):
        pass


ip = "0.0.0.0"
port = 8080
address = (ip, port)
server = HTTPServer(address, HTTPRequestHandler)
server.serve_forever()