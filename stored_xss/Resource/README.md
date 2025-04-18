### Where:  

`/?page=feedback`

### How:  

1. Change `name` field's `maxlength` to a very big number
2. Send `<img src="x" onerror="alert(document.cookie);">` on name
3. Found!

**NOTE:** This level is very buggy. We've managed to get the flag with this payload sometimes, but not everytime. We've tried several others that also work - even by just sending "script" or "alert" in any of the input fields, which is obviously a bug of the ISO.  

### Fixable by:  

1. Checking form fields' max lengths both client and server side
2. Properly sanitizing user input
