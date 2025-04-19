### Where  

`/?page=upload`

### How  

1. Upload any file that is not a `.jpeg`  
2. Intercept the form submission request with [BurpSuite](https://portswigger.net/burp)
3. Change the uploaded file's `Content-Type` to `image/jpeg`
4. Found!

### Fixable by  

1. Properly validating file extensions and MIME types
