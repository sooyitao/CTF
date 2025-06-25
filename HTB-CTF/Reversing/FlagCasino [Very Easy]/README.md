# FlagCasino (<font color=green> Very Easy </font>)


## Description

The team stumbles into a long-abandoned casino. As you enter, the lights and music whir to life, and a staff of robots begin moving around and offering games, while skeletons of prewar patrons are slumped at slot machines. A robotic dealer waves you over and promises great wealth if you can win - can you beat the house and gather funds for the mission?

## Tools Used

- GDB (for disassembly and memory inspection)
- Pwntools (for process automation and interaction)
- Ghidra (to get disassembly and decompilation)

## Skills Learned

- Understanding and bypassing PIE
- Brute forcing inputs by reversing PRNG outputs

## Steps Taken
1. Identified binary type and protections with file and checksec.
2. Import the binary into Ghidra to understand `main` program logic.
2. Used GDB to find base address of the binary in memory (due to PIE).
3. Calculated real runtime addresses to dump the check[] array used for validation.
4. Extracted the full 28 integers from the check[] array in memory.
5. Created Python [script](script.py) using ctypes to call srand() and rand() and find seed values producing check[] outputs.
6. Ran the script on WSL to get the full flag printed by the binary.