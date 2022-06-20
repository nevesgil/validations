from voluptuous import Schema, Required, MultipleInvalid, All, ALLOW_EXTRA
import json
import pandas as pd

with open("valid_schema_voluptuous.json", "r") as json_file:
    schema_imp = json.load(json_file)

df = pd.read_excel("sales_records.xlsx", engine="openpyxl")
df_dict = df.to_dict(orient="records")


def ids_test(value):
    val = value
    if val < 9999:
        return val


schema = Schema(
    {
        Required("id_client"): All(int, ids_test),
        Required("item"): str,
        Required("value"): float,
        Required("discount_pct"): float,
        Required("discount_value"): float,
        Required("store_id"): int,
    },
)


# result = schema({"id_client": "123"})

for idx, record in enumerate(df_dict):
    try:
        schema(record)
    except MultipleInvalid as e:
        print(f"item {idx}, errors: {e}")
