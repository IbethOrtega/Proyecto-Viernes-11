from flask import Flask, jsonify, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')  # Sirve index.html desde la carpeta actual

@app.route('/generar_datos', methods=['GET'])
def generar_datos():
    df = pd.read_csv('services_data_webstore.csv')
    labels = df['Order ID'].tolist()  # Etiquetas para el eje x

    # Contar ocurrencias de cada servicio para la gráfica de barras de servicios
    service_counts = df['Service'].value_counts().to_dict()
    services = list(service_counts.keys())  # Tipos de servicios
    counts = list(service_counts.values())  # Conteos de cada servicio

    # Diccionario con diferentes conjuntos de datos
    data = {
        'precio': df['Total Price'].tolist(),
        'horas': df['Hours of Work'].tolist(),
        'tarifa_hora': df['Hourly Rate'].tolist(),
        'service_labels': services,  # Etiquetas de servicios
        'service_counts': counts     # Conteo de servicios
    }
    
    return jsonify({'labels': labels, 'data': data})

if __name__ == '__main__':
    app.run(debug=True)
