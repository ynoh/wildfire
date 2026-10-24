#! .venv/bin/python

import json
import pandas as pd
import requests

url = "https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/WFIGS_Interagency_Perimeters/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"


def data_in_time_range(text: str) -> int:

    try:
        # df = pd.DataFrame(json.loads(text))
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return -1


    with open("wildfire_data.json", "w") as f:
        json.dump(data, f, indent=4)


    return 0


def main():
    response = requests.get(url)

    if response.status_code != 200:
        print(f"response failed: {response.status_code}")
        return -1

    return data_in_time_range(response.text)


if __name__ == "__main__":
    main()
