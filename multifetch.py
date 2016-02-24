import sys, urllib, re

title_re = re.compile("<title>(.*?)</title>",
                      re.MULTILINE | re.DOTALL | re.IGNORECASE)
                      
for url in sys.argv[1:]:
    match = title_re.search(urllib.urlopen(url).read())
    if match: 
        print url,  "\t", match.group(1).strip()
        
## test 
## chmod u+x multifetch.py

## execute 
## ./fetch.py http://www.google.com http://www.brandeis.edu

