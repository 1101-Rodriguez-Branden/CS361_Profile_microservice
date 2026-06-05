import requests

BASE_URL = "http://127.0.0.1:5006"


print("CREATE PROFILE TEST")
response = requests.post(BASE_URL + "/profile", json={
    "user_id": "123",
    "username": "Branden",
    "email": "b_rodriguez2000@yahoo.com",
    "location": "Corvallis",
    "favorite_pet_type": "cat"
})
print("Status code:", response.status_code)
print("Response:", response.json())


print("\nGET PROFILE TEST")
response = requests.get(BASE_URL + "/profile?user_id=123")
print("Status code:", response.status_code)
print("Response:", response.json())


print("\nINVALID PROFILE TEST")
response = requests.post(BASE_URL + "/profile", json={
    "username": "Branden",
    "email": "b_rodriguez2000@yahoo.com"
})
print("Status code:", response.status_code)
print("Response:", response.json())


print("\nPROFILE NOT FOUND TEST")
response = requests.get(BASE_URL + "/profile?user_id=999")
print("Status code:", response.status_code)
print("Response:", response.json())