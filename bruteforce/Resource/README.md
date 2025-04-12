### Where:  

`/?page=signin`

### How:  

1. Found no other hints so we decided to bruteforce
2. Develop a [script](https://github.com/Kuninoto/42_darkly/blob/master/bruteforce/Resource/bruteforce.py) to bruteforce the credentials using the [rockyou wordlist](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
3. Run it
4. Found!

### Fixable by:  

1. Having a stronger password:
    - Bigger, to prevent bruteforcing;
    - Not a word or phrase, to prevent dictionary attacks.
2. Rate limit requests
