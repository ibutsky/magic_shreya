
### HELLO THIS IS MY SILLY COMMENT 
### I can edit now
### Need to figure out how to take in input of points
import math

import numpy as np

print('What is the radius of the star your planet is orbiting')
starRadius = input()
print('What is the filename of your data')
fn = input()
time, flux = np.loadtxt(fn, unpack = True, skiprows =1)
print(time, flux)

minstorenumber = np.min(points)
maxstorenumber = np.max(points)

for index in range(len(points)):
    print(points[index][1])
    #first time store number
    if index == 0:
        maxstorenumber = points[index][1]
    #compare current and past
    #if current > past then keep current
    elif points[index][1] > maxstorenumber:
        maxstorenumber = points[index][1]
    #if current < past then keep past
    #if current = past then keep current
print('This is your maximum y-value from your points, ' + str(maxstorenumber) + ' .')
    
#doing square root of min-max--> exoplanet radius
sqNumber = maxstorenumber - minstoremumber
exoRadiuspre = math.sqrt(sqNumber)
exoRadius = int(exoRadiuspre) * int(starRadius)
print('The radius of your planet is ' + str(exoRadius) + '.')

#    prevnumber = points[index][]
#sqNumber = min(Points) - max(Points)
#finStep = sqrt(sqNumber)
#exoRadius = (finStep*starRadius)
#print( 'The radius of your exoplanet is' + exoRadius + '.')
