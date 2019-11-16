#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
import random
from psychopy import visual, core, event, gui, logging

#Initialize answer and response arrays
correct_answer = []
response = []

## Begin loop here ##

# Begin with pre-stim fixation interval 
win = visual.Window(fullscr=True, 
                    allowGUI=False, 
                    color='white', 
                    unit='height'
                    ) 
fixation = visual.GratingStim(win=win, 
                              size=0.02, 
                              pos=[0,0], 
                              sf=0, 
                              rgb='black')
fixation.draw()

event.Mouse(visible=False)

keys = event.waitKeys(keyList =['space']) # Wait for space bar press to begin trial

win.flip()
core.wait(0.4)
win.close()

#Present target face image
win2 = visual.Window(fullscr=True, 
                    allowGUI=False, 
                    color='white', 
                    unit='height'
                    ) 

event.Mouse(visible=False)

temp = random.randint(1,8)
file = '/Users/jmsaito/Documents/GitHub/trialloops-jmsaito25/faces/face' + str(temp) + '.jpg'
current_face = visual.ImageStim(win2, image=file, pos=(0,0))

current_face.draw()

win2.flip()
core.wait(2)
win2.close()

#Delay Period
win3 = visual.Window(fullscr=True, 
                    allowGUI=False, 
                    color='white', 
                    unit='height'
                    ) 

event.Mouse(visible=False)

win.flip()
core.wait(3)
win.close()

#Present probe face
win4 = visual.Window(fullscr=True, 
                    allowGUI=False, 
                    color='white', 
                    unit='height'
                    )

event.Mouse(visible=False)

temp2 = random.randint(1,8)
file = '/Users/jmsaito/Documents/GitHub/trialloops-jmsaito25/faces/face' + str(temp2) + '.jpg'
current_face = visual.ImageStim(win4, image=file, pos=(0,0))

current_face.draw()

if temp == temp2:
    correct_answer.append(1)
else:
    correct_answer.append(0)
    
win4.flip()

#Gather participant same/different response
keys = event.waitKeys(keyList =['1','0'])
response.append(keys)
win4.close()

#End loop with blank screen to indicate end of trial
win5 = visual.Window(fullscr=True, 
                    allowGUI=False, 
                    color='white', 
                    unit='height'
                    )

win5.flip()
