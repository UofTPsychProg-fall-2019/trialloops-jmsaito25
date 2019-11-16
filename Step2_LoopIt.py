#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%%
#In the task, there are 8 trials. To begin a trial, press the space bar. After a
#short delay, a face will be shown. After another brief delay, a second face will
#be shown. If the second face is the same as the first, press 1. If different,
#press 0. Once you submit your response to the second image, the screen will go 
#blank and you can begin the next trial by pressing the space bar. Once you 
#complete the last trial, the program will close automatically. The script outputs
#a 'test_data' text file that contains the correct answer to each trial, and the 
#participant's response in separate columns. 

#%%
import numpy as np
import pandas as pd
import os, sys
import random
from psychopy import visual, core, event

#Initialize answer and response arrays
correct_answer = []
response = []

#Initialize stim lists
target = list(range(1,8))
probe = list(range(1,8))
np.random.shuffle(target)
np.random.shuffle(probe)

#%%
for x in range(len(target)):
    win = visual.Window(fullscr=True, 
                    allowGUI=False, 
                    color='white', 
                    unit='height'
                    ) 
    fixation = visual.GratingStim(win=win, 
                              size=0.01, 
                              pos=[0,0], 
                              sf=0, 
                              rgb='black')
    fixation.draw()
    
    keys = event.waitKeys(keyList =['space']) # Wait for space bar press to begin trial

    event.Mouse(visible=False)
    
    win.flip()
    core.wait(0.5)
    win.close()
    #Present target face image
    win2 = visual.Window(fullscr=True, 
                    allowGUI=False, 
                    color='white', 
                    unit='height'
                    ) 

    temp = target[x]
    file = '/Users/jmsaito/Documents/GitHub/trialloops-jmsaito25/faces/face' + str(temp) + '.jpg'
    current_face = visual.ImageStim(win2, image=file, pos=(0,0))

    current_face.draw()

    event.Mouse(visible=False)
    
    win2.flip()
    core.wait(0.5)
    win2.close()
    #Delay Period
    win3 = visual.Window(fullscr=True, 
                    allowGUI=False, 
                    color='white', 
                    unit='height'
                    ) 
    
    fixation = visual.GratingStim(win=win3, 
                              size=0.01, 
                              pos=[0,0], 
                              sf=0, 
                              rgb='black')
    
    event.Mouse(visible=False)
    
    win3.flip()
    core.wait(3)
    win3.close()
    #Present probe face
    win4 = visual.Window(fullscr=True, 
                    allowGUI=False, 
                    color='white', 
                    unit='height'
                    )

    temp2 = probe[x]
    file = '/Users/jmsaito/Documents/GitHub/trialloops-jmsaito25/faces/face' + str(temp2) + '.jpg'
    current_face = visual.ImageStim(win4, image=file, pos=(0,0))

    current_face.draw()

    if temp == temp2:
        correct_answer.append(1)
    else:
        correct_answer.append(0)
    
    event.Mouse(visible=False)
    
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
    event.Mouse(visible=False)
    
    win5.flip()
    
#%%
core.wait(0.5)
win5.close()

data = pd.DataFrame({'answer':correct_answer,'response':response})
data.to_csv('test_data', sep='\t')