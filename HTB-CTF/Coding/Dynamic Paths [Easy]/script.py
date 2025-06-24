from pwn import *

def min_path_sum(i, j, values):
    # Build grid
    grid = [[0] * j for _ in range(i)]
    idx = 0
    for r in range(i):
        for c in range(j):
            grid[r][c] = values[idx]
            idx += 1

    # DP grid
    dp = [[0] * j for _ in range(i)]
    dp[0][0] = grid[0][0]

    # Fill first row
    for c in range(1, j):
        dp[0][c] = dp[0][c-1] + grid[0][c]

    # Fill first column
    for r in range(1, i):
        dp[r][0] = dp[r-1][0] + grid[r][0]

    # Fill rest
    for r in range(1, i):
        for c in range(1, j):
            dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]

    return dp[i-1][j-1]

r = remote('94.237.121.185', 32832)

while True:
    line = r.recvline().decode()
    print(line.strip())

    if line.strip().startswith("Test"):
        dims = r.recvline().decode().strip()
        print(dims)
        i, j = map(int, dims.split())

        values_line = r.recvline().decode().strip()
        print(values_line)
        values = list(map(int, values_line.split()))

        ans = min_path_sum(i, j, values)
        print(f"Sending answer: {ans}")
        r.sendline(str(ans))