import numpy as np

original_FLAG = [
    71331, 142484, 213504, 284536, 354910, 425892, 493787, 564176, 638649, 704120,
    779251, 843144, 915044, 990220, 1044255, 1118112, 1188113, 1249272, 1314401, 1390040,
    1447845, 1533092, 1606274, 1655472, 1713800, 1778712, 1843290, 1958488, 1978148, 2052060,
    2122167, 2185536, 2265879, 2366400, 2436595, 2470680, 2565210, 2642520, 2649309, 2656080,
]

N = len(original_FLAG)
weights = np.zeros((N, N), dtype=np.int64)

for i in range(N):
    for j in range(N):
        weights[i][j] = 0 if i == j else j*i + j + i + 1

target = np.array([original_FLAG[i] - ((i % 3)) for i in range(N)], dtype=np.int64)


try:
    input_solution = np.linalg.solve(weights, target)
except np.linalg.LinAlgError:
    input_solution = np.linalg.lstsq(weights, target, rcond=None)[0]

input_bytes = np.round(input_solution) % 256
input_bytes = input_bytes.astype(np.uint8)

print("Candidate input bytes:")
print(input_bytes.tolist())

def verify(input_bytes):
    for i in range(N):
        s = original_FLAG[i]
        for j in range(N):
            s -= weights[i][j] * input_bytes[j]
        if s == 0:
            print(f"FLAG[{i}] zeroed out! Input invalid.")
            return False
    return True

if verify(input_bytes):
    print("Valid input found!")
    flag_str = ''.join(chr(b) for b in input_bytes.tolist())
    print(flag_str)
else:
    print("No valid input found, try adjusting target or approach.")
    flag_str = ''.join(chr(b) for b in input_bytes.tolist())
    print(flag_str)
