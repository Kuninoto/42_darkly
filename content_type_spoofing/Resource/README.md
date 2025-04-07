### Where:  

`/?page=upload`

### How:  

1. Upload a `.php` file containing any code
2. Intercept the form submission request with [BurpSuite](https://portswigger.net/burp)
3. Change `Content-Type` to `image/jpeg`
4. Found!

### Fixable by:  

1. Adding proper validation to file extensions and mime types
