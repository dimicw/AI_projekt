import ipaddress
import requests

# Zakres IP do przeszukania
ip_range = ipaddress.ip_network('83.25.128.0/17')

# Sprawdź każde IP w zakresie
for ip in ip_range.hosts():
    try:
        response = requests.get(f"http://{ip}", timeout=1)

        # Jeśli odpowiedź zawiera 'camera', to prawdopodobnie jest to kamera
        if 'camera' in response.text.lower():
            print(f"Kamera znaleziona: {ip}")
    except requests.exceptions.RequestException:
        pass
