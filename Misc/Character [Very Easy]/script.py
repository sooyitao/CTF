import socket

HOST = '94.237.54.192'
PORT = 54763
FLAG_LEN = 1000  # Adjust upper bound if needed

flag = ''

try:
    with socket.create_connection((HOST, PORT), timeout=10) as s:
        s.settimeout(5)  # Read timeout per response

        # Consume initial prompt (e.g., menu or intro message)
        initial_data = s.recv(1024).decode()
        print("[INFO] Initial server response:\n", initial_data)

        for i in range(FLAG_LEN):
            s.sendall(f"{i}\n".encode())

            try:
                response = s.recv(1024).decode()
            except socket.timeout:
                print(f"[{i}] => Timeout receiving response")
                break

            char_found = False
            for line in response.splitlines():
                if "character" in line.lower():
                    char = line.strip()[-1]
                    flag += char
                    print(f"[{i}] => {char}")
                    char_found = True
                    break

            if not char_found:
                print(f"[{i}] => No character returned, stopping.")
                break

            if flag.endswith('}'):
                break

except Exception as e:
    print(f"[ERROR] Connection failed: {e}")

print(f"\nFinal flag: {flag}")

