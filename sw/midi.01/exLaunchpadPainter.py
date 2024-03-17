#Example of enoMidiController functionality for Novation Launchpad
#Brygg Ullmer, Clemson University
#Begun 2023-09-06

import sys, os
from pygame import time
from enoMidiController import *
from functools   import partial

#### callback function ####

def painterCB(emc, control, arg):
  if control[0] == 'm': #margin button
    whichMarginKey = control[1]

    if emc.isRightMargin(whichMarginKey):
      color = emc.getRightMarginColor(whichMarginKey)
      emc.setActiveColor(color)
      emc.topMarginFadedColor(color)

    if emc.isTopMargin(whichMarginKey):
      color = emc.getTopMarginColor(whichMarginKey)
      emc.setActiveColor(color)
      
  else: 
    x, y    = emc.addr2coord(control)
    r, g, b = emc.getActiveColor()
    emc.setLaunchpadXYColor(x, y, r, g, b)

#### main ####

emc = enoMidiController('nov_launchpad_x')
#emc = enoMidiController('nov_launchpad_mk2')
emc.clearLights()
emc.rightMarginRainbow()
emc.registerExternalCB(painterCB)

while True:
  emc.pollMidi()
  time.wait(100)

### end ###
