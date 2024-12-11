from secrets import token_hex
from smart_home_testbed import init_device, XiaomiCamera


### VARIABLES ###

ipv4 = "192.168.1.2"
token = token_hex(16)
android_package = "com.xiaomi.smarthome"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the XiaomiCamera constructor.
    """
    device = XiaomiCamera(ipv4=ipv4, token=token)
    assert isinstance(device, XiaomiCamera)
    assert device.ip == ipv4
    assert device.token == token
    assert device.android_package == android_package


def test_init_device() -> None:
    """
    Test the init_device function,
    with a XiaomiCamera object.
    """
    device = init_device("XiaomiCamera", ipv4=ipv4, token=token)
    assert isinstance(device, XiaomiCamera)
    assert device.ip == ipv4
    assert device.token == token
    assert device.android_package == android_package
