# Jailbreak (<font color=green>Very Easy</font>)


## Description
The crew secures an experimental Pip-Boy from a black market merchant, recognizing its potential to unlock the heavily guarded bunker of Vault 79. Back at their hideout, the hackers and engineers collaborate to jailbreak the device, working meticulously to bypass its sophisticated biometric locks. Using custom firmware and a series of precise modifications, can you bring the device to full operational status in order to pair it with the vault door's access port. The flag is located in /flag.txt

## Tool Used

- Web Browser

## Skill Learned

- XML External Entity (XXE) vulnerability

## Steps
1. Identify the page where scripts can be input and its vulnerability. In this case, XML can be enter which is vulnerable to XML External Entity (XXE).
2. Craft the external entity declaration. 
    ```
    <!DOCTYPE FirmwareUpdateConfig [
    <!ENTITY xxe SYSTEM "file:///flag.txt">
    ]>
    ```
3. Insert the entity reference ``&xxe;`` inside valid XML element. Since they display the version after successful update, entity reference can be in version to display the flag when the payload is submitted.
    ```
    <FirmwareUpdateConfig>
        <Firmware>
            <Version>&xxe;</Version>
            ...
        </Firmware>
    ```
4. Craft payload. Add external entity declaration at start and preserve the rest of the XML structure exactly as expected only changing version XML element.
5. Submit the crafted XML configuration file and retrieve the flag
