from smart_home_testbed import init_device, TpLinkPlugSmartThings


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.samsung.android.oneconnect"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the TpLinkPlugSmartThings constructor.
    """
    device = TpLinkPlugSmartThings(ipv4=ipv4)
    assert isinstance(device, TpLinkPlugSmartThings)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package


def test_init_device() -> None:
    """
    Test the init_device function,
    with a TpLinkPlugSmartThings object.
    """
    device = init_device("TpLinkPlugSmartThings", ipv4=ipv4)
    assert isinstance(device, TpLinkPlugSmartThings)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
