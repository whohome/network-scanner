from scapy.all import srp
from scapy.layers.l2 import ARP, Ether
from socket import gethostname, gethostbyname, gethostbyaddr

# Holen Sie den Hostnamen
hostname = gethostname()

# Holen Sie die IP-Adresse des Hostnamens
ip_address = gethostbyname(hostname)

# Holen Sie die Netzwerkadresse aus der IP-Adresse und der Netzwerkmaske
net_address = '.'.join(ip_address.split('.')[:3]) + '.0'

# Definieren Sie die Ziel-IP-Adresse
target_ip = f"{net_address}/24"

# Erstellen Sie ARP-Paket, um MAC-Adresse abzurufen
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

# Senden Sie das Paket und erhalten Sie die Antwort
result = srp(packet, timeout=3, verbose=0)[0]

# Analyse der Antwort
devices = []
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

print(devices)

# Überprüfen Sie, ob die gesuchte MAC-Adresse im Netzwerk vorhanden ist
target_mac = "36:39:A4:10:37:12"
found = False
for device in devices:

    if device['mac'] == target_mac.lower():
        found = True

if found:
    print(f"Das Gerät mit der MAC-Adresse {target_mac} wurde im Netzwerk gefunden.")
else:
    print(f"Das Gerät mit der MAC-Adresse {target_mac} konnte nicht im Netzwerk gefunden werden.")



