# Criticalops (<font color=green> Very Easy</font>)


## Description
Criticalops is a web application designed to monitor several critical infrastructure of XYZ region. Users usualy use this website to report for unusual behavioral, or we also called it ticket. They've asked you to hunt for any potential security issues in their application and retrieve the flag stored in their site.  
📝 Related Bug Bounty Reports  
Bug Report #1 - [JWT client-side](https://hackerone.com/reports/638635)


## Tools Used

- Browser Developer Tools (to inspect JavaScript and find the hardcoded key)

- `pyjwt` Python library (to generate HS256 tokens)

- curl or Postman (to send HTTP requests with forged token)

## Skills Learned

- Identifying and exploiting JWT vulnerabilities

- Extracting secrets from client-side JavaScript

- Forging valid JWTs using HS256 and a known secret

## Steps Taken
1. From the .js file, the line:  
`let a = new TextEncoder().encode("SecretKey-CriticalOps-2025");`  
means that the JWTs in this web app are signed using the key: `SecretKey-CriticalOps-2025`
2. Based on the code:  
    ```
    async function n(e) {
    return await new s.P(e)
        .setProtectedHeader({ alg: "HS256" })
        .setIssuedAt()
        .setExpirationTime("8h")
        .sign(a);
    }
    ```
    That a is the signing key. So the full JWT creation uses:  
    Algorithm: `HS256`  
    Secret: `"SecretKey-CriticalOps-2025" ` 
3. Forge your own JWT using [python](jwttoken.py)
4. Use the token with a [request](jwttoken.py)
5. Flag is found in the output