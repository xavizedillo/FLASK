#Preparacion de examen

ips =  ['127.0.0.1', '192.168.0.1', '10.0.0.1', '172.16.0.1']
divice_names = ["Router1", "Switch", "Firewall"]

'''

for ip in ips:
    for divice in divice_names:
        if (ip == '192.168.0.1' and divice == 'Router1'):
            print(f"IP: {ip}, Dispositivo: {divice}")
'''

dispo = ['Router', '192.168.0.1', ['P1', '192.168.0.1']]
#dispo.append(dispo[2])

print (dispo[2][1])

