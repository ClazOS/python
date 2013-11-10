def happynum(num):
    past = set()
    while True:
        total = sum(int(i)**2 for i in str(num))
        if total == 1:
            return 'Happy Number'
        if total in past:
            return 'Unhappy Number'
        num = total
        past.add(total)
