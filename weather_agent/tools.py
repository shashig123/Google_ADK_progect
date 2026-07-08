# Calculator

# Weather API

# Azure CLI

# kubectl

# Terraform
import requests

def get_weather(city: str):

    url = f"https://wttr.in/{city}?format=3"

    response = requests.get(url)

    if response.status_code == 200:
        return response.text

    return "Unable to fetch weather."


