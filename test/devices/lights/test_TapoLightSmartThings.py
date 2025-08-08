from smart_home_testbed import init_device, TapoLightSmartThings


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.samsung.android.oneconnect"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the TapoLightSmartThings constructor.
    """
    device = TapoLightSmartThings(ipv4=ipv4)
    assert isinstance(device, TapoLightSmartThings)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
    assert device.loop.is_running()


def test_init_device() -> None:
    """
    Test the init_device function,
    with a TapoLightSmartThings object.
    """
    device = init_device("TapoLightSmartThings", ipv4=ipv4)
    assert isinstance(device, TapoLightSmartThings)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
    assert device.loop.is_running()
