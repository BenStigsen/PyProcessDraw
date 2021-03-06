# Screen Options
screenW = 800
screenH = 800

# Brush Options
brushSize   = 20            # Width
brushCenter = brushSize / 2 # Center

# Palette Options
colorSize  = 30
strokeSize = 3 # Stroke Options

# Palette
class Palette(object):
    def __init__(self, x=0, y=0, s=0):
        self.x = x
        self.y = y
        self.w = s
        self.h = s

# Color Class
class Color(Palette):
    def __init__(self, x, y, s, c):
        super(Color, self).__init__(x, y, s)
        self.c = c
    
    def isMouseOn(self):
        if (mouseX >= self.x) and (mouseX <= self.x + self.w):
            if (mouseY >= self.y) and (mouseY <= self.y + self.h):
                return True
            
# Color Palette
palette = Palette()
colors = [
    Color(10, 10, colorSize, "#FF4444"),  # Red
    Color(50, 10, colorSize, "#33DD33"),  # Green
    Color(90, 10, colorSize, "#6666FF"),  # Blue
    Color(130, 10, colorSize, "#FFFFFF"), # White
    Color(170, 10, colorSize, "#000000"), # Black
    Color(10, 50, colorSize, "#FFAA66"),  # Orange
    Color(50, 50, colorSize, "#FFFF66"),  # Yellow
    Color(90, 50, colorSize, "#FF66FF"),  # Pink
    Color(130, 50, colorSize, "#66FFFF"), # Cyan
    Color(170, 50, colorSize, "#885555"), # Brown
]

# Drawing Options
colorEraser  = ""
colorCurrent = Color(screenW - (colorSize + 10), 10, colorSize, colors[0].c)

# Setup
def setup():
    # Set current color and eraser color
    global colorEraser, colorCurrent
    colorEraser = g.backgroundColor
    colorCurrent.c = colors[0].c
    
    # Options
    size(screenW, screenH)
    textSize(18)
    textAlign(CENTER)
    
    # Set palette width and height
    for c in colors:
        if ((c.x + c.w) > palette.w):
            palette.w = c.x + c.w + strokeSize
        if ((c.y + c.h) > palette.h):
            palette.h = c.y + c.h + strokeSize
    
    # Clear the screen
    clear()

# Draw Loop
def draw():
    fill(colorEraser)
    stroke(0)
    strokeWeight(strokeSize)
    square(screenW - (colorSize + 10), screenH - (colorSize + 10), colorSize)
    fill(0)
    text(int(brushSize), screenW - (colorSize - 5), screenH - (colorSize - 12))
    noStroke()

# Clear Screen
def clear():
    background(colorEraser)
    drawPalette()
    drawColorCurrent()

# Draw Palette
def drawPalette():
    strokeWeight(strokeSize)
    stroke(0)

    # Draw color palette
    for c in colors:
        fill(c.c)
        square(c.x, c.y, c.w)
    
    noStroke()
    
# Draw Current Color
def drawColorCurrent():
    strokeWeight(strokeSize)
    stroke(0)
    fill(colorCurrent.c)
    
    # Draw
    square(colorCurrent.x, colorCurrent.y, colorCurrent.w)
    noStroke()

# Mouse Release
def mousePressed():
    global colorCurrent
    
    # Set currently selected color
    if (mouseX < palette.w) and (mouseY < palette.h):
        for c in colors:
            if (c.isMouseOn()):
                colorCurrent.c = c.c
                drawColorCurrent()
                break

# Mouse Drag (draw / erase)
def mouseDragged():
    # Draw
    if (mouseButton == LEFT):
        fill(colorCurrent.c)
        square(mouseX - brushCenter, mouseY - brushCenter, brushSize)
    # Erase
    elif (mouseButton == RIGHT):
        fill(colorEraser)
        square(mouseX - brushCenter, mouseY - brushCenter, brushSize)
    
    # Only redraw palette when drawn over / erased
    if (mouseX < palette.w + brushCenter) and (mouseY < palette.h + brushCenter):
        drawPalette()

    # Only redraw current color when drawn over / erased
    elif (mouseX > screenW - (colorCurrent.x + strokeSize)) and (mouseY < (colorCurrent.y + colorSize + brushCenter + strokeSize)):
        drawColorCurrent()

# Key Release
def keyReleased():
    global brushSize, brushCenter
    
    # Clear the screen
    if (str(key).lower() == 'c'):
        clear()
    # Go Crazy
    elif (str(key).lower() == 'g'):
        goCrazy(int(random(3, 20)))
    # Change brush size
    elif (key == CODED):
        if ((keyCode == UP) and (brushSize < 85)):
            brushSize = brushSize * 1.2
            brushCenter = brushSize / 2
        elif ((keyCode == DOWN) and (brushSize > 5)):
            brushSize = brushSize / 1.2
            brushCenter = brushSize / 2

# Go Crazy
def goCrazy(n):
    if (n > 0):
        strokeWeight(int(random(2, 25)))
        stroke(
            int(random(80, 210)), 
            int(random(80, 210)),
            int(random(80, 210))
        )

        line(
             int(random(-50, screenW + 50)), 0, 
             int(random(-50, screenW + 50)), screenH
        )

        goCrazy(n - 1)
    
    noStroke()
    drawPalette()
    drawColorCurrent()
    
