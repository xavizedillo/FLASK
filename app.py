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
    },
    "106": {
        "ip": "10.0.0.2",
        "divice": "AP Ventas",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "107": {
        "ip": "10.0.0.3",
        "divice": "AP IT",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "108": {
        "ip": "10.0.0.4",
        "divice": "Router Backup",
        "policy": ["ALLOW_ALL"],
        "Status": False
    },
    "109": {
        "ip": "10.0.0.5",
        "divice": "Switch Access 1",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "110": {
        "ip": "10.0.0.6",
        "divice": "Switch Access 2",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "111": {
        "ip": "10.0.0.7",
        "divice": "Firewall Internet",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "112": {
        "ip": "10.0.0.8",
        "divice": "Servidor DNS",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "113": {
        "ip": "10.0.0.9",
        "divice": "Servidor DHCP",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "114": {
        "ip": "10.0.0.10",
        "divice": "Servidor FTP",
        "policy": ["ALLOW_ALL"],
        "Status": False
    },
    "115": {
        "ip": "10.0.0.11",
        "divice": "Servidor Mail",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "116": {
        "ip": "10.0.0.12",
        "divice": "Servidor DB",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "117": {
        "ip": "10.0.0.13",
        "divice": "AP Pasillo",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "118": {
        "ip": "10.0.0.14",
        "divice": "Switch Distribución",
        "policy": ["BLOCK_IP"],
        "status": True
    },
    "119": {
        "ip": "10.0.0.15",
        "divice": "Router WAN",
        "policy": ["ALLOW_ALL"],
        "Status": False
    },
    "120": {
        "ip": "10.0.0.16",
        "divice": "Firewall Internal",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "121": {
        "ip": "10.0.0.17",
        "divice": "Servidor Backup",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "122": {
        "ip": "10.0.0.18",
        "divice": "Servidor Archivo",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "123": {
        "ip": "10.0.0.19",
        "divice": "AP Exterior",
        "policy": ["REQUIRED_IP"],
        "Status": False
    },
    "124": {
        "ip": "10.0.0.20",
        "divice": "Switch PoE",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "125": {
        "ip": "10.0.0.21",
        "divice": "Router Branch",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "126": {
        "ip": "10.0.0.22",
        "divice": "Servidor VPN",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "127": {
        "ip": "10.0.0.23",
        "divice": "AP Conf",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "128": {
        "ip": "10.0.0.24",
        "divice": "Switch Core 2",
        "policy": ["BLOCK_IP"],
        "Status": False
    },
    "129": {
        "ip": "10.0.0.25",
        "divice": "Firewall Perimeter",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "130": {
        "ip": "10.0.0.26",
        "divice": "Servidor Proxy",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "131": {
        "ip": "10.0.0.27",
        "divice": "Servidor Logs",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "132": {
        "ip": "10.0.0.28",
        "divice": "AP Cafeteria",
        "policy": ["REQUIRED_IP"],
        "Status": False
    },
    "133": {
        "ip": "10.0.0.29",
        "divice": "Switch Access 3",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "134": {
        "ip": "10.0.0.30",
        "divice": "Router Lab",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "135": {
        "ip": "10.0.0.31",
        "divice": "Servidor Dev",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "136": {
        "ip": "10.0.0.32",
        "divice": "Servidor Test",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "137": {
        "ip": "10.0.0.33",
        "divice": "AP Garage",
        "policy": ["BLOCK_IP"],
        "Status": False
    },
    "138": {
        "ip": "10.0.0.34",
        "divice": "Switch Voice",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "139": {
        "ip": "10.0.0.35",
        "divice": "Router Voice",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "140": {
        "ip": "10.0.0.36",
        "divice": "Servidor VoIP",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "141": {
        "ip": "10.0.0.37",
        "divice": "AP Vestidores",
        "policy": ["REQUIRED_IP"],
        "Status": False
    },
    "142": {
        "ip": "10.0.0.38",
        "divice": "Switch Data",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "143": {
        "ip": "10.0.0.39",
        "divice": "Router Data",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "144": {
        "ip": "10.0.0.40",
        "divice": "Servidor Storage",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "145": {
        "ip": "10.0.0.41",
        "divice": "AP Rooftop",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "146": {
        "ip": "10.0.0.42",
        "divice": "Switch Access 4",
        "policy": ["BLOCK_IP"],
        "Status": False
    },
    "147": {
        "ip": "10.0.0.43",
        "divice": "Router Edge",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "148": {
        "ip": "10.0.0.44",
        "divice": "Servidor Video",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "149": {
        "ip": "10.0.0.45",
        "divice": "Servidor Media",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "150": {
        "ip": "10.0.0.46",
        "divice": "AP Lobby",
        "policy": ["REQUIRED_IP"],
        "Status": False
    },
    "151": {
        "ip": "10.0.0.47",
        "divice": "Switch Access 5",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "152": {
        "ip": "10.0.0.48",
        "divice": "Router Guest",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "153": {
        "ip": "10.0.0.49",
        "divice": "Servidor Guest",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "154": {
        "ip": "10.0.0.50",
        "divice": "AP Guest",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "155": {
        "ip": "10.0.0.51",
        "divice": "Switch Guest",
        "policy": ["BLOCK_IP"],
        "Status": False
    },
    "156": {
        "ip": "10.0.0.52",
        "divice": "Router IoT",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "157": {
        "ip": "10.0.0.53",
        "divice": "Servidor IoT",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "158": {
        "ip": "10.0.0.54",
        "divice": "Switch IoT",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "159": {
        "ip": "10.0.0.55",
        "divice": "AP IoT",
        "policy": ["REQUIRED_IP"],
        "Status": False
    },
    "160": {
        "ip": "10.0.0.56",
        "divice": "Router Security",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "161": {
        "ip": "10.0.0.57",
        "divice": "Servidor Security",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "162": {
        "ip": "10.0.0.58",
        "divice": "Switch Security",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "163": {
        "ip": "10.0.0.59",
        "divice": "AP Security",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "164": {
        "ip": "10.0.0.60",
        "divice": "Router HR",
        "policy": ["BLOCK_IP"],
        "Status": False
    },
    "165": {
        "ip": "10.0.0.61",
        "divice": "Servidor HR",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "166": {
        "ip": "10.0.0.62",
        "divice": "Switch HR",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "167": {
        "ip": "10.0.0.63",
        "divice": "AP HR",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "168": {
        "ip": "10.0.0.64",
        "divice": "Router Finance",
        "policy": ["REQUIRED_IP"],
        "Status": False
    },
    "169": {
        "ip": "10.0.0.65",
        "divice": "Servidor Finance",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "170": {
        "ip": "10.0.0.66",
        "divice": "Switch Finance",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "171": {
        "ip": "10.0.0.67",
        "divice": "AP Finance",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "172": {
        "ip": "10.0.0.68",
        "divice": "Router Marketing",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "173": {
        "ip": "10.0.0.69",
        "divice": "Servidor Marketing",
        "policy": ["BLOCK_IP"],
        "Status": False
    },
    "174": {
        "ip": "10.0.0.70",
        "divice": "Switch Marketing",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "175": {
        "ip": "10.0.0.71",
        "divice": "AP Marketing",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "176": {
        "ip": "10.0.0.72",
        "divice": "Router Sales",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "177": {
        "ip": "10.0.0.73",
        "divice": "Servidor Sales",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "178": {
        "ip": "10.0.0.74",
        "divice": "Switch Sales",
        "policy": ["ALLOW_ALL"],
        "Status": False
    },
    "179": {
        "ip": "10.0.0.75",
        "divice": "AP Sales",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "180": {
        "ip": "10.0.0.76",
        "divice": "Router Support",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "181": {
        "ip": "10.0.0.77",
        "divice": "Servidor Support",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "182": {
        "ip": "10.0.0.78",
        "divice": "Switch Support",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "183": {
        "ip": "10.0.0.79",
        "divice": "AP Support",
        "policy": ["REQUIRED_IP"],
        "Status": False
    },
    "184": {
        "ip": "10.0.0.80",
        "divice": "Router Operations",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "185": {
        "ip": "10.0.0.81",
        "divice": "Servidor Operations",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "186": {
        "ip": "10.0.0.82",
        "divice": "Switch Operations",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "187": {
        "ip": "10.0.0.83",
        "divice": "AP Operations",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "188": {
        "ip": "10.0.0.84",
        "divice": "Router Legal",
        "policy": ["BLOCK_IP"],
        "Status": False
    },
    "189": {
        "ip": "10.0.0.85",
        "divice": "Servidor Legal",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "190": {
        "ip": "10.0.0.86",
        "divice": "Switch Legal",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "191": {
        "ip": "10.0.0.87",
        "divice": "AP Legal",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "192": {
        "ip": "10.0.0.88",
        "divice": "Router Executive",
        "policy": ["REQUIRED_IP"],
        "Status": False
    },
    "193": {
        "ip": "10.0.0.89",
        "divice": "Servidor Executive",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "194": {
        "ip": "10.0.0.90",
        "divice": "Switch Executive",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "195": {
        "ip": "10.0.0.91",
        "divice": "AP Executive",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "196": {
        "ip": "10.0.0.92",
        "divice": "Router Warehouse",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "197": {
        "ip": "10.0.0.93",
        "divice": "Servidor Warehouse",
        "policy": ["BLOCK_IP"],
        "Status": False
    },
    "198": {
        "ip": "10.0.0.94",
        "divice": "Switch Warehouse",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "199": {
        "ip": "10.0.0.95",
        "divice": "AP Warehouse",
        "policy": ["ALLOW_ALL"],
        "Status": True
    },
    "200": {
        "ip": "10.0.0.96",
        "divice": "Router Production",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "201": {
        "ip": "10.0.0.97",
        "divice": "Servidor Production",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "202": {
        "ip": "10.0.0.98",
        "divice": "Switch Production",
        "policy": ["ALLOW_ALL"],
        "Status": False
    },
    "203": {
        "ip": "10.0.0.99",
        "divice": "AP Production",
        "policy": ["BLOCK_IP"],
        "Status": True
    },
    "204": {
        "ip": "10.0.0.100",
        "divice": "Router QC",
        "policy": ["REQUIRED_IP"],
        "Status": True
    },
    "205": {
        "ip": "10.0.0.101",
        "divice": "Servidor QC",
        "policy": ["ALLOW_ALL"],
        "Status": True
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
