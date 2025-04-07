### Where:  

`/?page=member`

### How:  

1. Found the `member` page by clicking on the "Members" button on the home page
2. Check the network tab
3. Randomly noticed a cookie called `I_am_admin`
4. Pasting its value on [Crackstation](https://crackstation.net/), we see that it's a md5 of `false`
5. Change it to a md5 of `true`
6. Send a request again
7. Found!

### Fixable by:  

1. Not storing privileges in cookies at all
2. Using server-side sessions to track user authentication
3. Storing users' privileges in the database
4. Verifying permissions server-side on each request 
