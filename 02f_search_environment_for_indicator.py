import requests

client_id = 'a1b2c3d4e5f6g7h8i9j0'

api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# EXAMPLES:
# query = 'sovereutilizeignty.com'
# query = '814a37d89a79aa3975308e723bc1a3a67360323b7e3584de00896fe7c59bbb8e'
# query = '75.102.25.76'
# query = 'SearchProtocolHost.exe'
query = '<INDICATOR>'

url = 'https://api.amp.cisco.com/v1/computers/activity'

response = requests.get(url, auth=(client_id, api_key), params={'q':query})

print(response.json())
