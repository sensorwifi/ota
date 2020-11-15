from m5stack import *
from ...abstract_screen import AbstractScreen
from ...utils.string_selector import StringSelector
from app.hardware.kippenstal_config import kippenstalConfig

class DoorScheduleEnabledScreen(AbstractScreen):

    def show(self):
        super().show()
        lcd.print('Door Schedule On/Off', lcd.CENTER, 85)

        lcd.setCursor(160, 125)
        value = 'On' if kippenstalConfig.isDoorOpenerScheduleEnabled() else 'Off'
        self.stringSelector = StringSelector(value, 
            [ 'On', 'Off']
        )
        self.stringSelector.printToLcd()
        self.stringSelector.startEditing(self)

    def editingDone(self, editor:StringSelector):
        print('Door schedule state', self.stringSelector.value)
        value = True if self.stringSelector.value == 'On' else False
        kippenstalConfig.setDoorOpenerScheduleEnabled(value)
        super().back()