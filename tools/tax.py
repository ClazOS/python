'''Incomes uptill 10,000 are not taxed at all.  Income in between 10,000 to 20,000 are taxed at 10% Income in between 20,000 to 40,000 are taxed at 20% Income above 40,000 are taxed at 30%.'''

# This def calculates the tax according to the given tax-structure and returns the tax
def calculate_tax(inc):
    "REPLACE THIS CODE WITH YOUR calculateTax() METHOD"
    lmax = inc - 40000
    if lmax < 0:
        lmax = 0
    l20 = inc - 20000
    if l20 < 0:
        l20 = 0
    if l20 > 20000:
        l20 = 20000
    l10 = inc - 10000
    if l10 < 0:
        l10 = 0
    if l10 > 10000:
        l10 = 10000
    return lmax * 0.3 + l20 * 0.2 + l10 * 0.1

# This def reads a series of incomes from comma separated values in the string text and then formats the income and tax in a table and returns the string

def income_list(text):
    "REPLACE THIS CODE WITH YOUR incomeList() METHOD"
    incomes = text.split(",")
    result = []
    for income in incomes:
        result.append(income + "-" + str(calculate_tax(int(income))))
    return result

