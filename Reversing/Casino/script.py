import ctypes
from pwn import *

libc = ctypes.CDLL('libc.so.6')

mapping = {}
for i in range(255):
    libc.srand(i)
    mapping[libc.rand()] = chr(i)

flag = ""

e = ELF("./casino", checksec=False)
for j in range(29):
    # Index into the `check` array by multiplying the index by 4
    # Use `e.u32()` to extract the 32-bit integer
    val = e.u32(e.sym["check"] + j * 4)
    flag += mapping[val]
print(flag)