# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition

temp = 28
is_raining = False
if temp > 35 or temp < 15 or is_raining: #if one condition is True then the event is cancelled
    print("The outdoor event is cancelled")
else: 
    print("The outdoor event is still scheduled")

is_sunny = False
if temp >= 28 and is_sunny:
    print("It is HOT and SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD and SUNNY")
elif 0 < temp > 28 and is_sunny: 
    print("It is WARM and SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is HOT and CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It is COLD and CLOUDY")
elif 0 < temp > 28 and not is_sunny: 
    print("It is WARM and CLOUDY")

 