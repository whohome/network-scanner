from fastapi import FastAPI
from scanner import scan_mac_addresses
from models import Target

app = FastAPI()


@app.get("/")
def get_mac_address(target: Target):
    return scan_mac_addresses(target_ip=target.target)
