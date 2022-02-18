import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
import twurl


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_dict_twitter(acct):
    print('')
    if len(acct) >= 1:
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': acct})
        try:
            connection = urllib.request.urlopen(url, context=ctx)
        except urllib.error.HTTPError as e:
            print(e.reason)
        data = connection.read().decode()

        js = json.loads(data)
        return js
        # print(json.dumps(js, indent=2))

        # headers = dict(connection.getheaders())
        # print('Remaining', headers['x-rate-limit-remaining'])

