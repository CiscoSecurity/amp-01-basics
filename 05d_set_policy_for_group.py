import requests

amp_client_id = 'a1b2c3d4e5f6g7h8i9j0'

amp_api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# EXAMPLES:
# group_guid = '68665863-74d5-4bc1-ac7f-5477b2b6406e'
# windows_policy_guid = '89912c9e-8dbd-4c2b-a1d8-dee8a0c2bb29'
group_guid = '<GROUP_GUID>'

windows_policy_guid = '<WINDOWS_POLICY_GUID>'

url = 'https://api.amp.cisco.com/v1/groups/{}'.format(group_guid)

data = {'windows_policy_guid':windows_policy_guid}

request = requests.patch(url, auth=(amp_client_id, amp_api_key), data=data)

print(request.json())
