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


# You can also control multiple lamps by sending a list as lamp_id
b.set_light( [1,2,3], 'on', True)

# You can also use light names instead of the id

# The set_light method can also take a dictionary as the second argument to do more fancy stuff
# This will turn light 1 on with a transition time of 30 seconds
#command =  {'transitiontime' : 30, 'on' : True, 'bri' : 254}
#b.set_light(3, command)
#time.sleep(3)

#command =  {'transitiontime' : 30, 'on' : True, 'bri' : 64}
#b.set_light(3, command)

lights = b.get_light_objects()


initialOffset = 1000
for i in range(0,3):
	light = lights[i]
	#light.hue = random.randint(100,60000)
	light.hue = 1 + initialOffset
	initialOffset -= 1000
	light.saturation = 255
	light.brightness = 127
	light.transitiontime = 60

lights[0].hue = 7000
lights[1].hue = (lights[0].hue + 2000) % 65536
lights[2].hue = (lights[1].hue + 2000) % 65536


flip = False
seed = 0
while True:
	for i in range(0,3):
		print i
		light = lights[i]
		if True:
			#seed = random.randint(100,500)
			seed += 300
			if (light.hue + seed) > 12000:
				seed = 0
				light.hue = 0
			light.hue = (light.hue + seed) % 65535
			print light.hue
			time.sleep(1.5);
		if flip:
			#light.brightness = 0
			#light.transitiontime = False
			flip = False
		else: 
			#light.brightness = 255
			flip = True
	



