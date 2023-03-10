import requests
from time import sleep
from threading import Thread
import json

header = {"User-Agent":"NotABot/69.420"}

def get_data(url):
    data = requests.get(url, headers=header).json()
    return data

def timer():
    while True:
        market_data = get_data("https://api.coingecko.com/api/v3/coins/helium")
        block_data = get_data("https://explorer-api.helium.com/api/metrics/blocks")
        validator_data = get_data("https://explorer-api.helium.com/api/metrics/validators")
        hotspot_data = get_data("https://explorer-api.helium.com/api/metrics/hotspots")
        dc_burn_data = get_data("https://ugxlyxnlrg9udfdyzwnrvghlu2vydmvycg.blockjoy.com/v1/dc_burns/stats")
        mobile_data = get_data("https://explorer-api.helium.com/api/metrics/cells")

        print("here")

        with open("market_data.json", "w+") as file:
            json.dump(market_data, file, indent=4)
        with open("block_data.json", "w+") as file:
            json.dump(block_data, file, indent=4)
        with open("validator_data.json", "w+") as file:
            json.dump(validator_data, file, indent=4)
        with open("hotspot_data.json", "w+") as file:
            json.dump(hotspot_data, file, indent=4)
        with open("dc_burn_data.json", "w+") as file:
            json.dump(dc_burn_data, file, indent=4)
        with open("mobile_data.json", "w+") as file:
            json.dump(mobile_data, file, indent=4)

        sleep(300)

timer()
