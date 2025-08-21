from flask import Flask, request, jsonify

app = Flask(__name__)

# Aquí se almacenarán los datos temporalmente (en memoria)
datos_diarios = []

@app.route('/guardar', methods=['POST'])
def guardar():
    datos = request.json
    datos_diarios.append(datos)
    return jsonify({"mensaje": "Guardado correctamente"}), 200

@app.route('/listar', methods=['GET'])
def listar():
    return jsonify(datos_diarios)

if __name__ == '__main__':
    app.run(debug=True)