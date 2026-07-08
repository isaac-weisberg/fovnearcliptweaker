try:
	import ac	
except ImportError:
	from acDevLibs.acDev import ac as ac
from Button import Button
from vec2 import vec2
from vec3 import vec3
from theme import accentColor, widgetBgColor

whiteColor = vec3(1, 1, 1)

class NearClipControlWidget:
	def __init__(self, app, pos, height, onNoControl, onFollowDistance):
		self.pos = pos
		self.height = height
		minX = pos.x
		self.currentValue = 0

		self.bg = Button(app, '', vec2(minX, pos.y), vec2(0, height))
		self.bg.setDrawBorder(0)
		self.bg.setBackgroundColor(widgetBgColor)

		self.controlButtonNone = Button(app, 'No Control', vec2(minX, pos.y), vec2(160, height), onClick=onNoControl)
		self.controlButtonNone.setDrawBorder(0)
		self.controlButtonNone.setBackgroundColor(accentColor)
		self.controlButtonFollowDistance = Button(app, 'Follow Distance', vec2(self.controlButtonNone.maxX() + 16, pos.y), vec2(200, height), onClick=onFollowDistance)
		self.controlButtonFollowDistance.setDrawBorder(0)
		self.controlButtonFollowDistance.setBackgroundColor(accentColor)
		self.maxX = self.controlButtonFollowDistance.maxX()

		self.bg.setSize(vec2(self.maxX - minX, height))

		self.syncCurrentValue()

	def syncCurrentValue(self):
		self.controlButtonNone.setFontColor(widgetBgColor if self.currentValue == 0 else whiteColor)
		self.controlButtonNone.setBackgroundOpacity(1 if self.currentValue == 0 else 0)
		self.controlButtonFollowDistance.setBackgroundOpacity(1 if self.currentValue == 1 else 0)
		self.controlButtonFollowDistance.setFontColor(widgetBgColor if self.currentValue == 1 else whiteColor)

	def setValue(self, value):
		self.currentValue = value
		self.syncCurrentValue()
	