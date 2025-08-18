import string
import random
from smart_home_testbed import init_device, HueLight


### VARIABLES ###

ipv4 = "192.168.1.2"
android_package = "com.philips.lighting.hue2"

# Generate sample Philips Hue app key
len_appkey = 40
chars = string.ascii_letters + string.digits



### TEST FUNCTIONS ###

def test_constructor() -> None:
    """
    Test the HueLight constructor.
    """
    appkey = ''.join(random.choices(chars, k=len_appkey))
    device = HueLight(ipv4=ipv4, appkey=appkey)
    assert isinstance(device, HueLight)
    assert device.ipv4 == ipv4
    assert device.appkey == appkey
    assert device.android_package == android_package
    assert device.loop.is_running()


def test_init_device() -> None:
    """
    Test the init_device function,
    with a HueLight object.
    """
    appkey = ''.join(random.choices(chars, k=len_appkey))
    device = init_device("HueLight", ipv4=ipv4, appkey=appkey)
    assert isinstance(device, HueLight)
    assert device.ipv4 == ipv4
    assert device.appkey == appkey
    assert device.android_package == android_package
    assert device.loop.is_running()
