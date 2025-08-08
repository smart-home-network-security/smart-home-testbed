from smart_home_testbed import init_device, TpLinkPlugTapo


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.tplink.iot"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the TpLinkPlugTapo constructor.
    """
    device = TpLinkPlugTapo(ipv4=ipv4)
    assert isinstance(device, TpLinkPlugTapo)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
    assert device.loop.is_running()


def test_init_device() -> None:
    """
    Test the init_device function,
    with a TpLinkPlugTapo object.
    """
    device = init_device("TpLinkPlugTapo", ipv4=ipv4)
    assert isinstance(device, TpLinkPlugTapo)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
    assert device.loop.is_running()
