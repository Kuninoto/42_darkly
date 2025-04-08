### Where:  

`/?page=feedback`

### How:  

1. Change `name` field's `maxlength`
2. Send `<img src="x" onerror="alert(document.cookies);">` on name
3. Found!

### Fixable by:  

1. Checking form fields' max lengths both client and server side
2. Properly sanitizing user input
