#!/usr/bin/env python3
"""Example code for testing Foscam video"""

import argparse
import cv2
import foscam

class TestVideo:

    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password
        self.image = None
        self.userdata = None
        self.cam = foscam.Foscam(self.url, self.user, self.password)

    def frame_callback(self, image, userdata):
        self.image = image
        self.userdata = userdata

    def run(self):
        userdata = 'test' # not really used
        resolution = self.cam.RESOLUTION['640x480']
        rate = self.cam.RATE_FPS['2']
        self.cam.start_video(self.frame_callback, userdata, resolution, rate)

if __name__ == "__main__":
    """Example code for testing Foscam video"""

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The IP address of the camera")
    parser.add_argument("user", help="The user account on the camera")
    parser.add_argument("password", help="The password of the user account")
    args = parser.parse_args()

    print("Opening display window...")
    window_name = f"Display {args.url}"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    print("Opening camera...")
    test_video = TestVideo(args.url, args.user, args.password)

    print("Starting video...")
    test_video.run()

    for view in ['up', 'down', 'left', 'right', 'preset']:
        print (f"Moving camera (to) {view}...")
        test_video.cam.move_ptz(view)

        print ("Show video...")
        for i in range(100):
            if test_video.image is not None:
                cv2.imshow(window_name, test_video.image)
                test_video.image = None
            cv2.waitKey(100)

    print("Stopping video...")
    test_video.cam.stop_video()
    cv2.destroyAllWindows()
