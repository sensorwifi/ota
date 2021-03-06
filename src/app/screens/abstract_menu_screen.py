from m5stack import lcd, buttonA, buttonB, buttonC
from .abstract_screen import AbstractScreen

class AbstractMenuScreen(AbstractScreen):

    def __init__(self):
        super().__init__()
        self.value = 1

    def show(self):
        super().show()
        buttonA.wasPressed(self._on_btnOk)
        buttonB.wasPressed(self._on_btnUp)
        buttonC.wasPressed(self._on_btnDown)
        
        self.resetScreen()
        self.printHeader()

        self.cursor = lcd.getCursor()
        if self.cursor[1] != 85:
            self.cursor = (self.cursor[0], self.cursor[1] + 15)
        
        self.printMenu()

    def hide(self):
        super().hide()
        buttonA.wasPressed(None)
        buttonB.wasPressed(None)
        buttonC.wasPressed(None)
    
    def printHeader(self):
        pass

    def getMenuItems(self):
        return []

    def back(self):
        super().back()
        self.value = 1

    def printMenu(self):
        self._menuItems = self.__filterMenuItems(self.getMenuItems())
        self._min = 1
        self._max = len(self._menuItems)

        lcd.font(lcd.FONT_DejaVu24, transparent=True)
        lcd.rect(self.cursor[0],self.cursor[1],320,240, lcd.WHITE, lcd.WHITE)
        lcd.setCursor(self.cursor[0],self.cursor[1])

        for i in range(self._max):
            selectedPrefix = '  '
            if (i+1) == self.value:
                selectedPrefix = '>'
            
            lcd.println('{} {}'.format(selectedPrefix, self._menuItems[i][0]))
    
    def _on_btnOk(self):
        buttonA.wasPressed(None)
        buttonB.wasPressed(None)
        buttonC.wasPressed(None)
        self._menuItems[self.value - 1][1]()

    def _on_btnUp(self):
        if self._min == self.value:
            self.value = self._max
        else:
            self.value = self.value - 1
        self.printMenu()

    def _on_btnDown(self):
        if self._max == self.value:
            self.value = self._min
        else:
            self.value = self.value + 1
        self.printMenu()

    def __filterMenuItems(self, menuItems):
        filtered_menuItems = [menuItem for menuItem in menuItems if AbstractMenuScreen.__isMenuItemEnabled(menuItem) ]
        return filtered_menuItems

    @staticmethod
    def __isMenuItemEnabled(menuItem):
        if len(menuItem) == 2:
            return True

        return menuItem[2] == True