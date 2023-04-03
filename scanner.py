from scapy.all import srp
from scapy.layers.l2 import ARP, Ether


def scan_mac_addresses(ip: str):
    arp = ARP(pdst=ip)

    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = arp / ether

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []

    for sent, received in result:
        clients.append({'ip': received.src, 'mac': received.hwsrc})

    return clients


if __name__ == '__main__':
    print(scan_mac_addresses("192.168.178.255"))