#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import math
import pcbnew
from pcbnew import *


# http://kevincuzner.com/tag/pcbnew/
def place_circle(refdes, start_angle, center, radius, component_offset=0, hide_ref=True, lock=False):
    """
    Places components in a circle
    refdes: List of component references
    start_angle: Starting angle
    center: Tuple of (x, y) mils of circle center
    radius: Radius of the circle in mils
    component_offset: Offset in degrees for each component to add to angle
    hide_ref: Hides the reference if true, leaves it be if None
    lock: Locks the footprint if true
    """
    deg_per_idx = 360 / len(refdes)
    for idx, rd in enumerate(refdes):
        part = pcb.FindModuleByReference(rd)
        angle = (deg_per_idx * idx + start_angle) % 360;
        print "{0}: {1}".format(rd, angle)
        xmils = center[0] + math.cos(math.radians(angle)) * radius
        ymils = center[1] + math.sin(math.radians(angle)) * radius
        part.SetPosition(wxPoint(FromMils(xmils), FromMils(ymils)))
        part.SetOrientation((angle + 270) * -10)
        if hide_ref is not None:
            part.Reference().SetVisible(not hide_ref)


dir_path = os.path.dirname(os.path.realpath(__file__))
pcb_file = os.path.join(dir_path, 'clock.kicad_pcb')
pcb = pcbnew.LoadBoard(pcb_file)
pcb.BuildListOfNets()  # needed fo load file
# if running from pcbnew console
# pcb = pcbnew.GetBoard()

seconds_refs = [];
minutes_refs = [];
hours_refs = [];
refs = [];

for module in pcb.GetModules():
    ref = module.GetReference().encode('utf-8')
    if (ref.startswith('D')):
        refs.append(ref)
refs.reverse()

for seconds in range(0, 60):
    seconds_refs.append(refs.pop())
for minutes in range(0, 60):
    minutes_refs.append(refs.pop())
for hours in range(0, 60):
    hours_refs.append(refs.pop())

outerRadius = 5000
radiusStep = 600

radius = outerRadius
place_circle(seconds_refs, 270, (500, 500), radius)
radius -= radiusStep
place_circle(minutes_refs, 270, (500, 500), radius)
radius -= radiusStep
place_circle(hours_refs, 270, (500, 500), radius)

pcb.Save(pcb_file)
