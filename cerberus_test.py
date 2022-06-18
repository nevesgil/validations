import pandas as pd
from cerberus import Validator
import json


class IMSValidator(Validator):
    def _check_with_ids_test(self, field, value):
        if value:
            self._error(field, "# IDS CHECKED #")


df = pd.read_excel("sales_records.xlsx", engine="openpyxl")
df_dict = df.to_dict(orient="records")

with open("valid_schema_cerberus.json", "r") as json_file:
    schema = json.load(json_file)

v = IMSValidator(schema)


for idx, record in enumerate(df_dict):
    if not v.validate(record):
        print(f"item {idx}, errors: {v.errors}")
