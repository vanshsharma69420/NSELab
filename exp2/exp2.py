import hashlib
import os

sender_file = "/home/raghu/Documents/network-security-lab/exp2/sender.txt"

# Step 1: Choose hash algorithm (NEW FEATURE 1)
print("Choose hash algorithm (sha256 / sha1 / md5): ")
algo = input("Algorithm: ").strip().lower()
if algo not in ["sha256", "sha1", "md5"]:
    print("Invalid algorithm, defaulting to sha256.")
    algo = "sha256"

try:
    with open(sender_file, "rb") as f:
        sender_data = f.read()
        sender_hash = getattr(hashlib, algo)(sender_data).hexdigest()
except FileNotFoundError:
    print(f"Sender file '{sender_file}' not found.")
    exit(1)

# Step 2: Get receiver file and compare hashes
receiver_file = input("Enter the receiver file path: ").strip()
try:
    with open(receiver_file, "rb") as f:
        receiver_data = f.read()
        receiver_hash = getattr(hashlib, algo)(receiver_data).hexdigest()

    print(f"\nSender Hash   : {sender_hash}")
    print(f"Receiver Hash : {receiver_hash}")

    # NEW FEATURE 2: File size comparison warning
    sender_size = os.path.getsize(sender_file)
    receiver_size = os.path.getsize(receiver_file)
    print(f"\nSender File Size   : {sender_size} bytes")
    print(f"Receiver File Size : {receiver_size} bytes")
    if sender_size != receiver_size:
        print("⚠ Warning: File sizes differ. Possible tampering.")

    if receiver_hash == sender_hash:
        print("\nData integrity verified ✔ Hashes match.")
    else:
        print("\nData integrity verification failed ✘ Hashes do not match.")

except FileNotFoundError:
    print("Receiver file not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
