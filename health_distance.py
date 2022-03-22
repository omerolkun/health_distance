import math

def distance (antenna, power, frequency,freq_unit):
    if antenna == "":
        antenna = 0
    if power == "":
        power = 0
    if frequency == "":
        frequency = 0
    if freq_unit == 'kHz':
        frequency = frequency * 1000
    elif freq_unit == 'MHz':
        frequency = frequency * 1000000
    elif freq_unit == 'GHz':
        frequency =  frequency * 1000000000
    
    frequency = frequency / 1000000
    try:
        lmbda = 299.8 / frequency
    except:
        return "error"
    fraun = antenna * antenna * 2 / lmbda
    g_distance = fraun
    if frequency < 0.01 or frequency>=300000:
        print("range of frequency is not desirable")
        return "error"
    if frequency >= 0.01 and frequency < 1:
        R = math.sqrt(30 * power) / ( 5 * math.sqrt(6 * math.pi))
    
    if frequency >= 1 and frequency < 10:
        R = math.sqrt(30 * power) / (5 * math.sqrt(6*math.pi))
    if frequency >= 10 and frequency < 400:
        R = math.sqrt(30* power) / (math.sqrt(15* math.pi))
    if frequency >= 400 and frequency < 2000:
        R = math.sqrt(30*power)/(0.25*math.sqrt(0.6*math.pi*frequency))
    if frequency >= 200 and frequency < 150000:
        R = math.sqrt(30*power) / (5*math.sqrt(3*math.pi))
    if frequency >=15000 and frequency < 300000:
        R = 100 * math.sqrt(30*power) / (math.sqrt(5*math.pi*frequency))
    

    result = str(round(g_distance,2))
    print("The health distance is ",round(g_distance,2), "m")
    return result


if __name__ == "__main__":
    distance(10,15.3,20,'MHz')    


