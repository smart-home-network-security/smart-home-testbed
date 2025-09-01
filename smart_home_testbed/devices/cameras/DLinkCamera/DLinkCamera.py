from ....DeviceState import CameraScreenshotState
from ....DeviceControl import CameraControl


class DLinkCamera(CameraScreenshotState, CameraControl):
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
    x_start = 637
    y_start = 1479
    x_stop = 76
    y_stop = 1648
    # Error message
    x_error = 540
    y_error = 1333


    def start_stream(self) -> None:
        """
        Dismiss the potential error message,
        then start the camera's video stream.
        Overwrites the method from the parent class CameraControl.
        """
        phone = self.get_phone()
        phone.shell(f"input tap {self.x_error} {self.y_error}")
        phone.shell(f"input tap {self.x_start} {self.y_start}")
