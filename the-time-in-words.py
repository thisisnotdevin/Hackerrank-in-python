def timeInWords(h, m):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    res = ""
    if m == 0:
        res += words[h-1]
        res += " o' clock"
    elif m == 30:
        res += "half past "
        res += words[h-1]
    elif m == 15:
        res += "quarter past "
        res += words[h-1]
    elif m == 45:
        res += "quarter to "
        res += words[h]
    elif m == 1:
        res += words[m-1] + " minute past "
        res += words[h-1]
    elif m < 30:
        res += words[m-1] + " minutes past "
        res += words[h-1]
    elif m > 30:
        res += words[60-m-1] + " minutes to "
        res += words[h]
    return res
        
