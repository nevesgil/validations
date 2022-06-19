from voluptuous import Schema, Required, All, Length, Range
import json
import pandas as pd

with open("valid_schema_voluptuous.json", "r") as json_file:
    schema_imp = json.load(json_file)

df = pd.read_excel("sales_records.xlsx", engine="openpyxl")
df_dict = df.to_dict(orient="records")


schema = Schema(
    {
        Required("id_client"): int,  # All(str, Length(max=10)),
        Required("item"): str,
        Required("value"): float,
        Required("discount_pct"): float,
        Required("discount_value"): float,
        Required("store_id"): int,
    }
)


# result = schema({"id_client": "123"})

for idx, record in enumerate(df_dict):
    if not schema(record):
        print(f"item {idx}, errors:")
