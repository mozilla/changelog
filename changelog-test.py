import json
import requests
import time

payload = {"criticality": 1, "unix_timestamp": int(time.time()), "category": "misc", "description": "python test"}
url = 'https://changelog.paas.allizom.org/api/events'
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
print r.text
print r.status_code
