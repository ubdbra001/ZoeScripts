from psychopy import core, visual

# Set trial time limit
timeLimit = 60

# Set starting values for red and green
red = 1
green = 0

# Setup window
win = visual.Window([400,400], monitor = "testMonitor")

# Calculate frame rate and frame duration
frameRate = win.getActualFrameRate()
if frameRate != None:
    frameDur = 1.0 / round(frameRate)
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Calculate how many frames (and therefore steps) there are in the time limit
colStep = frameDur/timeLimit

# Draw the stimulus
stimulus = visual.Circle(win, pos = (0,0), radius = 0.5, lineWidth = 0)

# While red is not 0
while red > 0:
    # Update colour variable 
    colour = [red, green, 0]
    
    # Set the colour
    stimulus.setFillColor(colour)
    
    # Draw the stimulus
    stimulus.draw()

    # Flip the window 
    win.flip()

    # Change red and green values     
    red = red - colStep
    green = green + colStep

# Close the window
win.close()
 
# Close PsychoPy
core.quit()
