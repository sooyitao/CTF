# Dynastic (<font color=green> Very Easy </font>)


## Description
You find yourself trapped inside a sealed gas chamber, and suddenly, the air is pierced by the sound of a distorted voice played through a pre-recorded tape. Through this eerie transmission, you discover that within the next 15 minutes, this very chamber will be inundated with lethal hydrogen cyanide. As the tape’s message concludes, a sudden mechanical whirring fills the chamber, followed by the ominous ticking of a clock. You realise that each beat is one step closer to death. Darkness envelops you, your right hand restrained by handcuffs, and the exit door is locked. Your situation deteriorates as you realise that both the door and the handcuffs demand the same passcode to unlock. Panic is a luxury you cannot afford; swift action is imperative. As you explore your surroundings, your trembling fingers encounter a torch. Instantly, upon flipping the switch, the chamber is bathed in a dim glow, unveiling cryptic letters etched into the walls and a disturbing image of a Roman emperor drawn in blood. Decrypting the letters will provide you the key required to unlock the locks. Use the torch wisely as its battery is almost drained out!


## Tools Used

- Python

## Skills Learned

- Understanding and reversing positional Caesar ciphers

## Steps Taken
1. Analyzed the `encrypt()` function in `source.py` to understand how each character was shifted based on its position.
    - only alphabetic characters were shifted; symbols remained unchanged
2. Reversed the shifting logic by subtracting the position index instead of adding it.
3. Wrote a [script](decrypt.py) with decrypt() function to reconstruct the original message.
4. Wrapped the output in the HTB{} flag format to retrieve the final flag