
class Phone:
    def make_call(self):
        raise NotImplementedError("make_call() must be implemented.")


class VideoCamera:
    def video_call(self):
        print("Making a video call using the video camera.")


class VideoCameraAdapter(Phone):
    def __init__(self, video_camera: VideoCamera):
        self.video_camera = video_camera
    
    def make_call(self):
        
        self.video_camera.video_call()


def main():
   
    video_camera = VideoCamera()

    
    phone = VideoCameraAdapter(video_camera)

    
    phone.make_call()  

if __name__ == "__main__":
    main()
