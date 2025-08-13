from pydantic import BaseModel

class DestinyMatrixRequest(BaseModel):
    birth_day: int
    birth_month: int
    birth_year: int

class DestinyMatrixResponse(BaseModel):
    life_path_number: int
    interpretation: str
    calculation_steps: str