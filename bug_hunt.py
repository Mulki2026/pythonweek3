count = 1
total = 0

# BUG: Missing colon at the end of the while loop statement. Added ':' to fix SyntaxError.
while count <= 5:  # BUG: 'count < 5' excluded 5 from the sum (giving 10). Changed to '<=' to sum 1 to 5 correctly.
    total = total + count
    count = count + 1

# BUG: Can't concatenate string and int directly. Converted 'total' to str(total) using type conversion or f-string.
print("Sum of 1 to 5 is: " + str(total))