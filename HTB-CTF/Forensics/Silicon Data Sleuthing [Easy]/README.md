# Silicon Data Sleuthing (<font color=green>Easy</font>)


## Description
In the dust and sand surrounding the vault, you unearth a rusty PCB... You try to read the etched print, it says Open..W...RT, a router! You hand it over to the hardware gurus and to their surprise the ROM Chip is intact! They manage to read the data off the tarnished silicon and they give you back a firmware image. It's now your job to examine the firmware and maybe recover some useful information that will be important for unlocking and bypassing some of the vault's countermeasures!


## Tools Used

- binwalk, squashfs and Jefferson to extract firmware image
- grep for searching configuration files

## Skills Learned

- Extracting network configuration from embedded device firmware
- Filtering and formatting command output

## Steps Taken
1. Based on the description, we can assume that we are given an OpenWRT firmware image. To examine such an image we need binwalk and squashfs which can be installed using:
    ```
    sudo apt install binwalk squashfs-tools
    ```
2. Run `binwalk -eM chal_router_dump.bin` to extract
3. What version of OpenWRT runs on the router (ex: 21.02.0)?  
    Run `grep -ri 'DISTRIB_RELEASE' _chal_router_dump.bin.extracted/` and version is displayed
4. What is the Linux kernel version (ex: 5.4.143)?  
    Run `cd _chal_router_dump.bin.extracted/squashfs-root/lib/modules/` and the folder name is the version
5. What's the hash of the root account's password, enter the whole line (ex: root:$2$JgiaOAai....)?  
    First install Jefferson, the extractor binwalk uses for JFFS2, using `sudo apt install python3-jefferson`. Run `binwalk -e 7C0000.jffs2` to extract then `grep -r "root" _7C0000.jffs2.extracted/` to find the hash.
6. What is the PPPoE username and password?  
    Run `grep -r "pppoe" _7C0000.jffs2.extracted/` which outputs `grep: _7C0000.jffs2.extracted/jffs2-root/work/work/#2: Permission denied`. Check its contents using `cat _7C0000.jffs2.extracted/jffs2-root/work/work/#4/network` and both username and password can be found in it.
7. What is the WiFi SSID?  
    Run `grep -r "ssid" _7C0000.jffs2.extracted/` and version is shown.
8. What is the WiFi Password?  
    From previous question, we know the file where WiFi info is store so run `cat _7C0000.jffs2.extracted/jffs2-root/work/work/#4/wireless` and find the password.
9. What are the 3 WAN ports that redirect traffic from WAN -> LAN (numerically sorted, comma sperated: 1488,8441,19990)?  
    Run `grep -r "redirect" _7C0000.jffs2.extracted/` to find relevent files then `cat _7C0000.jffs2.extracted/jffs2-root/work/work/#b` to display WAN redirect traffic details and the ports are under option src_dport.