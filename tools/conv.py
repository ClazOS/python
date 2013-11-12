#Basic units conversion tool
def temperature(n, frm):
    "REPLACE THIS CODE WITH YOUR TEMPERATURE CONVERSION METHOD"
    formats = ['celsius','fahrenheit','kelvin']
    if frm not in formats:
        return 'Format error'
    if frm == formats[0]:
        return [(9/5) * n + 32 , n + 273.15]
    if frm == formats[1]:
        return [(n - 32) / 1.8 , ((n-32)/ 1.8)+273.15]
    if frm == formats[2]:
        return [(n - 273.15)*9/5 + 32 , n - 273.15]

def length(n, frm):
   
    
    if frm == 'miles':
        km = n * 1.609
        ft = n * 5280
        m = n * 1609
        return [km,ft,m]
    if frm == 'feet':
        mi = n / 5280
        km = n * 0.0003047
        m = n * 0.3047
        return [km,m,mi]
        
    if frm == 'kilometers':
        mi = n / 1.609
        m = n * 1000
        ft = n * 3280.85
        return [mi,m,ft]
        
    if frm == 'meters':
        mi = n /1609
        km = n / 1000
        ft = n * 3.28085
        return [mi,km,ft]
        


def volume(n, frm):
    "REPLACE THIS CODE WITH YOUR VOLUME CONVERSION METHOD"
    if frm == 'cubic_meters':
        ml
        cubic_in
        gal
        return[ml,cubic_in,gal]

    if frm == 'milliliters':
        cubic_m
        cubic_in
        gal
        return[cubic_m,cubic_in,gal]

    if frm == 'cubic_inches':
        cubic_m
        ml
        gal
        return[cubic_m,ml,gal]

    if frm == 'gallons':
        cubic_m
        ml
        cubic_in
        return[cubic_m,ml,cubic_in]

def weight(n, frm):
    "REPLACE THIS CODE WITH YOUR OWN WEIGHT CONVERSION METHOD"

