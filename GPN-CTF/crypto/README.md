# hinting (<font color=green> </font>)


## Description
C'mon take a hint, you want to play that.


## Tools Used

- Python
- RSA decryption logic

## Skills Learned

- Exploiting partial leakage in RSA
- Base conversions (especially base-7)
- Implementing efficient backtracking algorithms for number reconstruction


## Steps Taken
### 1. Problem Analysis  
We were given:  
n: RSA modulus (product of two 1024-bit primes p and q).  
e: Public exponent (0x10001).  
c: Ciphertext (pow(FLAG, e, n)).  
V: A vector where each element is (pp[i] + qq[i]) % 7 (sum of base-7 digits of p and q).

Goal: Recover p and q from n and V, then decrypt c to get the flag.

### 2. Understanding the Leak
- p and q are 1024-bit primes, each represented in base-7 with 366 digits (padded).

- V[i] = (pp[i] + qq[i]) % 7 gives the sum of the i-th digits of p and q in base-7.

- We need to reconstruct p and q from this information.

### 3. Approach
- Since we know n = p * q and the digit-wise sums V[i], we can:
    1. Convert n to base-7 to compare digits.

    2. Reconstruct p and q digit-by-digit using backtracking:

    3. For each digit position i, try all possible pp[i] (0-6).

    4. Compute qq[i] = (V[i] - pp[i]) % 7.

    5. Verify that the multiplication constraints (including carries) match n's base-7 digits.

    6. Decrypt c once p and q are known.

### 4. Implementation
We wrote a Python [script](solver.py) to:
- Convert n to base-7:

- For each digit position, try all possible pp[i] and compute qq[i].

- Check if the partial product matches n's digits.

- Decrypt the flag:

    1. Compute phi(n) = (p-1)*(q-1).

    2. Compute d = pow(e, -1, phi).

    3. Decrypt flag = pow(c, d, n).