from smart_home_testbed import init_device, TapoLight


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.tplink.iot"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the TapoLight constructor.
    """
    device = TapoLight(ipv4=ipv4)
    assert isinstance(device, TapoLight)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package


def test_init_device() -> None:
    """
    Test the init_device function,
    with a TapoLight object.
    """
    device = init_device("TapoLight", ipv4=ipv4)
    assert isinstance(device, TapoLight)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
