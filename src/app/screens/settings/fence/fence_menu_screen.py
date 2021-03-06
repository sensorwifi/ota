from ...abstract_menu_screen import AbstractMenuScreen
from .fence_test_screen import FenceTestScreen
from .fence_state_selector_screen import FenceStateSelectorScreen
from app.hardware.fence import FenceConstants
from app.hardware.kippenstal_config import kippenstalConfig

class FenceMenuScreen(AbstractMenuScreen):

    def __init__(self):
        super().__init__()
        self._fenceTestScreen = FenceTestScreen()
        self._fenceStateSelectorScreen = FenceStateSelectorScreen()

    def getMenuItems(self):
        return [
                ('Test Fence', self._fenceTestScreen.show),
                ('Fence Schedule - {}'.format('off' if kippenstalConfig.getFenceOnState() == FenceConstants.alwaysOff else 'on'), self._fenceStateSelectorScreen.show),
                ('Back', super().back)
            ]
