import ac

class Label:
    def __init__(self, app, text, pos, size):
        self.pos = pos
        self.size = size

        self.label = ac.addLabel(app, text)
        ac.setPosition(self.label, pos.x, pos.y)
        ac.setSize(self.label, size.x, size.y)

    def setText(self, text):
        ac.setText(self.label, text)
    
    def maxY(self):
        return self.pos.y + self.size.y
