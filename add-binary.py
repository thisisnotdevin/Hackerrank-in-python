    a_int = int(a, 2)
    b_int = int(b, 2)
    # Add integers and convert result to binary string
    result_int = a_int + b_int
    result_str = bin(result_int)[2:]
    return result_str
