from stt import AudioRecorder
from text_generation import ChatAI
from object_detection import ObjectDetection
from translate import Translator
from tts import TTS

class AI() :
    def __init__(self) -> None:
        self.recorder = AudioRecorder()
        self.chat = ChatAI()
        self.objdetect = ObjectDetection()
        self.translator = Translator()
        self.speaker = TTS()

    def log(self, output) :
        print(output)

    def run(self) :
        audio = self.recorder.record_audio()
        audio_command = audio.lower()

        if "open the camera" in audio_command :
            self.log("Opening camera")
            self.objdetect.detect_object()
            return None
        elif "translate" in audio_command :
            audio_command = audio_command.split("translate")
            text = audio_command[1]
            output = self.translator.translate_enfr(text)
            return output
        else :
            output = self.chat.generate_text(audio)
            return output
        
    def speak(self, prompt) :
        self.speaker.text_to_speech(prompt) 

if __name__ ==  '__main__' :
    print("Starting ...")
    bot = AI()
    output = bot.run()
    if(output != None) :
        print(output)
        bot.speak(output)