def reduce_to_single_digit(number: int) -> int:
    """Reduce a number to a single digit by summing its digits."""
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number

def calculate_life_path_number(birth_day: int, birth_month: int, birth_year: int) -> int:
    """Calculate Life Path Number from birth date."""
    day_number = reduce_to_single_digit(birth_day)
    month_number = reduce_to_single_digit(birth_month)
    year_number = reduce_to_single_digit(birth_year)
    return reduce_to_single_digit(day_number + month_number + year_number)

def get_destiny_interpretation(number: int) -> str:
    """Return a simple interpretation for a given number."""
    interpretations = {
        1: "Leader, independent, ambitious",
        2: "Diplomatic, cooperative, intuitive",
        3: "Creative, expressive, social",
        4: "Practical, disciplined, hardworking",
        5: "Adventurous, dynamic, freedom-loving",
        6: "Responsible, nurturing, harmonious",
        7: "Analytical, spiritual, introspective",
        8: "Authoritative, goal-oriented, successful",
        9: "Humanitarian, compassionate, idealistic",
    }
    return interpretations.get(number, "Unknown number")