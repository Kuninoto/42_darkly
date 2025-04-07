### Where:  

`/?page=searchimg`

### How:  

1. Found `searchimg` page by clicking on "Search Image" button on the home page
2. Tried to inject SQL in different manners until we've tried a `UNION` attack

    ```SQL
    1 UNION SELECT table_name, column_name FROM information_schema.columns
    ```

    ```SQL
    1 OR 1=1 UNION SELECT id, comment FROM list_images
    ```

3. By running the above query, we were able to dump the `id` and `comment` columns of every image. The image with id `5` has an intersting comment: "If you read this just use this md5 decode lowercase then sha256 to win this flag ! `<hash>`"
4. We picked up the `<hash>`, and did has the comment said
5. Found!

### Fixable by:  

1. Properly sanitizing user input
