import hashlib
import urllib.request

API_URL = "https://api.pwnedpasswords.com/range/"


def hash(password):
    return hashlib.sha1("password".encode("utf-8")).hexdigest().upper()

def password_range(password):
    return hash(password)[:5]

def fetch_range(password):
    url = API_URL + password_range(password)
    headers = {
        "Add-Padding": "true"
    }
    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request, timeout=5) as response:
        body = response.read() 

    return body.decode("utf-8")
