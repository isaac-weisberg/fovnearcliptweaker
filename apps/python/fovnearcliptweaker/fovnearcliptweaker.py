import ac
from UIInstance import *

uiInstance = None

def acMain(ac_version):
    try:
        global uiInstance
        uiInstance = UIInstance()
    except Exception as e:
        ac.log('ASDF shit! {}'.format(e))
        
        return


def acUpdate(dt):
    if uiInstance != None:
        try:
            uiInstance.acUpdate(dt)
        except Exception as e:
            ac.log('ASDF update shat {}'.format(e))

