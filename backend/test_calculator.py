from core.matrix_calculator import (
    calculate_life_path_number,
    get_destiny_interpretation
)

# Test Life Path Number
birth_day = 15
birth_month = 3
birth_year = 1992
life_path = calculate_life_path_number(birth_day, birth_month, birth_year)
interpretation = get_destiny_interpretation(life_path)

print(f"Life Path Number: {life_path}")  # Should output 3
print(f"Interpretation: {interpretation}")  # Should match 3's description