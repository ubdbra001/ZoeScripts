
# This sets pygame as the audio driver
from psychopy import prefs
prefs.general['audioLib'] = ['pygame']

# Import needed libraries
from psychopy import core, visual, data, event, sound

# Define length of trial
trialLength = 10

# Define function for playing sound`
def playSound(soundIn):
    beep = sound.Sound(soundIn, secs = 0.3)
    beep.setVolume(0.5)
    beep.play()
    core.wait(0.3)

# Set up window
win = visual.Window([600,600], monitor = "testMonitor")

# Import image info
stimList = data.importConditions('stimList.csv')
imageStim = dict()
soundStim = dict()

# Turn image info into stimuli
for stim in stimList:
    imageStim[stim['imageName']] = visual.ImageStim(win,
        image = 'images/%s' % stim['imageFile'],
        pos = stim['imagePos'],
        size = stim['imageSize'])
    soundStim[stim['imageName']] = stim['soundName']

# Set up mouse
mouse = event.Mouse(win = win)

# Set up countdown timer
routineTimer = core.CountdownTimer() 

# Draw all images to buffer
for stimulus in imageStim.values():
    stimulus.draw()

# Show drawn images
win.flip()

# Add trial length to countdown
routineTimer.add(trialLength)

# Do the following while the countdown timer is above 0
while routineTimer.getTime() > 0:
    
    # For each of the stimuli
    for name, stimulus in imageStim.items():
        # See if the mouse has been clicked in its bounds
        mousePress = mouse.isPressedIn(stimulus, buttons = [0])
        
        # If it has play a sound
        if mousePress:
            playSound(soundStim[name])
            mousePress = False

# Close the window
win.close()
 
# Close PsychoPy
core.quit()