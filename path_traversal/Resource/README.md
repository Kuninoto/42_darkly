### Where  

`/?page=../../../../../../../../etc/passwd`

### How  

1. Try to escape out of the possible location where the site files are being served from (possibly `/var/www/html`), with `../`
2. Try the same with `../../`
3. The alert displays a different message... Huh?
4. Since the message keeps changing, we kept adding `../`
5. When it didn't change anymore, we've tried common sensible files that we might want to find
6. Try with `/etc/passwd`
7. Found!

### Fixable by  

1. Sanitize routes/paths
2. Configuring proper file system restrictions
3. Configuring proper web server directory permissions
