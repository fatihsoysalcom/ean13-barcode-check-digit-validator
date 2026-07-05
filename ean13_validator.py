import sys

def validate_ean13_checksum(ean13_barcode_str):
    """
    Validates the EAN-13 barcode using the GS1 Mod-10 algorithm.

    Args:
        ean13_barcode_str (str): A 13-digit string representing the EAN-13 barcode.

    Returns:
        bool: True if the barcode is valid, False otherwise.
        str: A message indicating the validation result.
    """
    if not isinstance(ean13_barcode_str, str) or not ean13_barcode_str.isdigit() or len(ean13_barcode_str) != 13:
        return False, f"Error: Barcode '{ean13_barcode_str}' must be a 13-digit string."

    # Extract the 12 data digits and the provided check digit
    data_digits_str = ean13_barcode_str[:12]
    provided_check_digit = int(ean13_barcode_str[12])

    sum_odd_positions = 0
    sum_even_positions = 0

    # GS1 Mod-10 Algorithm for EAN-13:
    # Digits are numbered from left to right, starting at 1.
    # Step 1: Sum digits at odd positions (1st, 3rd, 5th, etc.) and multiply by 1.
    # Step 2: Sum digits at even positions (2nd, 4th, 6th, etc.) and multiply by 3.
    for i, digit_char in enumerate(data_digits_str):
        digit = int(digit_char)
        # Position 'i+1' because enumerate is 0-indexed
        if (i + 1) % 2 == 1:  # Odd position (1st, 3rd, 5th, 7th, 9th, 11th)
            sum_odd_positions += digit # Multiplied by 1 implicitly
        else:  # Even position (2nd, 4th, 6th, 8th, 10th, 12th)
            sum_even_positions += digit # Will be multiplied by 3 later

    # Apply weighting for even positions
    sum_even_positions_weighted = sum_even_positions * 3

    # Step 3: Add the results from Step 1 and Step 2
    total_sum = sum_odd_positions + sum_even_positions_weighted

    # Step 4: Calculate the remainder when the total sum is divided by 10
    remainder = total_sum % 10

    # Step 5: Calculate the check digit
    # If the remainder is 0, the check digit is 0.
    # Otherwise, subtract the remainder from 10.
    calculated_check_digit = 0 if remainder == 0 else (10 - remainder)

    if calculated_check_digit == provided_check_digit:
        return True, f"Barcode '{ean13_barcode_str}' is VALID. Calculated check digit: {calculated_check_digit}."
    else:
        return False, f"Barcode '{ean13_barcode_str}' is INVALID. Calculated check digit: {calculated_check_digit}, Provided check digit: {provided_check_digit}."

if __name__ == "__main__":
    # Example barcodes for demonstration
    test_barcodes = [
        "4006381333931",  # Valid example from article context / common EAN
        "9780321765723",  # Valid ISBN-13 (which uses EAN-13 structure)
        "1234567890128",  # Valid example
        "1234567890123",  # Invalid example (check digit should be 8)
        "123456789012X",  # Invalid format
        "123456789012",   # Too short
        "12345678901234"  # Too long
    ]

    print("--- EAN-13 Barcode Validation using GS1 Mod-10 Algorithm ---")
    print("-----------------------------------------------------------\n")

    for barcode in test_barcodes:
        is_valid, message = validate_ean13_checksum(barcode)
        print(message)
        print("-" * 50)

    print("\n--- Try validating a custom barcode (enter 'q' to quit) ---")
    while True:
        user_input = input("Enter a 13-digit EAN-13 barcode: ")
        if user_input.lower() == 'q':
            break
        
        is_valid, message = validate_ean13_checksum(user_input)
        print(message)
        print("-" * 50)
