# Getting Started (<font color=green>Very Easy</font>)


## Description
Get ready for the last guided challenge and your first real exploit. It's time to show your hacking skills.


## Tools Used

- pwntools 
- gdb 

## Skills Learned

- Identifying and exploiting buffer overflows

## Steps Taken
1. Ran `checksec` to identify security mitigations in the binary.
2. Used `gdb` to list symbols and locate the `win` function.
3. Using GDB, I disassembled main to understand the stack layout and where input is read.
    ```
    0x00000000000016a4 <+4>: sub $0x30, %rsp      ; allocate 48 bytes on stack
    ...
    0x00000000000017b4 <+276>: call __isoc99_scanf ; read input into buffer
    ```
4. Identify Buffer Location
    - Input buffer is at `[rbp - 0x30]`, i.e., 48 bytes below base pointer.
    - The saved base pointer (`rbp`) and return address (`rip`) are stored above [rbp].
    - A guard variable (with value `0xdeadbeef`) is stored at [`rbp` - 0x8].
5. Calculate Offset to Control Flow
    - To overwrite the guard at [rbp - 8], need to overflow at least 40 bytes (48 - 8).
    - To reach the saved rbp (8 bytes) and then the saved return address (rip) another 8 bytes, total offset becomes:
        - Buffer size: 48 bytes
        - Guard: 8 bytes
        - Saved rbp: 8 bytes
        - Total: 64 bytes to rip
    - Adding these up, total offset to overwrite return address is 72 bytes.
6. Validate with Exploit Payload
Using the offset: `payload = b'A' * 72 + p64(win_addr)`
Sending this overwrote the return address with win() and triggered the flag print.
