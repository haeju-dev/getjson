import json
import requests
import time

def getjson(requesttype, url, params=None, timeout=10.0, maxtry=5, sleeptime=0.15, headers=None, cookies=None):
    '''
    :return: python dictionary
    :param requesttype: 'get' or 'post', Uppercase Support
    :param url: a url
    :param params: a python dictionary
    :param timeout: timeout of each requests
    :param maxtry:
    :param sleeptime:
    :param headers:
    :param cookies:

    usage:
    url = 'https://api.bithumb.com/public/ticker/'
    param = {'currency' : 'BTC'}
    print(getjson(requesttype = 'get', url = url, params = param))

    print(type(result.status_code)) --> int
    result = json.loads(str(result.text.strip())) --> OLD
    '''

    if type(requesttype) != type(''):
        raise Exception('No Request Types')
    requesttype = requesttype.upper()
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    i = 0
    result = 0
    excepts = list()
    while i < maxtry:
        try:
            if requesttype == 'GET':
                if params is None:
                    if cookies is None:
                        result = requests.get(url=url, timeout=timeout, headers=headers)
                    else:
                        result = requests.get(url=url, timeout=timeout, headers=headers, cookies=cookies)
                    result.raise_for_status()
                    if result.status_code == 200:
                        result = result.json()
                else:
                    if cookies is None:
                        result = requests.get(url=url, timeout=timeout, params=params, headers=headers)
                    else:
                        result = requests.get(url=url, timeout=timeout, params=params, headers=headers, cookies=cookies)
                    result.raise_for_status()
                    if result.status_code == 200:
                        result = result.json()
                break

            if requesttype == 'POST':
                if params is None:
                    raise Exception('No Params On Post Request')
                else:
                    if cookies is None:
                        result = requests.post(url=url, timeout=timeout, data=json.dumps(params), headers=headers)
                    else:
                        result = requests.post(url=url, timeout=timeout, data=json.dumps(params), headers=headers,
                                               cookies=cookies)
                    result.raise_for_status()
                    if result.status_code == 200:
                        result = result.json()
                break

        except Exception as inst:
            excepts.append(inst)
            time.sleep(sleeptime)
        i += 1
    if i == maxtry:
        raise Exception('Count over Maxtry Error', excepts)
    if result == 0:
        raise Exception('Something was wrong in responce', excepts)
    return result
