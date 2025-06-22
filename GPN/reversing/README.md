# The old way (<font color=green> </font>)


## Description
Back then, one had to put a lot of manual work in to get efficient code. Nowadays, they say the compiler just does it. But I don't trust them...


## Tools Used

- Ghidra: Decompiled the ELF binary to analyze compute_secret logic.
- GDB: Located the FLAG variable and verified memory layout.
- Python (NumPy): Built and solved a system of linear equations to reverse the flag computation logic.

## Skills Learned

- Reversing statically linked, non-stripped ELF binaries.

## Steps Taken
1. Used file, checksec, and strings to inspect the ELF binary structure and contents.
2. Located compute_secret function in Ghidra and analyzed its control flow and data transformations.
3. Identified FLAG as a global array and dumped its original contents using nm, readelf, and dd.
4. Converted dumped bytes into 64-bit integers representing the encoded flag using python [script](convert.py).
5. Wrote a Python [solver](solver.py) using NumPy to reverse-engineer the expected input from the FLAG values.
6. Reconstructed and verified the final flag