# 🌐 API Cliente-Servidor en Python

Proyecto **cliente-servidor** desarrollado en **Python** que implementa una **API REST sencilla** usando el servidor HTTP integrado de Python. El servidor expone endpoints para consultar información de municipios y el cliente consume dicha API mediante peticiones HTTP.

Proyecto ideal para practicar conceptos de **comunicación cliente-servidor**, manejo de **JSON**, creación de **APIs REST básicas** y consumo de servicios web con Python.

---

## 🚀 Características

* Servidor HTTP propio en Python
* API REST sencilla
* Respuesta de datos en formato JSON
* Listado completo de municipios
* Consulta individual de datos por nombre
* Cliente que consume la API usando peticiones HTTP

---

## 🛠️ Tecnologías usadas

* **Lenguaje:** Python
* **Servidor:** `http.server` (HTTPServer)
* **Cliente HTTP:** `requests`
* **Formato de datos:** JSON
* **Librerías estándar:**

  * `http.server`
  * `json`
  * `urllib.parse`

---

## 📂 Estructura del proyecto

```
project/
 ├── server.py      # Servidor HTTP y API
 └── client.py      # Cliente que consume la API
```

---

## 🧠 Funcionamiento de la aplicación

### 🔹 Servidor

El servidor expone los siguientes endpoints:

* **GET /api/list**
  Devuelve un listado completo de municipios en formato JSON.

* **GET /api/get/{municipio}**
  Devuelve la información asociada a un municipio concreto.

Si la ruta no existe o el municipio no es válido, el servidor responde con un error 404.

---

### 🔹 Cliente

El cliente realiza una petición HTTP al servidor:

1. Envía una solicitud `GET` al endpoint `/api/list`.
2. Recibe la respuesta en formato JSON.
3. Procesa los datos recibidos.
4. Muestra la información por consola.

---

## ▶️ Cómo ejecutar el proyecto

### 1️⃣ Ejecutar el servidor

```bash
python server.py
```

El servidor se iniciará en:

```
http://0.0.0.0:8080
```

---

### 2️⃣ Ejecutar el cliente

En otra terminal:

```bash
python client.py
```

El cliente se conectará al servidor y mostrará los datos recibidos.

---

## 📌 Posibles mejoras futuras

* Implementar método `POST`
* Manejo de errores más detallado
* Respuestas JSON estandarizadas
* Separar rutas y lógica del servidor
* Añadir persistencia con base de datos
* Autenticación básica

---

## 👨‍💻 Autor

Desarrollado por **Esteban**

---

## 📄 Licencia

Proyecto de uso educativo y personal. Se permite su modificación y reutilización libremente.

---

⭐ Si te gusta el proyecto, ¡no olvides darle una estrella en GitHub!
