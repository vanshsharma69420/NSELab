import hashlib
import random
import time

# Each user has their own secret key
user_secrets = {
    "alice": "alice_secret_key",
    "bob": "bob_secret_key"
}

# Store used nonces to prevent reuse attacks
used_nonces = set()

# NEW FEATURE 1: Nonce expiration store
nonce_expiration = {}  
NONCE_VALID_SECONDS = 10

# NEW FEATURE 2: User lockout mechanism
failed_attempts = {"alice": 0, "bob": 0}
LOCKOUT_LIMIT = 3

def generate_nonce():
    return str(random.randint(100000, 999999))

def hash_response(nonce, secret, username):
    data = nonce + secret + username
    return hashlib.sha256(data.encode()).hexdigest()

# ---------------- CLIENT -----------------
username = "bob"
secret = user_secrets[username]

# Step 1: Server generates nonce
nonce = generate_nonce()
nonce_expiration[nonce] = time.time() + NONCE_VALID_SECONDS   # Store expiration
print("Server sends nonce:", nonce)

# Step 2: Client creates response
client_response = hash_response(nonce, secret, username)
print(f"Client ({username}) sends response: {client_response}")

# ---------------- SERVER -----------------
# Step 3: Server verifies

# Check lockout
if failed_attempts[username] >= LOCKOUT_LIMIT:
    print(f"User '{username}' is LOCKED OUT due to multiple failed attempts.")
else:
    # Check nonce reuse
    if nonce in used_nonces:
        print("Replay attack detected: Nonce already used")

    # Check nonce expiration (NEW)
    elif time.time() > nonce_expiration[nonce]:
        print("Nonce expired: Authentication rejected")

    else:
        expected_response = hash_response(nonce, user_secrets[username], username)

        if client_response == expected_response:
            print(f"Authentication Successful for user {username}")
            used_nonces.add(nonce)  # Mark nonce as used
            failed_attempts[username] = 0  # reset failures
        else:
            print("Authentication Failed")
            failed_attempts[username] += 1
            print(f"Failed attempts: {failed_attempts[username]}")
