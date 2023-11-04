import requests

token = "<token>"

phone_id = "<phone_id>"

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
