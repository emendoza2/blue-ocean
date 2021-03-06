# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
from drawBot import *
import math

# CONSTANTS
W = 1024  # Width
H = 512   # Height
M = 32    # Margin
U = 32    # Unit (Grid Unit)
F = 64    # Frames (Animation)

# REMAP INPUT RANGE TO VARIABLE FONT AXIS RANGE
# (E.G. SINE WAVE(-1,1) to WGHT(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan  = inputMax  - inputMin   # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)

# DRAWS A GRID
def grid():
    strokeWidth(1)
    stroke(0,0,0.8)
    step_X = 0
    step_Y = 0
    increment_X = U
    increment_Y = U
    for x in range(32):
        polygon( (M+step_X, M), (M+step_X, H-M) )
        step_X += increment_X
    for y in range(16):
        polygon( (M, M+step_Y), (W-M, M+step_Y) )
        step_Y += increment_Y
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# NEW PAGE
def new_page():
    newPage(W, H)
    frameDuration(1/60)
    fill(0,0,1)
    rect(-2, -2, W+2, H+2)

# SET FONT
font("../../fonts/ttf/BlueOcean.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))
varWght = 0
step = -1

# MAIN
for frame in range(F-1):
    new_page()
    font("../../fonts/ttf/BlueOcean.ttf")
    #grid() # Toggle for grid view
    fill(1)
    stroke(None)
    fontSize((M*2.5))
    #print("Sine step:", sin(step))

    # ROW 1
    varWght = remap(sin(step),-1,1,400,900)
    fontVariations(wght=varWght)
    text("Blue Ocean", (M, M*13))

    # ROW 2
    varWght = remap(sin(step+0.5),-1,1,400,900)
    fontVariations(wght=varWght)
    text("Blue Ocean", (M, M*11))

    # ROW 3
    varWght = remap(sin(step+1),-1,1,400,900)
    fontVariations(wght=varWght)
    text("Blue Ocean", (M, M*9))

    # ROW 4
    varWght = remap(sin(step+1.5),-1,1,400,900)
    fontVariations(wght=varWght)
    text("Blue Ocean", (M, M*7))

    # ROW 5
    varWght = remap(sin(step+2),-1,1,400,900)
    fontVariations(wght=varWght)
    text("Blue Ocean", (M, M*5))

    # LARGE "Aa"
    fontSize(M*9)
    textBox("Aá", (M*13.75, M*(-0.5), M*18, M*14), align="center")
    fontSize(M*2.5)

    # ROW 6
    varWght = remap(sin(step+2.5),-1,1,400,900)
    fontVariations(wght=varWght)
    text("Blue Ocean", (M, M*3))

    # ROW 7
    varWght = remap(sin(step+3),-1,1,400,900)
    fontVariations(wght=varWght)
    text("Blue Ocean", (M, M*1))

    # MOVES THE ANIMATION FORWARD
    step += 0.1

# SAVE THE ANIMATION IN THIS SCRIPT'S DIRECTORY LOCATION
saveImage("variable-font-specimen-001.gif")
