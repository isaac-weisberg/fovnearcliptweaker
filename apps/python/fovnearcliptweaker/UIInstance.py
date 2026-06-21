try:
	import ac	
except ImportError:
	from acDevLibs.acDev import ac as ac
try:	
	import acsys	
except ImportError:
	from acDevLibs.acsysDev import acsys as acsys
from Slider import Slider
from vec2 import vec2
from vec3 import vec3
from Label import Label
from RangeMapping import RangeMapping

count = 0
uiInstance = None

class UIInstance:
    def __init__(self):
        width = 900
        self.freeCamOn = False

        self.fovRange = RangeMapping(60, 0.5, 0.25)
        self.nearClipRange = RangeMapping(1000, 0.75, 0.1)
        self.fov = None
        self.nearClip = None
        self.cameraMode = -1
        self.distanceToCar = None
        self._updateIndex = -1

        self.app = ac.newApp("Fov Near Clip Tweaker")

        startY = 48

        self.enabledButton = ac.addButton(self.app, 'Toggle Enabled')
        ac.addOnClickedListener(self.enabledButton, onFreeCamButtonClicked)
        ac.setSize(self.enabledButton, 200, 24)
        ac.setPosition(self.enabledButton, 16, startY)
        enabledButtonMaxY = 24 + startY

        self.fovTitle = Label(self.app, "FOV:", vec2(16, enabledButtonMaxY + 16), vec2(width - 32, 22))
        self.fovSlider = Slider(self.app, vec2(16, self.fovTitle.maxY()), vec2(width - 32, 24), onFovClick)

        self.nearClipTitle = Label(self.app, "Near clip:", vec2(16, self.fovSlider.maxY() + 16), vec2(width - 32, 22))
        self.nearClipSlider = Slider(self.app, vec2(16, self.nearClipTitle.maxY()), vec2(width - 32, 24), onNearClipClick)

        self.distanceToCarLabel = Label(self.app, "Distance to car:", vec2(16, self.nearClipSlider.maxY()), vec2(width - 32, 22))

        height = self.distanceToCarLabel.maxY() + 16

        ac.setSize(self.app, width, height)

        global uiInstance
        uiInstance = self

    def acUpdate(self, dt):
        self._updateIndex += 1

        if self._updateIndex % 30 == 0:
            fov = ac.ext_getCameraFov()
            if fov != self.fov:
                self.fov = fov
                self.fovSlider.setFill(self.fovRange.outToIn(fov))
                self.syncFovTitle()
            
            nearClip = ac.ext_getCameraClipNear()
            if nearClip != self.nearClip:
                self.nearClip = nearClip
                self.nearClipSlider.setFill(self.nearClipRange.outToIn(nearClip))
                self.syncNearClipTitle()

            cameraMode = ac.getCameraMode()
            if cameraMode != self.cameraMode:
                self.cameraMode = cameraMode
                if cameraMode == 6:
                    ac.setText(self.enabledButton, 'Disable free camera')
                else:
                    ac.setText(self.enabledButton, 'Enable free camera')
            
            distanceToCar = self.calcDistanceToCar()
            if distanceToCar != self.distanceToCar:
                self.distanceToCar = distanceToCar
                self.syncDistanceToCarLabel()
    
    def syncFovTitle(self):
        self.fovTitle.setText('FOV: {:.2f} degrees'.format(self.fov))
    
    def syncNearClipTitle(self):
        self.nearClipTitle.setText('Near Clip: {:.2f} meters'.format(self.nearClip))

    def syncDistanceToCarLabel(self):
        self.distanceToCarLabel.setText('Distance to car: {:.2f} meters'.format(self.distanceToCar))

    def onFreeCamButtonClicked(self):
        if self.cameraMode == 6:
            ac.setCameraMode(0)
        else:
            ac.setCameraMode(6)

    def handleFovClick(self, x, y):
        uiInstance.fovSlider.handleClick(x, y)
        range = uiInstance.fovSlider.size.x
        if range == 0:
            return

        fill = x / range

        fov = self.fovRange.inToOut(fill)
        
        ac.ext_setCameraFov(fov)
        self.fov = fov
        self.syncFovTitle()

    def handleNearClipClick(self, x, y):
        uiInstance.nearClipSlider.handleClick(x, y)
        range = uiInstance.nearClipSlider.size.x
        if range == 0:
            return

        fill = x / range
        nearClip = self.nearClipRange.inToOut(fill)
        
        ac.ext_setCameraClipNear(nearClip)
        self.nearClip = nearClip
        self.syncNearClipTitle()

    def calcDistanceToCar(self):
        carWorldPosition = ac.getCarState(0, acsys.CS.WorldPosition)
        carWorldPosition = vec3(carWorldPosition[0], carWorldPosition[1], carWorldPosition[2])

        cameraWorldPosition = ac.ext_getCameraPosition()
        cameraWorldPosition = vec3(cameraWorldPosition[0],cameraWorldPosition[1],cameraWorldPosition[2])

        distance = cameraWorldPosition.distance(carWorldPosition)
        
        return distance


def onFreeCamButtonClicked(x,y):
    uiInstance.onFreeCamButtonClicked()

def onFovClick(x,y):
    uiInstance.handleFovClick(x, y)

def onNearClipClick(x, y):
    uiInstance.handleNearClipClick(x, y)
