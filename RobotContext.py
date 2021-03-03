class RobotContext:

    # Construct
    def __init__(self,realSense):
        self.realSense = realSense
        self.camerasContext = realSense.context()

    # Verify if there are cameras availables
    def isThereCamera(self):
        if len(camerasContext.devices) > 0:
            return True
        else:
            return False

    # Get a specific Ccmera
    def getCamera(self,camera):
        for camera in camerasContext.devices:
            if camera in camera.get_info(realSense.camera_info.name):
                return camera
        else:
            return None
