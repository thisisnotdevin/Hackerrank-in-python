def findDigits(n):
    count = 0
    for digit in str(n):
        if digit != "0" and n % int(digit) == 0:
            count += 1
    return count
