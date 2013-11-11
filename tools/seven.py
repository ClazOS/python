def  illuminate(num):
    "REPLACE THIS CODE WITH YOUR illuminate() METHOD"
    pattern = []
    for i in range (0,10):
        pattern.append('')
    pattern[0] = "yyyyyyn"
    pattern[1] = "nyynnnn"
    pattern[2] = "yynyyny"
    pattern[3] = "yyyynny"
    pattern[4] = "nyynnyy"
    pattern[5] = "ynyynyy"
    pattern[6] = "ynyyyyy"
    pattern[7] = "yyynnnn"
    pattern[8] = "yyyyyyy"
    pattern[9] = "yyyynyy"
    return pattern[int(num)]

def  get_digits(text):
    "REPLACE THIS CODE WITH YOUR getDigits() METHOD"
    res = []
    for letter in text:
        if letter.isdigit():
            res.append(illuminate(letter))
    return res
