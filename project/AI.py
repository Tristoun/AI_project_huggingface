from stt import AudioRecorder
from text_generation import ChatAI
from object_detection import ObjectDetection
from translate import Translator
from tts import TTS
from text3d import ThreeDGenerator
from huggingface_hub import login
import keyboard

login("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")

class AI() :
    def __init__(self) -> None:
        self.recorder = AudioRecorder()
        self.chat = ChatAI()
        self.objdetect = ObjectDetection()
        self.translator = Translator()
        self.speaker = TTS()

    def log(self, output) :
        print(output)

    def speak(self, prompt) :
        self.speaker.text_to_speech(prompt) 

    def run(self) :
        while True :
            print("Press enter to run..")
            key = keyboard.read_key()
            if (key == "enter") :
                audio = self.recorder.record_audio()
                audio_command = audio.lower()
                if "open the camera" in audio_command :
                    self.log("Opening camera")
                    self.objdetect.detect_object()
                elif audio_command.startswith("translate"):
                    audio_command = audio_command.split("translate")
                    text = audio_command[1]
                    output = self.translator.translate_enfr(text)
                    self.speak(output)
                elif audio_command.startswith("generate in 3d") :
                    threed = ThreeDGenerator()
                    audio_command = audio_command.split("generate in 3d")
                    text = audio_command[1]
                    threed.generate3D(text)
                else :
                    output = self.chat.generate_text(audio)
                    print(output)
                    self.speak(output)
            elif (key == "q") :
                print("Exiting...")
                break
        


if __name__ ==  '__main__' :
    print("Starting ...")
    bot = AI()
    output = bot.run()
