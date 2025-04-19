### Where

`/robots.txt`, `/whatever` and `/admin`

### How

1. Randomly decided to check if there was a `robots.txt` file, possibly trying to avoid crawlers to crawl sensitive pages
2. Found there was one, and that it shows two routes
3. Visit `/whatever`
4. Found that it's a directory that has listing and holds a `htpasswd` file
5. Opening it, we see an username and a password
6. Pasting the password on [Crackstation](https://crackstation.net/), we see it's a md5 and its value
7. Normally, `htpasswd` holds the credentials for admins so we decided to try the credentials on `/admin`
8. Found!

### Fixable by

1. Disabling directory listing
2. Securing files that contain sensitive information
