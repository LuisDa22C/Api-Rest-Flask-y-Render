# API REST Flask y Render - Registro de Animales

API REST desarrollada con Python y el microframework Flask, diseñada para la gestión de registros de animales utilizando un archivo local en formato JSON como base de datos. Se encuentra desplegada en la nube mediante Render.

## URL Pública de la API
* **Base URL:** https://api-animales-flask.onrender.com

---

## Endpoints Disponibles

La API cuenta con las siguientes rutas operativas para realizar operaciones CRUD:

1. **Obtener todos los animales**
   * **URL:** `/animals`
   * **Método:** `GET`
   * **Descripción:** Retorna una lista con todos los registros almacenados en formato JSON.

2. **Obtener un animal por nombre**
   * **URL:** `/animals/<nombre>`
   * **Método:** `GET`
   * **Descripción:** Consulta y devuelve los detalles de un animal específico.

3. **Crear un nuevo animal**
   * **URL:** `/animals`
   * **Método:** `POST`
   * **Descripción:** Registra un nuevo elemento enviando un objeto JSON en el cuerpo de la petición.
   * **Ejemplo de Body (JSON):**
     ```json
     {
       "nombre": "León",
       "grupo": "Mamífero",
       "alimentacion": "Carnívoro",
       "habitat": "Terrestre",
       "reproduccion": "Vivíparo",
       "estado_conservacion": "Vulnerable"
     }
     ```

4. **Actualizar un animal**
   * **URL:** `/animals/<nombre>`
   * **Método:** `PUT`
   * **Descripción:** Modifica los datos de un registro existente buscando por su nombre.

5. **Eliminar un animal**
   * **URL:** `/animals/<nombre>`
   * **Método:** `DELETE`
   * **Descripción:** Remueve un animal del sistema mediante su identificador o nombre.

---

## Tecnologías y Dependencias
* **Python 3.x**
* **Flask** (Microframework web)
* **Gunicorn** (Servidor WSGI para producción)

