#
def hit_message():
    print("You took down the '{}' alien worth '{}' points".format(alien0['color'], alien0['points']))

def location_readout():
    print("""
    Your ship is moving at '{}' pace. 
    The new current x-location is {}""".format(alien0['speed'], alien0['x_position']))
    
#Defining alien and its values. Printing out single values
alien0 = {'color': 'green', 'points': '10'}
print(alien0['color'])
print(alien0['points'])
hit_message()

#Adding more keys/values to alien.
alien0['x_position'] = 0
alien0['y_position'] = 25
alien0['speed'] = 'medium'

#Moves the Alien to the right according to 'speed' value.
if alien0['speed'] == 'slow':
    alien0['x_position'] += 1
    location_readout()
elif alien0['speed'] == 'medium':
    alien0['x_position'] += 2
    location_readout()
elif alien0['speed'] == 'fast':
    alien0['x_position'] += 3
    location_readout()
else:
    print("""
    Ayo dis ship insanely fast. I can't calculate 
    its speed!! 
    """)
    
alien_vehicle_producer = {
    'V330':'Doobiu$',
    'R32Z':'WeDoSpaceshipsInc',
    'Zoomer':'CompanyZoomz'
}

#Loop through items() list returend from dictionary
# Saves values in vehicle and producer variables 
for vehicle, producer in alien_vehicle_producer.items():
    print("-------------")
    print("Vehicle: '{}'".format(vehicle))
    print("Manufacturer: '{}'".format(producer))
    print("-------------")





