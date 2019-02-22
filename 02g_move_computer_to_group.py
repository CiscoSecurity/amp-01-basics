import requests

amp_client_id = 'a1b2c3d4e5f6g7h8i9j0'

amp_api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# EXAMPLES:
# computer_guid = 'd7fbcdb6-0a14-4e39-867e-02f5e1649497'
# group_guid = '68665863-74d5-4bc1-ac7f-5477b2b6406e'
computer_guid = '<COMPUTER_GUID>'

group_guid = '<GROUP_GUID>'

url = 'https://api.amp.cisco.com/v1/computers/{}'.format(computer_guid)

request = requests.patch(url, auth=(amp_client_id, amp_api_key), data={'group_guid':group_guid})

print(request.json())
