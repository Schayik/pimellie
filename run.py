import requests

token = "EABWxZBcoSl4sBOz88sRvkheNguf8gmkJyDZCBjXgeo2SprbRcNezZCPePdWxECbPkS4r4ZBrj7MSTKvgpEkRGCwKBkAh6qBumBWyiu5HgWZC6O6iDWqMO2YmYRpjVJjQanhpBVvST3QFLD7wWtywkKbYyvAbttZCuZAw5CREFZAbEvcIucoQtvHxT3kbZBMBIyoAjDcSNyGZCqyDxrq2eU"

phone_id = "114565751731975"

url = "https://graph.facebook.com/v17.0/" + phone_id + "/messages"

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
}

data = {
    "messaging_product": "whatsapp",
    "to": "31683488976",
    "type": "template",
    "template": {"name": "save_the_date", "language": {"code": "nl"}},
    "type": "image",
    "image": {"link": "https://ibb.co/6yDKzZD"},
    "components": [
        {
            "type": "body",
            "parameters": [{"type": "text", "text": "Jip & Eveline"}],
        }
    ],
}

r = requests.post(url, headers=headers, json=data)

print(r)
print(r.json())

# recipients = [
#     { "1": "Jip & Eveline", "phone": "31984754987"},
#     { "1": "Dave & Ash", "phone": "31984754987"},
# ]
