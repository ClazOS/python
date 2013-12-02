#Base Conversion methods
import math
def get_number_by_base(base) :
    # This method accepts a base ('base') and returns the largest value for
    # a single digit of that base -- where 'base' can be up to base 16 (hexadecimal).
    # Thus if the base is 5, then the largest value would be 4. If it is base 16
    # (hexadecimal), the largest value would be F. The returned values can be
    # as follows: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    digits = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    return digits.index(base)


def base_to_base10(num, base) :
    # Given a number ('num') and its base ('base'), this method returns the
    # number in its base 10 equivalent. Thus, an input of num=3E, base=16
    # would return 62 (= 48 + 14).
    # Use the get_number_by_base() def above to help with the conversion.
    list_char = []
    digits = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    calcul = 0
    for char in num:
        list_char.append(char)
    list_char.reverse()
    for i in range (0, len(list_char)):
        calcul += digits.index(list_char[i]) * int(base) ** i

    return calcul

def base10_to_base(x, base) :
    # This method converts a base 10 number ('x') into its equivalent in
    # another base ('base') and returns that value.
