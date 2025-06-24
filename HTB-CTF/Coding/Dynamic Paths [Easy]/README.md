# Dynamic Paths (<font color=green>Easy</font>)


## Description
On your way to the vault, you decide to follow the underground tunnels, a vast and complicated network of paths used by early humans before the great war. From your previous hack, you already have a map of the tunnels, along with information like distances between sections of the tunnels. While you were studying it to figure your path, a wild super mutant behemoth came behind you and started attacking. Without a second thought, you run into the tunnel, but the behemoth came running inside as well. Can you use your extensive knowledge of the underground tunnels to reach your destination fast and outrun the behemoth?


## Tools Used

- Python
- Dynamic Programming (for grid-based pathfinding)

## Skills Learned

- Implementing dynamic programming for minimum path problems
- Automating input/output to solve multiple test cases in a loop

## Steps Taken
1. Read the challenge prompt and understood the movement constraints (only right or down).
2. Implemented a dynamic programming function to compute the minimum path sum through a grid.
3. Used pwntools to connect to the remote challenge server via nc (netcat-style socket).
4. Parsed each test case: read grid dimensions and values, reshaped them into a 2D list.
5. Applied the DP algorithm to calculate the optimal path cost.
6. Sent the result back to the server and repeated for multiple test cases using python [script](script.py)