import math

import matplotlib.pyplot as plt

import numpy as np

def return_filename(filenumber):
    filename = 'data/hlsp_k2sff_k2_lightcurve_%i-c02_kepler_v1_llc-default-aper.txt' %(filenumber)
    return filename

print('What is your file number?')
filenumber = int(input())
fn = return_filename(filenumber)
time, flux = np.loadtxt(fn, delimiter=',', unpack=True, skiprows = 1, usecols=(0,1))

plt.scatter(time,flux)                                          
plt.xlabel('Time (days)')
plt.ylabel('Relative Flux')
plt.show()

print('What do you want as your start time?')
startTime = float(input())
print('What do you want as your end time?')
endTime = float(input())

print('What is the radius of the star your planet is orbiting? If you do not know, then type 0')
starRadius = float(input())
if starRadius > 0:
     print('What is the unit?')
     unit = input()

mask = (time>startTime)&(time<endTime)
time = time[mask]
flux = flux[mask]
 
medianstorenumber = np.median(flux)
minstorenumber = np.min(flux)
plt.scatter(time,flux)
#plt.show()
plt.xlabel('Time (days)')
plt.ylabel('Relative Flux')
#plt.xlim(2350, 2360)
#plt.ylim(0.995, 1.003)
plt.show()

for index in range(len(flux)):
    #first time store number
    if index == 0:
        maxstorenumber = flux[index]
    #compare current and past
    #if current > past then keep current
    elif flux[index] > maxstorenumber:
        maxstorenumber = flux[index]
    #if current < past then keep past
    #if current = past then keep current
print('This is your median y-value from your points, ' + str(medianstorenumber) + ' .')
print('This is your minimum y-value from your points, ' + str(minstorenumber) + ' .')    

#doing square root of min-max--> exoplanet radius
sqNumber = medianstorenumber - minstorenumber
exoRadiuspre = math.sqrt(sqNumber)
exoRadius = exoRadiuspre * starRadius
if starRadius == 0 :
    print('That radius of your planet in stellar radii is ' + str(exoRadiuspre) + ' .')
else:
    print('The radius of your planet is %f %s'%(exoRadius, unit))
