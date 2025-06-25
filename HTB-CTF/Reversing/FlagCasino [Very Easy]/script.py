from ctypes import CDLL
from pwn import *

libc = CDLL("libc.so.6")

# Dumped from GDB
target_vals = [
    608905406,   183990277,   286129175,   128959393,
    1795081523,  1322670498,  868603056,   677741240,
    1127757600,  89789692,    421093279,   1127757600,
    1662292864,  1633333913,  1795081523,  1819267000,
    1127757600,  255697463,   1795081523,  1633333913,
    677741240,   89789692,    988039572,   114810857,
    1322670498,  214780621,   1473834340,  1633333913
]

# Brute-force seeds
payload = []
for target in target_vals:
    for seed in range(256):
        libc.srand(seed)
        if libc.rand() == target:
            payload.append(chr(seed))
            break
    else:
        payload.append('?')  # fallback if not found

final_input = ''.join(payload)
print(f"[+] Brute-forced input: {final_input!r}")

# Send to binary
p = process("./casino")

for c in final_input:
    p.send(c)

p.interactive()
