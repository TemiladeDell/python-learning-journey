import requests


url = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "format": "json",
    "prop": "extracts",
    "explaintext": 1,
    "titles": ""
}

user_agent = "mybot/1.0"
user_search = input("Enter search: ").strip(" ")
params["titles"] = user_search

try:
    response = requests.get(url, params=params, headers={"User-Agent": user_agent}, timeout=5.0)
    response.raise_for_status()
    data = response.json()
    print(response.status_code)
    print(data["query"]["pages"][list(data["query"]["pages"].keys())[0]]["extract"])

except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except KeyError:
    print("Key not found in response.")



