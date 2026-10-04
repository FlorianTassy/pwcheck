import hashlib


def hash(password):
    return hashlib.sha1("password".encode("utf-8")).hexdigest().upper()
