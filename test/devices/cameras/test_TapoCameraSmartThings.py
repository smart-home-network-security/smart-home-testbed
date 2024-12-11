from smart_home_testbed import init_device, TapoCameraSmartThings


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.samsung.android.oneconnect"
path_screenshot_stream = "sample.png"


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
