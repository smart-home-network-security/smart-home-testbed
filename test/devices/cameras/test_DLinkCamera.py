from smart_home_testbed import init_device, DLinkCamera


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.dlink.mydlinkunified"
path_screenshot_stream = "sample.png"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the DLinkCamera constructor.
    """
    device = DLinkCamera(ipv4=ipv4, path_screenshot_stream=path_screenshot_stream)
    assert isinstance(device, DLinkCamera)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package


def test_init_device() -> None:
    """
    Test the init_device function,
    with a DLinkCamera object.
    """
    device = init_device("DLinkCamera", ipv4=ipv4, path_screenshot_stream=path_screenshot_stream)
    assert isinstance(device, DLinkCamera)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
