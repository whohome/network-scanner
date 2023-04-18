from scapy.all import srp
from scapy.layers.l2 import ARP, Ether
from socket import gethostname, gethostbyname, gethostbyaddr


def find_ip_and_mac_addresses():

    ## hostname = gethostname()
    ## ip_address = gethostbyname(hostname)
    ## net_address = '.'.join(ip_address.split('.')[:3]) + '.0'

    ## print(net_address)

    target_ip = f"{'192.168.178.0'}/24"

    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices


def find_mac_addresses():
    macs = []

    for address in find_ip_and_mac_addresses():
        macs.append(address["mac"])

    return macs
