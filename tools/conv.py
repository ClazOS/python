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
    res = [] 
    if frm == 'cubic_meter': 
        milliliters = n * 1000000 
        cubic_inches = n * 61023.74 
        gallons = n * 264.17 
        res.append(milliliters)
        res.append(cubic_inches)
        res.append(gallons)
        return res 
     
    if frm == 'milliliters': 
        cubic_meters = n * 0.000001 
        cubic_inches = n * 0.061 
        gallons = n * 0.00026 
        res.append(cubic_meters)
        res.append(cubic_inches)
        res.append(gallons)
        return res 
     
    if frm == 'cubic_inches': 
        cubic_meters = n * 0.000016 
        milliliters = n * 16.38 
        gallons = n * 0.0043 
        res.append(cubic_meters)
        res.append(milliliters)
        res.append(gallons)
        return res 
     
    if frm == 'gallons': 
        cubic_meters = n * 0.0037 
        milliliters = n * 3785.4 
        cubic_inches = n * 231 
        res.append(cubic_meters)
        res.append(milliliters)
        res.append(cubic_inches)
        return res 
def weight(n, frm):
    "REPLACE THIS CODE WITH YOUR OWN WEIGHT CONVERSION METHOD"
    if frm == 'pounds':
        return [0.45 * n , 16 * n]
    if frm == 'kilograms':
        return [n * 2.2 , n * 35.27]
    if frm == 'ounces':
        return [n * 0.0625 , n * 0.028]
