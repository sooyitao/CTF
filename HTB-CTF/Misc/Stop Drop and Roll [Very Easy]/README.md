# Stop Drop and Roll  (<font color=green>Very Easy </font>)


## Description
The Fray: The Video Game is one of the greatest hits of the last... well, we don't remember quite how long. Our "computers" these days can't run much more than that, and it has a tendency to get repetitive...


## Tools Used

- Python
- pwntools

## Skills Learned

- Automating CTF interaction using pwntools
- String parsing and cleanup

## Steps Taken
1. Connected to the remote service using nc to understand input/output format.
2. Analyzed challenge instructions to map each keyword to the correct response.
3. Wrote a Python [script](script.py) using pwntools to automate connection and interaction.
4. Captured the scenarios and mapped each to its corresponding action using a dictionary.
5. Joined the mapped actions in the correct format and sent the result back.