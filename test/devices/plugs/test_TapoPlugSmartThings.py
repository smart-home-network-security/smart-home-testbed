from smart_home_testbed import init_device, TapoPlugSmartThings


### VARIABLES ###

ipv4 = "192.168.1.2"
username = "user"
password = "password"
android_package = "com.samsung.android.oneconnect"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the TapoPlugSmartThings constructor.
    """
    device = TapoPlugSmartThings(ipv4=ipv4, username=username, password=password)
    assert isinstance(device, TapoPlugSmartThings)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
    assert device.loop.is_running()


def test_init_device() -> None:
    """
    Test the init_device function,
    with a TapoPlugSmartThings object.
    """
    device = init_device("TapoPlugSmartThings", ipv4=ipv4, username=username, password=password)
    assert isinstance(device, TapoPlugSmartThings)
    assert device.ipv4 == ipv4
    assert device.android_package == android_package
    assert device.loop.is_running()
