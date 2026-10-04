import hashlib
import urllib.request

API_URL = "https://api.pwnedpasswords.com/range/"

def sha1_hash(password):
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

def password_prefix(password):
    return sha1_hash(password)[:5]

def password_suffix(password):
    return sha1_hash(password)[5:]

def fetch_range(prefix):
    if len(prefix) != 5:
        raise ValueError("the prefix must be exactly 5 characters")

    url = API_URL + prefix
    headers = {
        "Add-Padding": "true",
    }
    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request, timeout=5) as response:
        body = response.read()

    return body.decode("utf-8")

def pwned_count(password):
    full_hash = sha1_hash(password)
    prefix = password_prefix(password)
    suffix = password_suffix(password)

    text = fetch_range(prefix)
 
    for line in text.splitlines():
        line_suffix, count = line.split(":")
        if line_suffix == suffix:
            return int(count)
 
    return 0
