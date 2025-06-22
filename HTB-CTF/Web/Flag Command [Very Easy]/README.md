# Flag Command (<font color=green>Very Easy</font>)


## Description
Embark on the "Dimensional Escape Quest" where you wake up in a mysterious forest maze that's not quite of this world. Navigate singing squirrels, mischievous nymphs, and grumpy wizards in a whimsical labyrinth that may lead to otherworldly surprises. Will you conquer the enchanted maze or find yourself lost in a different dimension of magical challenges? The journey unfolds in this mystical escape!

## Tool Used
- Web Browser

## Skill Learned
- Basic Code Analysis

## Steps
1. Look through .js files using developer tools
2. main.js contains
    ```
        if (availableOptions[currentStep].includes(currentCommand) || availableOptions['secret'].includes(currentCommand)) {
            ...

                if(data.message.includes('HTB{')) {
                    playerWon();
                    fetchingResponse = false;

                    return;
                }
            ...
    ```
3. So if secret command is entered, the flag will be displayed
4. Looking at api/options
    ```
    "secret": [
      "Blip-blop, in a pickle with a hiccup! Shmiggity-shmack"
    ]
    ```
5. Therefore entering "Blip-blop, in a pickle with a hiccup! Shmiggity-shmack", flag is displayed.

