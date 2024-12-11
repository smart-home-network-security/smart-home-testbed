from smart_home_testbed import init_device, HueLight


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.philips.lighting.hue2"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the HueLight constructor.
    """
    device = HueLight(ipv4=ipv4)
    assert isinstance(device, HueLight)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package


def test_init_device() -> None:
    """
    Test the init_device function,
    with a HueLight object.
    """
    device = init_device("HueLight", ipv4=ipv4)
    assert isinstance(device, HueLight)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
