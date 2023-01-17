def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j+1):
        reversedDay = int(str(day)[::-1]) # reverse the string
        if abs(day - reversedDay) % k == 0:
            count += 1
    return count
