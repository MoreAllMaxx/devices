import random

def get_mac_48():
    return ':'.join(f'{random.randrange(256):02x}' for _ in range(6))