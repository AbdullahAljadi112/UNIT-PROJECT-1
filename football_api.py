import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("FOOTBALL_API_KEY")

url = "https://api.football-data.org/v4/teams/86"

headers = {
    "X-Auth-Token": api_key
}

try:
    response = requests.get(url, headers=headers, timeout=10)

    response.raise_for_status()

    data = response.json()

    print("API connected successfully!")
    print(f"Club: {data['name']}")
    print(f"Founded: {data['founded']}")
    print(f"Stadium: {data['venue']}")

except requests.exceptions.RequestException as error:
    print("API connection failed!")
    print(f"Status Code: {response.status_code}" if "response" in locals() else "")
    print(f"Error: {error}")