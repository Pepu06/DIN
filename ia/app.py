# from generateresponse import generate_response
from flask import Flask, jsonify, make_response, request
import pandas as pd
from flask_cors import CORS
import google.generativeai as genai
import os
import threading
import json


app = Flask(__name__)


respuestas_separadas = []

def generate_multiple_answers_by_prompt(prompt):
    genai.configure(api_key='AIzaSyBEUX9jRLF8XEB8kz7Y8xsATQI_ZkGlz4Q')


    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "max_output_tokens": 8192,
    }


    model = genai.GenerativeModel(
        model_name="tunedModels/din-7joru1ifz2cq",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
    ]
    )
   
    response = chat_session.send_message(prompt)
   
    return response.text


CORS(app)
@app.route("/")
def hello():
    return "I am alive!"


@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    texto = json.loads(request.get_data().decode("utf-8"))["texto"]
    if not json.loads(request.get_data().decode("utf-8"))["texto"] or not texto:
        texto = "HOLA"
    print(texto)
    # texto = "hola"
    respuestas = generate_multiple_answers_by_prompt(texto)
   
    print(respuestas)
    # Supongamos que 'respuestas' es tu cadena original
    respuestas_separadas = respuestas.split(';')
    print(respuestas_separadas)

    # respuestas_filtradas = [respuesta for respuesta in respuestas_separadas if respuesta.startswith(('1:', '2:', '3:'))]


    # Obtener solo las primeras 3 respuestas
    primeras_tres_respuestas = respuestas_separadas[:3]


    # Mostrar las primeras 3 respuestas
    # print(respuestas_separadas)
    # respuestas_separadas = ["Hola, soy Matias", "Hola como estas?", "Hola buen dia."]
    return jsonify(primeras_tres_respuestas)


threading.Thread(target=app.run, kwargs={'host':'0.0.0.0','port':3000}).start()
