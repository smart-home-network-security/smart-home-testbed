from smart_home_testbed import init_device, HueLightSmartThings


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.samsung.android.oneconnect"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the HueLightSmartThings constructor.
    """
    device = HueLightSmartThings(ipv4=ipv4)
    assert isinstance(device, HueLightSmartThings)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package


def test_init_device() -> None:
    """
    Test the init_device function,
    with a HueLightSmartThings object.
    """
    device = init_device("HueLightSmartThings", ipv4=ipv4)
    assert isinstance(device, HueLightSmartThings)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
