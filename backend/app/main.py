from fastapi import FastAPI
from backend.core.matrix_calculator import (
    calculate_life_path_number,
    get_destiny_interpretation
)
from .schemas import DestinyMatrixRequest, DestinyMatrixResponse

app = FastAPI()

def get_calculation_steps(day: int, month: int, year: int) -> str:
    """Helper function to generate calculation explanation"""
    steps = [
        f"1. Day ({day}): {sum(int(d) for d in str(day))}",
        f"2. Month ({month}): {sum(int(d) for d in str(month))}",
        f"3. Year ({year}): {sum(int(d) for d in str(year))}",
        "4. Sum all reduced numbers",
        "5. Reduce to single digit"
    ]
    return "\n".join(steps)

@app.post("/calculate", response_model=DestinyMatrixResponse)
async def calculate_destiny(data: DestinyMatrixRequest):
    life_path = calculate_life_path_number(
        data.birth_day,
        data.birth_month,
        data.birth_year
    )
    return DestinyMatrixResponse(
        life_path_number=life_path,
        interpretation=get_destiny_interpretation(life_path),
        calculation_steps=get_calculation_steps(
            data.birth_day,
            data.birth_month,
            data.birth_year
        )
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

from database import SessionLocal, Calculation

# Add to your calculate_destiny endpoint:
db = SessionLocal()
db_calculation = Calculation(
    birth_day=data.birth_day,
    birth_month=data.birth_month,
    birth_year=data.birth_year,
    life_path_number=life_path
)
db.add(db_calculation)
db.commit()
db.refresh(db_calculation)