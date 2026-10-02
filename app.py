from flask import Flask, jsonify

app = Flask(__name__)

# Datos de dispositivos
dispositivos = {
    "0001": {
        "ip": "192.168.0.1",
        "divice" : "Router",
        "policy" : ["Ro", "Not Allowed", [0.2,0.3,0.4]],
        "Status" : True
    },
    "101": {
        "ip": "192.168.1.10",
        "divice": "Router Principal",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "102": {
        "ip": "192.168.1.20",
        "divice": "Switch Core",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "103": {
        "ip": "192.168.1.30",
        "divice": "Firewall DMZ",
        "policy": ["REQUIRED_IP"],
        "Status": False
    },
    "104": {
        "ip": "192.168.1.40",
        "divice": "Servidor Web",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "105": {
        "ip": "10.0.0.1",
        "divice": "AP Recepción",
        "policy": ["REQUIRED_IP"],
        "Status": False
    }
}

#Endpoint html 
@app.route('/')
def inicio():
    return """
    <html>
    <body>
    <h1>Hola mundo</h1>
    <a href="https://127.0.0.1:5000/api/saludo">Buscar datos</>
    </body>
    </html>
    """

#Endpoint JSON
@app.route('/servidor_1')
def servidor_1():
    return jsonify(dispositivos)

# FUNCIÓN 2: Validar política de un solo dispositivo
def validar_politica(dispositivo):
    ip = dispositivo.get("ip", "")
    politica = dispositivo.get("policy", [""])
    ips_permitidas = ["192.168.1.10", "192.168.1.20", "192.168.1.30", "192.168.1.40", "192.168.1.50"]
    
    if "ALLOW_ALL" in politica:
        return "Configuración válida"
    elif "BLOCK_IP" in politica:
        return "Configuración inválida (IP bloqueada)"
    elif "REQUIRED_IP" in politica:
        if ip in ips_permitidas:
            return "Configuración válida"
        else:
            return "Configuración inválida (IP incorrecta)"
    return "Configuración inválida"

# Endpoint para validar un dispositivo específico
@app.route('/validar/<dispositivo_id>')
def validar_dispositivo(dispositivo_id):
    if dispositivo_id in dispositivos:
        resultado = validar_politica(dispositivos[dispositivo_id])
        return jsonify({
            "id": dispositivo_id,
            "resultado": resultado
        })
    return jsonify({"error": "Dispositivo no encontrado"}), 404

# FUNCIÓN 1: Mostrar todos los dispositivos
def mostrar_dispositivos(dicc_dispositivos):
    resultado = []
    for disp_id, datos in dicc_dispositivos.items():
        resultado_validacion = validar_politica(datos)
        resultado.append({
            "ID": disp_id,
            "Nombre": datos.get('divice'),
            "IP": datos.get('ip'),
            "Política": datos.get('policy'),
            "Estado": datos.get('Status'),
            "Resultado": resultado_validacion
        })
    return resultado

# Endpoint para mostrar todos los dispositivos con validación
@app.route('/dispositivos')
def listar_dispositivos():
    return jsonify(mostrar_dispositivos(dispositivos))

# FUNCIÓN 3: Generar resumen de estadísticas de la red
def generar_resumen(dicc_dispositivos):
    activos = 0
    inactivos = 0
    validos = 0
    invalidos = 0
    
    for datos in dicc_dispositivos.values():
        # Conteo de estado
        if datos.get("Status") == True:
            activos += 1
        else:
            inactivos += 1
            
        # Conteo de validación
        if validar_politica(datos) == "Configuración válida":
            validos += 1
        else:
            invalidos += 1
    
    return {
        "activos": activos,
        "inactivos": inactivos,
        "validos": validos,
        "invalidos": invalidos
    }

# Endpoint para generar resumen de estadísticas
@app.route('/resumen')
def resumen():
    return jsonify(generar_resumen(dispositivos))






if __name__ == '__main__':
    app.run(debug=True)
