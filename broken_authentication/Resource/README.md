### Where  

`/?page=recover`

### How  

1. Check page source
2. Edit `<form>`, setting another email address
3. Found!

### Fixable by  

1. Having the destination email be given thru input
2. Validating if it exists in the database but **always** return the same ambiguous
message to the user to not be explicit about whether the email is registered
or not e.g. "If an account exists with this email address, you will receive password reset instructions."
3. Send a recovery token and save an expiry on the database 
