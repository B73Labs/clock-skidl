#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.environ['KICAD_SYMBOL_DIR'] = '/usr/share/kicad/library'
os.environ['KISYSMOD'] = '/usr/share/kicad/modules'

from skidl import *

gnd = skidl.Net('GND')
vdd = skidl.Net('VDD')

num_leds = 60 + 60 + 60;

# Create an LED template that will be copied for each LED needed.
led = Part(lib='LED', name='WS2813', footprint='LED_SMD:LED_Normandled_WS2813-06_5.0x5.0mm_Pitch1.6mm', dest=TEMPLATE)
leds = []
dout = []
for i in range(num_leds):
    leds.append(led())
    dout.append(skidl.Net('DOUT' + str(i)))
    leds[i]['DIN'] += dout[i]
    leds[i]['VDD'] += vdd
    leds[i]['GND'] += gnd
    leds[i]['VCC'] += NC
    if i > 0:
        # connect input to previous output
        leds[i - 1]['DOUT'] += dout[i]
        leds[i]['BIN'] += dout[i - 1]

# don't connect the output of the last LED
leds[-1]['DOUT'] += NC
# connect the backup input to the first input
leds[0]['BIN'] += dout[0]

# connect the input of the first LED to a pin header
header = skidl.Part(
    'Connector_Generic', 'Conn_01X03',
    footprint='Connector_PinHeader_1.00mm:PinHeader_1x03_P1.00mm_Horizontal'
)
header[1] += gnd
header[2] += vdd
header[3] += dout[0]

# assume that power is applied to pin header
header[1].net.drive = skidl.POWER
header[2].net.drive = skidl.POWER

# Example Decoupling Capacitor
decoupling_caps = []
decoupling_caps.append(skidl.Part('Device', 'C', footprint='Capacitor_SMD:C_0805_2012Metric'))
decoupling_caps.append(skidl.Part('Device', 'C', footprint='Capacitor_SMD:C_0603_1608Metric'))

for i in range(2):
    decoupling_caps[i][1] += vdd
    decoupling_caps[i][2] += gnd

skidl.ERC()  # Look for rule violations.
skidl.generate_netlist()  # Generate netlist file.
