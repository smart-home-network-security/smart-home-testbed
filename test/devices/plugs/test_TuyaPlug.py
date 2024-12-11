from smart_home_testbed import init_device, TuyaPlug


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.tuya.smart"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the TuyaPlug constructor.
    """
    device = TuyaPlug(ipv4=ipv4)
    assert isinstance(device, TuyaPlug)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package


def test_init_device() -> None:
    """
    Test the init_device function,
    with a TuyaPlug object.
    """
    device = init_device("TuyaPlug", ipv4=ipv4)
    assert isinstance(device, TuyaPlug)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
