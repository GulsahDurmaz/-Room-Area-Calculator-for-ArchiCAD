from archicad import ACConnection

# from archicad.releases.ac25.b3000types import ElementPropertyValue
conn = ACConnection.connect()

assert conn

acc = conn.commands
act = conn.types
acu = conn.utilities

elements = acc.GetElementsByType('Zone')
propArray = []
zoneName = acu.GetBuiltInPropertyId('Zone_ZoneName')
zoneArea = acu.GetBuiltInPropertyId('Zone_MeasuredArea')
zoneNumber = acu.GetBuiltInPropertyId('Zone_ZoneNumber')
zoneCategory = acu.GetBuiltInPropertyId('Zone_ZoneCategoryCode')
zoneLayer = acu.GetBuiltInPropertyId('ModelView_LayerName')
zoneNumber = acu.GetUserDefinedPropertyId('zone_calculator','zone_number')
totalArea = acu.GetUserDefinedPropertyId('zone_calculator','sum_of_zone_area') # Custom property for sum of unit areas
showFlag = acu.GetUserDefinedPropertyId('zone_calculator','total_area_show') # Custom flag to show unit number

# Adding properties to the list
propArray.append(zoneName) #0
propArray.append(zoneNumber) #1
propArray.append(totalArea) #2
propArray.append(zoneLayer) #3
propArray.append(zoneArea) #4
propArray.append(zoneCategory) #5
propArray.append(showFlag) #6
# propArray.append(zoneStory) #7
propArray.append

# Getting property values of the elements
value = acc.GetPropertyValuesOfElements(elements, propArray)

# Dictionary to store zone data by zone number
floorZones = {}
# Dictionary to store GUID for each zone
floorGuid = {}
# List to store room zones
roomZones = []
# Dictionary to store additional data for zones
extra = {}

# Processing each element to categorize zones
for index, element in enumerate(value):
    check = str(element.propertyValues[1].propertyValue.value) # zoneNumber
    if check == '':  # Skip if the zone number is empty
        continue
    if element.propertyValues[6].propertyValue.value == True:  # Check if the 'unit_number_show' flag is True
        # Store zones in floorZones by zone number
        floorZones[str(element.propertyValues[1].propertyValue.value)] = element
        # Store the GUID for each zone
        floorGuid[str(element.propertyValues[1].propertyValue.value)] = elements[index].elementId
        
    # Check if the zone is on the specified layer
    if element.propertyValues[3].propertyValue.value == 'Model Unit - Zone':  # Layer name for room stamps
        roomZones.append(element)
    else:
        continue

# Initialize total area to 0 for each zone
for key, value in floorZones.items():
    xstr = str(value.propertyValues[1].propertyValue.value)  # zoneNumber
    floorZones[xstr].propertyValues[2].propertyValue.value = 0 #totalArea

# Summing the areas for each room zone
for index, num in enumerate(roomZones):
    xstr = str(num.propertyValues[1].propertyValue.value)  # zoneNumber
    code = num.propertyValues[5].propertyValue.value # zoneCategory
    # Store the code and number for each zone
    extra[xstr] = {'code': code, 'number': xstr}
    tot = num.propertyValues[4].propertyValue.value  # zoneArea
    # Accumulate the area for each zone
    floorZones[xstr].propertyValues[2].propertyValue.value += tot

# Preparing the property values to be set in ArchiCAD
EPVArray = []
for key, value in floorZones.items():
    buffer = value.propertyValues[2].propertyValue.value  # totalArea
    index = str(value.propertyValues[1].propertyValue.value) # zoneNumber
    code = extra[index]['code']
    roomnum = extra[index]['number']
    normalnum = act.NormalStringPropertyValue(roomnum, type='string', status='normal')
    normalcode = act.NormalStringPropertyValue(code, type='string', status='normal')
    normalArea = act.NormalAreaPropertyValue(buffer, type='area', status='normal')
    element = floorGuid[index]
    EPV = act.ElementPropertyValue(element, totalArea, normalArea)  # Setting the accumulated area
    EPVArray.append(EPV)

# Sending the property values back to ArchiCAD
result = acc.SetPropertyValuesOfElements(EPVArray)
print(result)
