### Where:

`/` and `/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`

### How:

1. Inspect page source in main page's footer
2. See weird copyright link
3. Visit it
4. Inspect page source
5. View source code comment
6. Make request with `Referer: https://www.nsa.gov/` and `User-Agent: ft_bornToSec` headers
7. Found!

### Fixable by:

1. Removing comments in HTML that contains private information
2. Adding proper authorization to requests
