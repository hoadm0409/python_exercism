def is_armstrong(number):
    k = len(str(number))
    return number == sum([(int(n) ** k) for n in str(number)])
