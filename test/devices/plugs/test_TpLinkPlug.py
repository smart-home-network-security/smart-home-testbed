from smart_home_testbed import init_device, TpLinkPlug


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.tplink.kasa_android"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the TpLinkPlug constructor.
    """
    device = TpLinkPlug(ipv4=ipv4)
    assert isinstance(device, TpLinkPlug)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
    assert device.loop.is_running()


def test_init_device() -> None:
    """
    Test the init_device function,
    with a TpLinkPlug object.
    """
    device = init_device("TpLinkPlug", ipv4=ipv4)
    assert isinstance(device, TpLinkPlug)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
    assert device.loop.is_running()
