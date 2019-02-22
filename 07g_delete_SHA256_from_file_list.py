import requests

amp_client_id = 'a1b2c3d4e5f6g7h8i9j0'

amp_api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# EXAMPLES:
# file_lists_guid = 'e773a9eb-296c-40df-98d8-bed46322589d'
# sha256 = '4ce4e7ab22a8900bf438ff84baebe74d3ef3828a716b933b6e2a85b991b36f31'
file_lists_guid = '<FILE_LIST_GUID>'

sha256 = '<SHA256>'

url = 'https://api.amp.cisco.com/v1/file_lists/{}/files/{}'.format(file_lists_guid, sha256)

request = requests.delete(url, auth=(amp_client_id, amp_api_key))

print(request.json())
