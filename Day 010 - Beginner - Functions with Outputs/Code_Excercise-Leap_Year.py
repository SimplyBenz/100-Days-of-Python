def is_leap_year(year):
    # A leap year must be divisible by 4
    if year % 4 == 0:
        # If it is also divisible by 100, it must be divisible by 400 to be a leap year
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400: Leap Year
            else:
                return False  # Divisible by 100 but not by 400: Not a Leap Year
        else:
            return True  # Divisible by 4 but not by 100: Leap Year
    else:
        return False  # Not divisible by 4: Not a Leap Year



print(is_leap_year(2024))