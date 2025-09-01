from ....DeviceState import CameraScreenshotState
from ....DeviceControl import CameraErrorControl


class DLinkCamera(CameraScreenshotState, CameraErrorControl):
    """
    DLink camera (DCS-8000LH).
    """

    ### Class attributes
    # Android package
    android_package = "com.dlink.mydlinkunified"
    # SSIM threshold below which images are considered different
    SSIM_DIFF_THRESHOLD = 0.9
    ## Screen coordinates
    # Stream event
    x_start = 424.8
    y_start = 907.2
    x_stop = 57.6
    y_stop = 1008
    # Error message
    x_error = 360
    y_error = 806.4
