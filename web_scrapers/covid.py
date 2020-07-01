import requests


def covid_data():
    url = "https://api.covid19india.org/v3/data.json"
    r = requests.get(url)
    data = r.json()
    data = data["TT"]
    added = data["delta"]
    total = data["total"]
    return added, total


covid_data()
