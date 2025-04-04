### Where:  

`/?page=../../../../../../../../etc/passwd`

### How:  

1. Try to escape out of the possible location where the site files are being served from with `../`
2. Try the same with `../../`
3. The alert displays a different message... Huh?
4. Since the message keeps changing, we kept adding `../`
5. When it didn't change anymore, we've tried common files that we might want to check
6. Try with `/etc/passwd`
7. Found!
