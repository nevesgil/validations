from typing import Any, List, Type
import pandas as pd
from pydantic import BaseModel


df = pd.read_excel("sales_records.xlsx", engine="openpyxl")
df_dict = df.to_dict(orient="records")


class IMSRMValidator(BaseModel):
    id_client: str
    item: str
    value: float
    discount_pct: float
    discount_value: float
    store_id: str


class IMSRMValidatorDF(BaseModel):
    rows: List[IMSRMValidator]


"""
data = {
    "id_client": "123",
    "item": "abc",
    "value": "1.0",
    "discount_pct": "0.1",
    "dicount_value": "0.1",
    "store_id": "e23",
}


row = IMSRMValidator(**data)

print(row)
print()
print(row.dict())
print()
# Serialize to JSON
print(row.json(indent=4))
"""

collectionval = IMSRMValidatorDF(rows=df_dict)


######  VALIDATING A DATAFRAME


class ValidDataframe(pd.DataFrame):
    """subclass that validates on instatiation"""

    @property
    def _constructor(self) -> Type["ValidDataframe"]:
        """Use the constructor for this type when returning a new dataframe"""
        return ValidDataframe

    def __init__(self, *args: Any, verbose: bool = True, **kwargs: Any) -> None:
        """instantiate as normal, then validate using pydantic"""
        super().__init__(*args, **kwargs)

        ## Print out validating message
        if verbose:
            print("Validating The DATA!")

        IMSRMValidatorDF(rows=self.to_dict(orient="records"))

        if verbose:
            print("Looks good!")


validdf = ValidDataframe(df, verbose=True)
