#!/usr/bin/python

from phue import Bridge

import time
import math
import random
import logging
logging.basicConfig()

b = Bridge('192.168.0.6')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
#b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
api = b.get_api()
#print api
print '1' , api['lights']['1']['state']['hue']
print '2' , api['lights']['2']['state']['hue']
print '3' , api['lights']['3']['state']['hue']


#colors = [25653, 65528, 63265]
s = 45000
colors = [s+0, s+4000, s+8000]

# Set brightness of lamp 3 to max
#b.set_light(3, 'bri', 127)
for i in range(0,3):
	command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254, 'sat': 254}
	print b.set_light(i+1, command)

c=0
while True:
	b.set_light(3, 'bri', 127)
	for i in range(0,3):
		print b.set_light(i+1, 'hue', colors[(c + i) % 3])
		command =  {'transitiontime' : 300, 'hue': colors[(c + i) % 3] }
		print b.set_light(i+1, command)
	c += 2
	time.sleep(3.0)
	


