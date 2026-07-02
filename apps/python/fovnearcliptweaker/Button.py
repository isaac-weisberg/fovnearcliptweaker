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
        ac.addOnClickedListener(self.button, onClick)
        ac.setSize(self.button, size.x, size.y)
        ac.setPosition(self.button, pos.x, pos.y)

    def setText(self, text):
        if self.text != text:
            self.text = text
            ac.setText(self.button, text)

    def maxY(self):
        return self.pos.y + self.size.y
