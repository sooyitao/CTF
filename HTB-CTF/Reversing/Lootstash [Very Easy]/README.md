# Lootstash  (<font color=green> Very Easy </font>)


## Description
A giant stash of powerful weapons and gear have been dropped into the arena - but there's one item you have in mind. Can you filter through the stack to get to the one thing you really need?


## Tools Used

- `strings`
- `grep`
- `checksec`
- `file`

## Skills Learned

- Using `strings` and `grep` to locate hidden or embedded flags

## Steps Taken
1. Ran `file stash` and `checksec --file=stash` to determine binary type, architecture, and security features.

2. Confirmed it was a 64-bit PIE-enabled, NX-enabled ELF binary without canaries and not stripped, making static analysis easier.

3. Used `strings stash` to extract printable strings from the binary.

4. Filtered the output with `strings stash | grep "HTB"` to locate the flag pattern HTB{...}.