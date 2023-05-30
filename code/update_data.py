import requests
import pandas as pd


speadsheet_urls = {
    "targets": (
        "https://docs.google.com/spreadsheets/d/e/"
        "2PACX-1vRe7-Yk7TxigT4MK3qz-RbuVt7lZu0u4vQjiqotiXCT1Ynb9sUrO7tA1RdPemXKaE2dD8IYYO5K0E1C"
        "/pub?gid=1971059158&single=true&output=csv"
    ),
    "sensors": (
        "https://docs.google.com/spreadsheets/d/e/"
        "2PACX-1vRe7-Yk7TxigT4MK3qz-RbuVt7lZu0u4vQjiqotiXCT1Ynb9sUrO7tA1RdPemXKaE2dD8IYYO5K0E1C"
        "/pub?gid=1162044269&single=true&output=csv"
    ),
}

df_targets = pd.read_csv(speadsheet_urls["targets"]).dropna(how="all", axis=0)
df_sensors = pd.read_csv(speadsheet_urls["sensors"]).dropna(how="all", axis=0)

df_sensors.to_csv("dataset/sensor_data.csv", index=False)
df_targets.to_csv("dataset/target_data.csv", index=False)
