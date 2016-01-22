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
b.get_api()

# Prints if light 3 is on or not
b.get_light(2, 'on')

# Set brightness of lamp 3 to max
b.set_light(3, 'bri', 127)

# Set brightness of lamp 2 to 50%
b.set_light(2, 'bri', 127)

# Turn lamp 2 on
b.set_light(2,'on', True)

# You can also control multiple lamps by sending a list as lamp_id
b.set_light( [1,2], 'on', True)

# Get the name of a lamp
b.get_light(3, 'name')

# You can also use light names instead of the id

# The set_light method can also take a dictionary as the second argument to do more fancy stuff
# This will turn light 1 on with a transition time of 30 seconds
command =  {'transitiontime' : 30, 'on' : True, 'bri' : 254}
b.set_light(3, command)
#time.sleep(3)

command =  {'transitiontime' : 30, 'on' : True, 'bri' : 64}
b.set_light(3, command)

lights = b.get_light_objects()


for i in range(0,3):
	light = lights[i]
	light.hue = random.randint(100,60000)
	light.saturation = 255
	light.brightness = 127
	light.transitiontime = 30

while True:
	for i in range(0,3):
		print i
		light = lights[i]
		seed = random.randint(100,500000)
		if (light.hue + seed) > 30000:	
			light.hue = (light.hue + seed - 15000) % 65535
		else:
			light.hue = light.hue + seed
		print light.hue
		time.sleep(1.0);
	



