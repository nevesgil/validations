import pandas as pd
from cerberus import Validator
import json


class IMSValidator(Validator):
    def _check_with_ids_test(self, field, value):
        if value < 9999:
            self._error(field, "# value < 9999 #")

    def _check_with_55_code(self, field, value):
        if "55" not in value:
            self._error(field, "# no 55 code in item #")

    def _check_with_blabla_test(self, field, value):
        if isinstance(value, int):
            self._error(field, " #blabla failed #")


df = pd.read_excel("sales_records.xlsx", engine="openpyxl")
df_dict = df.to_dict(orient="records")

with open("valid_schema_cerberus.json", "r") as json_file:
    schema = json.load(json_file)

v = IMSValidator(schema)


for idx, record in enumerate(df_dict):
    if not v.validate(record):
        print(f"item {idx}, errors: {v.errors}")
