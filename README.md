# # getjson

Send a Get/Post request and return as dictionary


## Usage

### Example
'''python
from getjson import getjson
url = 'https://api.bithumb.com/public/ticker/'
param = {'currency' : 'BTC'}
print(getjson(requesttype = 'get', url = url, params = param))
'''

### param

```python
getjson(requesttype = 'get', url = 'http://127.0.0.1/')

:param requesttype: 'get' or 'post', Uppercase Support
:param url: a url
:param params: a python dictionary
:param timeout: timeout of each requests, sec
:param maxtry: 
:param sleeptime: sleep time for each requests, sec
:param headers: 
:param cookies: 
```
