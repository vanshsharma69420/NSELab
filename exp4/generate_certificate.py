import subprocess
import os

# Ask user for certificate details
country = input("Country Code (e.g., IN): ")
state = input("State: ")
locality = input("Locality/City: ")
organization = input("Organization Name: ")
org_unit = input("Organizational Unit: ")
common_name = input("Common Name (e.g., localhost): ")

# Absolute paths
BASE_DIR = "/home/raghu/Documents/NSELab/exp4"
PRIVATE_KEY_FILE = os.path.join(BASE_DIR, "private.key")
CSR_FILE = os.path.join(BASE_DIR, "request.csr")   # NEW FEATURE 2
CERT_FILE = os.path.join(BASE_DIR, "certificate.crt")

# NEW FEATURE 1: Create directory if missing
os.makedirs(BASE_DIR, exist_ok=True)

def run_command(command, input_text=None):
    """Run a shell command and return its output."""
    result = subprocess.run(
        command,
        input=input_text,
        text=True,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
    return result.stdout

# 1. Generate private key (RSA 2048)
print("Generating private key...")
run_command(f"openssl genpkey -algorithm RSA -out \"{PRIVATE_KEY_FILE}\" -pkeyopt rsa_keygen_bits:2048")

# 2. Create CSR (Certificate Signing Request) – NEW FEATURE 2
print("Generating CSR...")
subject = f"/C={country}/ST={state}/L={locality}/O={organization}/OU={org_unit}/CN={common_name}"
run_command(f"openssl req -new -key \"{PRIVATE_KEY_FILE}\" -out \"{CSR_FILE}\" -subj \"{subject}\"")

# 3. Generate self-signed certificate (valid 365 days)
print("Generating self-signed certificate...")
run_command(f"openssl req -x509 -key \"{PRIVATE_KEY_FILE}\" -in \"{CSR_FILE}\" -out \"{CERT_FILE}\" -days 365")

print("Certificate and CSR generated successfully.")
