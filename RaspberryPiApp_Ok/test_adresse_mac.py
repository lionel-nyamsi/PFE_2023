import netifaces

interfaces = netifaces.interfaces()
mac_addr = None

# Faire une boucle sur toutes les interfaces pour trouver l'adresse MAC
for interface in interfaces:
    try:
        # Obtenir les adresses IP et MAC de l'interface
        addrs = netifaces.ifaddresses(interface)
        mac_addr = addrs[netifaces.AF_LINK][0]['addr']
        break

    except:
        pass

print("Adresse MAC de l'interface réseau actuelle :", mac_addr)
