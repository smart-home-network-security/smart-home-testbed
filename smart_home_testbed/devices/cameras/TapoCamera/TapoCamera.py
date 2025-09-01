from ....DeviceState import CameraScreenshotState
from ....DeviceControl import CameraControl


class TapoCamera(CameraScreenshotState, CameraControl):
    """
    Tapo camera (C200).
    """

    ### Class attributes
    # Android package
    android_package = "com.tplink.iot"
    # SSIM threshold below which images are considered different
    SSIM_DIFF_THRESHOLD = 0.95
    ## Screen coordinates
    # Stream event
    x_start = 281
    y_start = 994
    x_stop = 65
    y_stop = 242
