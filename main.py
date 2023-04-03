from fastapi import FastAPI
from scanner import scan_mac_addresses

app = FastAPI()


@app.get("/")
def scan():
    return scan_mac_addresses(target_ip="192.168.178.255")
