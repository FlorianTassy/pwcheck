import argparse
import getpass
import sys

from entropy import characters_pool_size, families, naive_entropy
from hibp import sha1_hash, pwned_count

MIN_ENTROPY = 75

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

    print(f"Entropy: {entropy:.1f} bits")
    if entropy < MIN_ENTROPY:
        print("You should try a password with more entropy, less than 75 is not secure enought")

    times_pwned= pwned_count(password)

    if times_pwned > 0:
        print(f"Seen {times_pwned:,} times in known data breaches.")
        print("Do not use this password.")
    else:
        print("Not found in known data breaches.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
