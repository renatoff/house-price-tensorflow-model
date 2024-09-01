# %%
import pandas as pd
import requests

house_df = pd.read_csv("house_df.csv", index_col=0)
house_df

# %%
response = requests.post(
    "http://127.0.0.1:5000/predict",
    json=house_df.to_json(orient="records"),
)

response.json()
