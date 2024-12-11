import os
from smart_home_testbed import init_device, TuyaLight


### VARIABLES ###

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ipv4 = "192.168.1.2"
android_package = "com.tuya.smart"
path_screenshot_off = os.path.join(parent_dir, "sample.png")


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the TuyaLight constructor.
    """
    device = TuyaLight(ipv4=ipv4, path_screenshot_off=path_screenshot_off)
    assert isinstance(device, TuyaLight)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package


def test_init_device() -> None:
    """
    Test the init_device function,
    with a TuyaLight object.
    """
    device = init_device("TuyaLight", ipv4=ipv4, path_screenshot_off=path_screenshot_off)
    assert isinstance(device, TuyaLight)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
