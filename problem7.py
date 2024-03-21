def is_all_digits_even(number):
    for digit in str(number):
        if int(digit) % 2 != 0:
            return False
    return True

even_digit_numbers = []

for num in range(1000, 3001):
    if is_all_digits_even(num):
        even_digit_numbers.append(num)

print(','.join(map(str, even_digit_numbers)))