from .TapoControl import TapoControl
from .PlugControl import PlugControl


class TapoPlugControl(TapoControl, PlugControl):
    """
    Abstract class to control a generic plug through the Tapo app.
    """

    # Toggle coordinates
    x = 612
    y = 619.2
