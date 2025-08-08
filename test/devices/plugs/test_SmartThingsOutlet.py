from uuid import uuid4
from smart_home_testbed import init_device, SmartThingsOutlet


### VARIABLES ###

ipv4 = "192.168.1.2"
id = str(uuid4())
token = "smart-things-token"
android_package = "com.samsung.android.oneconnect"


### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the SmartThingsOutlet constructor.
    """
    device = SmartThingsOutlet(ipv4=ipv4, id=id, token=token)
    assert isinstance(device, SmartThingsOutlet)
    assert device.ipv4 == ipv4
    assert device.id == id
    assert device.token == token
    assert device.android_package == android_package
    assert device.loop.is_running()


def test_init_device() -> None:
    """
    Test the init_device function,
    with a SmartThingsOutlet object.
    """
    device = init_device("SmartThingsOutlet", ipv4=ipv4, id=id, token=token)
    assert isinstance(device, SmartThingsOutlet)
    assert device.ipv4 == ipv4
    assert device.id == id
    assert device.token == token
    assert device.android_package == android_package
    assert device.loop.is_running()
