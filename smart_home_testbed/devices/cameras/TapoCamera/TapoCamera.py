from ....DeviceState import CameraScreenshotState
from ....DeviceControl import CameraErrorControl


class TapoCamera(CameraScreenshotState, CameraErrorControl):
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
    x_start = 187.2
    y_start = 446.4
    x_stop = 50.4
    y_stop = 100.8
    # Error message
    x_error = 540
    y_error = 2231
