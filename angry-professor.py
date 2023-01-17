def angryProfessor(k, a):
    for time in a:
        if time <= 0:
            k -= 1
    return "YES" if k > 0 else "NO"
