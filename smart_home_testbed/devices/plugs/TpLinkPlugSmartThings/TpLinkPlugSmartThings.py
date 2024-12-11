from ....DeviceState import TpLinkPlugState
from ....DeviceControl import SmartThingsPlugControl


class TpLinkPlugSmartThings(TpLinkPlugState, SmartThingsPlugControl):
    """
    TP-Link HS110 plug,
    controlled through SmartThings.
    """

    ## Class attributes
    # Screen to open the device controls
    device_x = 532.8
    device_y = 532.8
