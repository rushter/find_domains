## find_domains Documentation

This library is for searching domain names in raw text data. First it searches domain-like strings
using simple regexp. Then it uses list of top level domain names to remove names which could be a
domain name i.e. last segment is not top level domain name. TLD list is provided by
[tldextract](https://github.com/john-kurkowski/tldextract) library, technicall that means that
when you will use `find_domains` in first time it will download top level domains list (this is
tldextract behaviour).

## Installation

`pip install -U find_domains`


## Usage

```
from find_domains import find_domains

data = """
foo bar google.com foo.bar.com domain.info
превед-медвед.рф
"""

for domain in find_domains(data):
    print(domain)
```
