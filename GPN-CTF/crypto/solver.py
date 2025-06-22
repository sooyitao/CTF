from Crypto.Util.number import long_to_bytes

# Given values
n = 0xc615bebc59f778947dbfb17bd76c3d9d1c17ddfa385504df58bbfd8fa7e1639ae73c2e6e58e8868ecc53c6b730a5aaeaba505b66986152664ae09ed95f27df8c8989ca11da33981bd00ff43dc5fd325ebb0f40e602f437c9a8569c6df68f5c17ee336a0dcbc81a4b2c7c713714a080c497d502b707b6bbbe0fb045ea6edae65f196bc21c3766b5f0a1d2013fa3ce0b368325ef5ebcb38e9772f3384a547dac7698fb84055f7c51b5754facd100ad91254bb100bd441c3328f7a4d8a7a6885908e1cb95a4ce3651f773619cc0aa7a3e57754c6730883f36519b4001c6413d3c26df5f8c341e6c6a4cda202de10b0212637e6878f8d9a092c005985b9a9aecb639
e = 0x10001
c = 0xb0fc0c33e8dc67bf6efaa1ce539cceeb90e043eefe20b9bb2043279edf4e98880c4a3a887d91521b56687660a35d2d74858ac2e7ce0c1dbe3551bd0989f143f8ea1d18c970961a801b8f0764b730fb4b76520987f98a081751b6d4b175dacb8780d71dfe5cafe24f1754b72288ced75409c395f049073fa06cd8bc220aee11eff092cd80fa736b01ec856a97291599856a01b351a5bc36137ce4f23148a1e2d26d769471997bc265bc10945be00e82894e1d3e32092d7739a14af9d6e6497bde8f10eec400d153ffcb85181a691a4f58c8a427d2383c0ba6aab01669263771463db747467af6f1232f6f83a9b0387ad735704bb83ceba521a4f152f60fb0aa40
V = [6, 5, 4, 1, 1, 6, 3, 6, 1, 4, 3, 6, 4, 2, 2, 5, 2, 5, 6, 1, 4, 4, 5, 2, 4, 1, 6, 2, 6, 2, 0, 1, 3, 5, 0, 1, 1, 0, 0, 6, 4, 0, 4, 1, 2, 5, 0, 6, 5, 0, 1, 0, 2, 3, 6, 0, 2, 1, 5, 5, 5, 6, 2, 5, 2, 2, 2, 3, 0, 4, 4, 3, 5, 0, 1, 1, 6, 1, 0, 6, 4, 3, 1, 2, 2, 5, 5, 6, 2, 2, 1, 5, 3, 4, 3, 0, 3, 1, 3, 6, 4, 1, 5, 2, 5, 4, 6, 3, 0, 5, 5, 5, 4, 4, 5, 4, 4, 3, 1, 6, 6, 1, 3, 6, 5, 4, 4, 6, 2, 3, 0, 6, 5, 6, 2, 0, 4, 4, 6, 1, 5, 2, 6, 5, 1, 3, 1, 5, 1, 3, 0, 6, 5, 2, 5, 3, 0, 1, 2, 2, 3, 2, 3, 4, 5, 4, 1, 0, 0, 6, 0, 4, 3, 0, 2, 5, 3, 1, 6, 3, 0, 6, 3, 6, 3, 6, 6, 3, 3, 6, 1, 0, 1, 1, 0, 3, 4, 6, 5, 6, 2, 3, 1, 5, 2, 2, 0, 1, 6, 5, 6, 6, 6, 2, 5, 3, 0, 0, 5, 4, 1, 6, 2, 3, 3, 6, 3, 0, 2, 0, 0, 3, 5, 3, 0, 2, 5, 4, 3, 0, 1, 5, 6, 1, 2, 4, 4, 0, 3, 1, 0, 5, 2, 5, 4, 6, 1, 5, 5, 0, 2, 1, 2, 4, 3, 4, 1, 0, 5, 4, 4, 0, 2, 1, 2, 3, 4, 2, 3, 0, 4, 3, 5, 3, 3, 3, 6, 0, 4, 0, 5, 4, 2, 2, 4, 5, 5, 3, 6, 2, 1, 0, 0, 0, 5, 1, 5, 6, 0, 3, 1, 6, 5, 1, 1, 5, 4, 1, 0, 5, 3, 1, 6, 6, 1, 3, 4, 5, 5, 3, 1, 3, 4, 4, 4, 1, 0, 1, 1, 6, 5, 5, 4, 2, 5, 4, 0, 1, 5, 2, 4, 2, 2, 0, 4, 0, 2, 1, 5, 0, 5, 1, 4, 4, 0, 0, 0]

# Convert n to base-7 digits
def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(int(n % b))
        n = n // b
    return digits

n_base7 = number_to_base(n, 7)
n_base7 = n_base7 + [0] * (366 - len(n_base7))  # Pad to 366 digits

# Initialize pp and qq
pp = [None] * 366
qq = [None] * 366

# We'll use a recursive approach to find pp and qq
def solve(i, carry):
    if i == 366:
        # All digits filled, check if p * q == n
        p = sum(pp[k] * (7 ** k) for k in range(366))
        q = sum(qq[k] * (7 ** k) for k in range(366))
        return p * q == n
    for a in range(7):
        pp[i] = a
        qq[i] = (V[i] - a) % 7
        # Calculate the sum of products for digit i
        total = carry
        for k in range(i + 1):
            total += pp[k] * qq[i - k]
        current_digit = total % 7
        if current_digit == n_base7[i]:
            new_carry = total // 7
            if solve(i + 1, new_carry):
                return True
    return False

if solve(0, 0):
    p = sum(pp[k] * (7 ** k) for k in range(366))
    q = sum(qq[k] * (7 ** k) for k in range(366))
    print(f"Found p: {p}")
    print(f"Found q: {q}")
    # Verify p and q
    assert p * q == n, "Factorization failed"
    # Compute phi(n)
    phi = (p - 1) * (q - 1)
    # Compute private key d
    d = pow(e, -1, phi)
    # Decrypt the ciphertext
    flag = pow(c, d, n)
    print(f"Flag: {long_to_bytes(flag).decode()}")
else:
    print("Failed to factorize n")