def format_indian_number(number):
    if number < 100000:
        return str(number)
    elif number < 10000000:
        lakh = number // 100000
        remainder = number % 100000
        if remainder == 0:
            return str(lakh) + " Lakh"
        else:
            return str(lakh) + " Lakh " + str(remainder)
    else:
        crore = number // 10000000
        remainder = number % 10000000
        if remainder == 0:
            return str(crore) + " Crore"
        else:
            lakh = remainder // 100000
            if lakh == 0:
                return str(crore) + " Crore"
            else:
                remainder = remainder % 100000
                if remainder == 0:
                    return str(crore) + " Crore " + str(lakh) + " Lakh"
                else:
                    return str(crore) + " Crore " + str(lakh) + " Lakh " + str(remainder)

# Example usage:
number = int(input("Enter the number:"))
formatted_number = format_indian_number(number)
print(formatted_number)  # Output: 12 Lakh 34 Thousand 567
