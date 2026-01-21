#El Detector de Intrusos (Hacking) Simulado
#Tienes una lista de IPs permitidas (Whitelist). Si aparece una IP rara,lanza una alerta.
#Reto:comparar contra una lista buena 

# empezamos con lista de IPs que tenemos permmitidas

ips_permitidas = ["192.168.1.1","192.168.1.2","10.0.0.55","192.168.1.5"]
""" definimos la lista de ips permitidas
"""
print("--- iniiciando escaneo del trafico de red para detectar intrusos--")
# si la ip empieza con 192.168 es de la casa,seguro
for ip in ips_permitidas:
    if "192.168" in ip :
        print(f"ip segura detectada:{ip} es de la casa")
    else:
        print(f"alerta ip {ip} desconocida, posible intruso detectado!")