#Zeller Method project
# We'll be using Zeller's congruence, which is an algorithm devised by Christian Zeller to 
# calculate the day of the week for any Julian or Gregorian calendar date:
#h = ( ( q +( (m+1) * 26 // 10)+ Y +( Y // 4)+ 6 * (Y // 100)+ (Y // 400)) % 7 )
#... all of which translates to this:
#dayOfWeek = (dayOfMonth + ((month + 1) * 26 // 10) + year + (year // 4) +
#   6 * (year/ / 100) + (year // 400)) % 7)
# Note that in this algorithm, January and February are counted as
# months #13 & #14 of the previous year, which will need to factor into your method.

def zeller(q, m, Y):
    # Where: q = day of month; m = month of the year (string); Y = year
    # This method should return the day of the week as a string
    q = int(q)
    Y = int(Y)
    months_list = ['January','February','March','April','May','June','July','August','September','October','November','December','January','February']
    months_dict = {}
    for i in range (0, 14):
        months_dict[months_list[i]] = i + 1
    m = months_dict[m]

    if m > 12:
        Y -= 1

    print(q)
    print(m)
    print(Y)
    h = ( ( q +( (m+1) * 26 // 10)+ Y +( Y // 4)+ 6 * (Y // 100)+ (Y // 400)) % 7 )
    print(h)
    answers = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']

    return answers[h]
