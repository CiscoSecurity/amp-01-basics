import requests

amp_client_id = 'a1b2c3d4e5f6g7h8i9j0'

amp_api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# EXAMPLE:
# computer_guid = 'd7fbcdb6-0a14-4e39-867e-02f5e1649497'
computer_guid = '<COMPUTER_GUID>'

url = 'https://api.amp.cisco.com/v1/computers/{}/trajectory'.format(computer_guid)

request = requests.get(url, auth=(amp_client_id, amp_api_key))

print(request.json())
