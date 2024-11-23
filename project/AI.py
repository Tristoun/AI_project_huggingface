from stt import AudioRecorder
from text_generation import ChatAI

class AI() :
    def __init__(self) -> None:
        self.recorder = AudioRecorder()
        self.chat = ChatAI()

    def run(self) :
        audio = self.recorder.record_audio()
        output = self.chat.generate_text(audio)
        return output

if __name__ ==  '__main__' :
    bot = AI()
    output = bot.run()
    print(output)