import json
from flask import Flask, jsonify, request

app = Flask(__name__)


# Carga la lista de animales desde el JSON
def cargar_animales():
    try:
        with open('animales.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Guarda la lista actualizada en el JSON
def guardar_animales(datos):
    with open('animales.json', 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)


# --- RUTAS DE LA API ---

@app.route("/")
def home():
    return "¡API de Animales funcionando!"


# 1. MÉTODO GET (Obtener todos los animales)
@app.route("/animals", methods=["GET"])
def get_animals():
    lista_animales = cargar_animales()
    return jsonify(lista_animales), 200

    # 1.5. MÉTODO GET ESPECÍFICO (Obtener un solo animal por su nombre)
@app.route("/animals/<string:nombre_animal>", methods=["GET"])
def get_animal_by_name(nombre_animal):
    lista_animales = cargar_animales()
    
    # Buscar el animal en la lista (ignorando mayúsculas/minúsculas)
    for animal in lista_animales:
        if animal["nombre"].lower() == nombre_animal.lower():
            return jsonify(animal), 200
            
    # Si termina el ciclo y no lo encuentra, manda un error 404
    return jsonify({"error": f"Animal '{nombre_animal}' no encontrado"}), 404


# 2. MÉTODO POST (Crear un nuevo animal)
@app.route("/animals", methods=["POST"])
def create_animal():
    lista_animales = cargar_animales()
    
    nuevo_animal = request.get_json()
    
    if not nuevo_animal or "nombre" not in nuevo_animal:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
        
    lista_animales.append(nuevo_animal)
    guardar_animales(lista_animales)
    
    return jsonify({"mensaje": "Animal agregado con éxito", "animal": nuevo_animal}), 201


# 3. MÉTODO PUT (Actualizar un animal por su nombre)
@app.route("/animals/<string:nombre_animal>", methods=["PUT"])
def update_animal(nombre_animal):
    lista_animales = cargar_animales()
    datos_actualizados = request.get_json()
    
    # Buscar el animal en la lista
    for animal in lista_animales:
        if animal["nombre"].lower() == nombre_animal.lower():
            # Actualiza los campos que se envíen en la petición
            animal.update(datos_actualizados)
            guardar_animales(lista_animales)
            return jsonify({"mensaje": f"Animal '{nombre_animal}' actualizado", "animal": animal}), 200
            
    return jsonify({"error": "Animal no encontrado"}), 404


# 4. MÉTODO DELETE (Eliminar un animal por su nombre)
@app.route("/animals/<string:nombre_animal>", methods=["DELETE"])
def delete_animal(nombre_animal):
    lista_animales = cargar_animales()
    
    lista_filtrada = [a for a in lista_animales if a["nombre"].lower() != nombre_animal.lower()]
    
    # Si la lista mide lo mismo, significa que no se encontró el animal
    if len(lista_animales) == len(lista_filtrada):
        return jsonify({"error": "Animal no encontrado"}), 404
        
    guardar_animales(lista_filtrada)
    return jsonify({"mensaje": f"Animal '{nombre_animal}' eliminado con éxito"}), 200


import os

if __name__ == '__main__':
    # Obtiene el puerto asignado por el sistema de hospedaje o usa el 5000 por defecto si estás en local
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)