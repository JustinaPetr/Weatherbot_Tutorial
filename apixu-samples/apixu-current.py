import os

from apixu.client import ApixuClient

api_key = os.environ['APIXU_KEY']
#api_key = 'xxxx' #your apixu key
client = ApixuClient(api_key)

current = client.current(q='London')

print(current['location']['name'])
print(current['location']['region'])

print(current['current']['last_updated_epoch'])

