def is_modified_kaprekar_number(n):
    if n == 0:
        return False
    if n == 1:
        return True
    square = str(n * n)
    i = len(square) // 2
    left, right = int(square[:i] or 0), int(square[i:] or 0)
    if right != 0 and left + right == n:
        return True
    if int(square) == n:
        return True
    return False

def kaprekarNumbers(p, q):
    kaprekar_numbers = []
    for n in range(p, q+1):
        if is_modified_kaprekar_number(n):
            kaprekar_numbers.append(n)
    if kaprekar_numbers:
        print(*kaprekar_numbers)
    else:
        print("INVALID RANGE")

kaprekarNumbers(1,100)
