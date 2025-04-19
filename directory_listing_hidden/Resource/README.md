### Where  

`/robots.txt` and `/.hidden`

### How  

1. Randomly decided to check if there was a `robots.txt` file, possibly trying to avoid crawlers to crawl sensitive pages
2. Found there was one, and that it shows two routes
3. Visit `/.hidden`
4. Found that it's a directory that has listing and holds a huge amount of folders with READMEs with repetitive phrases
5. Decided to develop a [script](https://github.com/Kuninoto/42_darkly/blob/master/directory_listing_hidden/Resource/explore.py) to recursively walk the directories and read every README file encountered along the way, searching for one with a content different from the repetitive ones
6. Found!

### Fixable by  

1. Disabling directory listing
2. Securing files that contain sensitive information
