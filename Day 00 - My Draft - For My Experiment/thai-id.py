def validate_citizen_id(prefix):
    def calculate_check_digit(number_str):
        # คำนวณตามหลักเกณฑ์การตรวจสอบเลขบัตรประชาชน
        weights = list(range(13, 1, -1))
        total = sum(int(digit) * weight for digit, weight in zip(number_str, weights))
        remainder = total % 11
        check_digit = 11 - remainder if remainder != 0 else 0
        return check_digit if check_digit < 10 else 0

    # ลองทุกเลข 3 หลักสุดท้าย
    valid_combinations = []
    for last_3_digits in range(1000):
        full_number = f"{prefix}{last_3_digits:03d}"
        if calculate_check_digit(full_number[:-1]) == int(full_number[-1]):
            valid_combinations.append(last_3_digits)
    
    return valid_combinations

# ใช้งาน
prefix = "3200600245"
results = validate_citizen_id(prefix)
print(f"เลข 3 หลักที่ถูกต้อง: {results}")