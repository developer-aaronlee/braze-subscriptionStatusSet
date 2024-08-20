import csv
import json
import requests

url = 'https://rest.iad-06.braze.com/subscription/status/set'
API_KEY = 'Bearer api_key'

headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

with open('sms_subscription_group_migration.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if len(row)==0:
            continue
        temp = row[0].split(",")
        if temp[0]=="external_id":
            continue

        body = json.dumps({
            "subscription_group_id": "7726f4af-54bc-49a0-9dba-4a3338788679",
            "subscription_state": "subscribed",
            "external_id": temp[0]
        })

        response = requests.post(url, data=body, headers=headers)
        print(response.json())
