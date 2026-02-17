import configparser
import os
import socket

DATA_DIR = os.environ.get("BAMBU_DATA_DIR", "data")
os.makedirs(DATA_DIR, exist_ok=True)

CONFIG_FILE = os.path.join(DATA_DIR, "credentials.ini")
SECTION = "DEFAULT"
def ReadCredentials():
    config = configparser.ConfigParser()
    # Create file if it doesn't exist
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as file:
            file.write("[DEFAULT]\n")  # Add an empty DEFAULT section

    config.read(CONFIG_FILE)
    return config

def SaveNewToken(name, token):
    config = ReadCredentials()
    config[SECTION][name] = token
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

def IsValidIp(host: str) -> bool:
    try:
        socket.inet_aton(host)
        return True
    except OSError:
        return False

def IsValidPort(port) -> bool:
    try:
        port = int(port)
        return 1 <= port <= 65535
    except (TypeError, ValueError):
        return False