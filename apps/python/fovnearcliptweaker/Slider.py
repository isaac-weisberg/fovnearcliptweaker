import ac

class Slider:
    def __init__(self, app, pos, size, handler):
        self.pos = pos
        self.size = size

        self.bg = ac.addButton(app, '')
        ac.setPosition(self.bg, pos.x, pos.y)
        ac.setSize(self.bg, size.x, size.y)
        ac.drawBackground(self.bg, 1)
        ac.setBackgroundColor(self.bg, 0,0,0)
        ac.setBackgroundOpacity(self.bg, 0.7)
        ac.drawBorder(self.bg, 0)

        self.fg = ac.addButton(app, '')
        ac.setPosition(self.fg, pos.x, pos.y)
        ac.setSize(self.fg, size.x / 2, size.y)
        ac.drawBackground(self.fg, 1)
        ac.setBackgroundColor(self.fg, 1,0.2,0)
        ac.setBackgroundOpacity(self.fg, 1)
        ac.drawBorder(self.fg, 0)

        ac.addOnClickedListener(self.bg, handler)
    
    def setFill(self, fill):
        ac.setSize(self.fg, self.size.x * fill, self.size.y)

    def handleClick(self, x, y):
        ac.setSize(self.fg, x, self.size.y)

    def maxY(self):
        return self.pos.y + self.size.y