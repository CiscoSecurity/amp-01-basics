[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/AMP-for-Endpoints "Gitter chat")

### AMP for Endpoint API Basics

This collection of scripts cover the basics of interacting with the AMP for Endpoints API. Each script covers one API endpoint. These are intented to show the bare minimum required to interact with the API endpoint.

### Before using you must update the following:
- client_id
- api_key

Some scripts require additional variables to be set, for example a computer GUID or a SHA256. An example with the appropriate format is provided as a comment. These variables are noted with a < (less-than-sign) and > (greater-than-sign).

```
# EXAMPLE:
# computer_guid = 'd7fbcdb6-0a14-4e39-867e-02f5e1649497'
computer_guid = '<COMPUTER_GUID>'
```

### Usage

```
python 01_authentication.py
```
