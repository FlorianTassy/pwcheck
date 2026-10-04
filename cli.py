import argparse
import getpass
import sys

from entropy import characters_pool_size, families, naive_entropy
from hibp import sha1_hash, pwned_count

def ask_password():
    try:
        password = getpass.getpass("Password: ")
    except (EOFError, KeyboardInterrupt):
        return None
    
    if password == "":
        print("Password is empty")
        print("\nAborted")
        return None

    return password

def main(argv=None):
    parser = argparse.ArgumentParser(prog="pwcheck", description="Password strength checker.")
    parser.parse_args(argv)
 
    password = ask_password()
    if password is None:
        return 2
 
    entropy = naive_entropy(password)

    print("Entropy = " + str(entropy))
    if entropy < 75:
        print("You should try a password with more entropy, less than 75 is not secure enought")

    print("Seen " + str(pwned_count(password)) + " times in known data breaches.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
