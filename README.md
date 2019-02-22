[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/AMP-for-Endpoints "Gitter chat")

### AMP for Endpoint API Basics:
This collection of scripts cover the basics of interacting with the AMP for Endpoints API. Each script covers one API endpoint. These are intented to show the bare minimum required to interact with the API endpoint.

### Before using you must update the following:
- client_id
- api_key

Additional variables where present:
- computer_guid
- user
- query
- computer_guid
- group_guid
- parent_group_guid
- policy_guid
- file_lists_guid
- sha256
- stream_id

When an additional variable is present in a script an example with the appropriate format is provided as a comment. These variables are noted with a < (less-than-sign) and > (greater-than-sign).
```
# EXAMPLE:
# computer_guid = 'd7fbcdb6-0a14-4e39-867e-02f5e1649497'
computer_guid = '<COMPUTER_GUID>'
```

### Usage:
```
python 01_authentication.py
```

### Example script output:
```
{'version': 'v1.2.0', 'metadata': {'links': {'self': 'https://api.amp.cisco.com/v1/version'}}, 'data': {}}
```
