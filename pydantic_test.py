from typing import List
from pydantic import BaseModel, Field, ValidationError
import pandas as pd


df = pd.read_excel("sales_records.xlsx", engine="openpyxl")
#df_dict = df.to_dict(orient="records")


class IMSRMValidator(BaseModel):
    id_client: str
    item: str
    value: float
    discount_pct: float
    dicount_value: float
    store_id: str


class PdVal(BaseModel):
    df_dict: List[IMSRMValidator]


PdVal(df_dict=df.to_dict(orient="records"))
