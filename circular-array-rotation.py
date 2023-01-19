def circularArrayRotation(a, k, queries):
    if k > len(a):
        k = k % len(a)
    rotatedValues = []
    for i in queries:

        rotatedValues.append(a[(i-k) % len(a)])
    return rotatedValues
    
