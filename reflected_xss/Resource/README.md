### Where:  

`/?page=media`

### How:  

1. Randomly click on NSA 3rd image on the home page
2. Found `media` page
2. Tried to change `src` parameter
3. Noticed that the page displays the "Wrong Answer" GIF
4. Open page source
5. Noticed `<object>` tag
6. Noticed that changing `src` parameter changes `<object>`'s `data` attribute
7. Try to load HTML thru `src`
8. Send `<script>alert(1)</script>` payload base64 encoded `data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`
9. Found!

### Fixable by:  

1. Not having the `src` be the `<object>`'s `data` attribute OR have a whitelist of values and validate
2. Use the [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) header
