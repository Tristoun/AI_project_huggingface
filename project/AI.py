from stt import AudioRecorder
from text_generation import ChatAI
from object_detection import ObjectDetection

class AI() :
    def __init__(self) -> None:
        self.recorder = AudioRecorder()
        self.chat = ChatAI()
        self.objdetect = ObjectDetection()

    def log(self, output) :
        print(output)

    def run(self) :
        audio = self.recorder.record_audio()
        audio_command = audio.lower()

        if "open the camera" in audio_command :
            self.log("Opening camera")
            self.objdetect.detect_object()
            return "Object detection done"
        else :
            output = self.chat.generate_text(audio)
            return output

if __name__ ==  '__main__' :
    print("Starting ...")
    bot = AI()
    output = bot.run()
    print(output)