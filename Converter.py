def binary_fixed_point_to_decimal(binary_string):
    if len(binary_string) != 10:
        raise ValueError("Must use 10 bit")

    #extraction
    integer_part = binary_string[:2]
    fractional_part = binary_string[2:]

    #CA2
    if integer_part[0] == '1':  #neg
        integer_value = -2 + int(integer_part[1])
    else:
        integer_value = int(integer_part[1])

    #convert dec
    fractional_value = sum(int(bit) * (2 ** -(i+1)) for i, bit in enumerate(fractional_part))

    #sum
    decimal_value = integer_value + fractional_value

    return decimal_value


binary_number = "1100111010"
decimal_result = binary_fixed_point_to_decimal(binary_number)
print(f"Il valore decimale di {binary_number} è {decimal_result}")

binary_number1 = "0011111111"
decimal_result = binary_fixed_point_to_decimal(binary_number1)
print(f"Il valore decimale di {binary_number1} è {decimal_result}")
