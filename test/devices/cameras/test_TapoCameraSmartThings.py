import os
from smart_home_testbed import init_device, TapoCameraSmartThings


### VARIABLES ###

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ipv4 = "192.168.1.2"
android_package = "com.samsung.android.oneconnect"
path_screenshot_stream = os.path.join(parent_dir, "sample.png")


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the TapoCameraSmartThings constructor.
    """
    device = TapoCameraSmartThings(ipv4=ipv4, path_screenshot_stream=path_screenshot_stream)
    assert isinstance(device, TapoCameraSmartThings)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package


def test_init_device() -> None:
    """
    Test the init_device function,
    with a TapoCameraSmartThings object.
    """
    device = init_device("TapoCameraSmartThings", ipv4=ipv4, path_screenshot_stream=path_screenshot_stream)
    assert isinstance(device, TapoCameraSmartThings)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
