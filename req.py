
import requests
import json
#
# # GET
status = "avaliable"
#
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# POST

url = 'https://petstore.swagger.io/v2/pet'


headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}


data = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}


response = requests.post(url, headers=headers, json=data)


print(response.status_code)
print(response.json())

# PUT

url = 'https://petstore.swagger.io/v2/pet'


headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}


data = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}


response1 = requests.put(url, headers=headers, json=data)


print(response1.status_code)
print(response1.json())


# DELETE

petID = 9223372036854775807
url = f'https://petstore.swagger.io/v2/pet/{petID}'


headers = {
    'accept': 'application/json'
}


response = requests.delete(url, headers=headers)


print(response.status_code)
print(response.json())