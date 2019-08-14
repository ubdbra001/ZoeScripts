from psychopy import core, visual

timeLimit = 60

red = 1
green = 0

win = visual.Window([400,400], monitor = "testMonitor")

frameRate = win.getActualFrameRate()
if frameRate != None:
    frameDur = 1.0 / round(frameRate)
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

colStep = frameDur/timeLimit

stimulus = visual.Circle(win, pos = (0,0), radius = 0.5, lineWidth = 0)

while red > 0:
    colour = [red, green, 0]
    
    stimulus.setFillColor(colour)
    stimulus.draw()
    win.flip()
    
    red = red - colStep
    green = green + colStep

# Close the window
win.close()
 
# Close PsychoPy
core.quit()