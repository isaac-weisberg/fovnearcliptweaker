from vec2 import vec2

try:
	import ac	
except ImportError:
	from acDevLibs.acDev import ac as ac

class Button:
    def __init__(self, app, text, pos, size, onClick = None):
        self.app = app
        self.button = ac.addButton(self.app, text)
        self.pos = pos
        self.size = size
        self.text = text
        if onClick != None:
            ac.addOnClickedListener(self.button, onClick)
        ac.setSize(self.button, size.x, size.y)
        ac.setPosition(self.button, pos.x, pos.y)
        ac.drawBackground(self.button, 1)

    def setText(self, text):
        if self.text != text:
            self.text = text
            ac.setText(self.button, text)

    def setDrawBorder(self, enabled):
        ac.drawBorder(self.button, enabled)
    
    def setFontColor(self, color, a = 1.0):
        ac.setFontColor(self.button, color.x, color.y, color.z, a)

    def setBackgroundColor(self, color):
        ac.setBackgroundColor(self.button, color.x, color.y, color.z)

    def setBackgroundOpacity(self, opacity):
        ac.setBackgroundOpacity(self.button, opacity)

    def maxY(self):
        return self.pos.y + self.size.y

    def setSize(self, size):
         ac.setSize(self.button, size.x, size.y)

    def maxX(self):
        return self.pos.x + self.size.x
