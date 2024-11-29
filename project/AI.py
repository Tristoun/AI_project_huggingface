from stt import AudioRecorder
from text_generation import ChatAI
from object_detection import ObjectDetection
from translate import Translator

class AI() :
    def __init__(self) -> None:
        self.recorder = AudioRecorder()
        self.chat = ChatAI()
        self.objdetect = ObjectDetection()
        self.translator = Translator()

    def log(self, output) :
        print(output)

    def run(self) :
        audio = self.recorder.record_audio()
        audio_command = audio.lower()

        if "open the camera" in audio_command :
            self.log("Opening camera")
            self.objdetect.detect_object()
            return "Object detection done"
        elif "translate" in audio_command :
            audio_command = audio_command.split("translate")
            text = audio_command[1]
            output = self.translator.translate_enfr(text)
            return output
        else :
            output = self.chat.generate_text(audio)
            return output

if __name__ ==  '__main__' :
    print("Starting ...")
    bot = AI()
    output = bot.run()
    print(output)