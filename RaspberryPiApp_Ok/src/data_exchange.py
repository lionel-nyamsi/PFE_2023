#import netifaces

#interfaces = netifaces.interfaces()
mac_addr = None


def get_mac_address():
    # Faire une boucle sur toutes les interfaces pour trouver l'adresse MAC
    global mac_addr
    """for interface in interfaces:
        try:
            # Obtenir les adresses IP et MAC de l'interface
            addrs = netifaces.ifaddresses(interface)
            mac_addr = addrs[netifaces.AF_LINK][0]['addr']
            break

        except:
            pass"""

    return "mac_addr"
