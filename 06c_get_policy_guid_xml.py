import requests

amp_client_id = 'a1b2c3d4e5f6g7h8i9j0'

amp_api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# EXAMPLE:
# group_guid = '89912c9e-8dbd-4c2b-a1d8-dee8a0c2bb29'
policy_guid = '<POLICY_GUID>'

url = 'https://api.amp.cisco.com/v1/policies/{}.xml'.format(policy_guid)

request = requests.get(url, auth=(amp_client_id, amp_api_key))

print(request.text)
