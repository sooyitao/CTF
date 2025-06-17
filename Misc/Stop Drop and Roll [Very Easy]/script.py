from pwn import *

# Connect to the remote host
conn = remote("94.237.54.240", 44704)

# Mapping from threat to action
actions = {
    "GORGE": "STOP",
    "PHREAK": "DROP",
    "FIRE": "ROLL"
}

# Wait for initial prompt and send 'y'
conn.recvuntil(b"(y/n)")
conn.sendline(b"y")
conn.recvuntil(b"Ok then! Let's go!")

while True:
    try:
        line = conn.recvline(timeout=5).decode().strip()
        if not line:
            continue

        print("Challenge:", line)

        conn.recvuntil(b"What do you do?")

        challenge = line
        threats = [x.strip() for x in challenge.split(",")]
        response = "-".join([actions[t] for t in threats])
        print("Response:", response)
        conn.sendline(response.encode())

    except EOFError:
        print("Connection closed.")
        break
