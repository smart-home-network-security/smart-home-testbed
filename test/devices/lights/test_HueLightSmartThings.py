from smart_home_testbed import init_device, HueLightEssentials


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.superthomaslab.hueessentials"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the HueLightEssentials constructor.
    """
    device = HueLightEssentials(ipv4=ipv4)
    assert isinstance(device, HueLightEssentials)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
    assert device.loop.is_running()


def test_init_device() -> None:
    """
    Test the init_device function,
    with a HueLightEssentials object.
    """
    device = init_device("HueLightEssentials", ipv4=ipv4)
    assert isinstance(device, HueLightEssentials)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
    assert device.loop.is_running()
