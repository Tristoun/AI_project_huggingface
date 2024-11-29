from RealtimeSTT import AudioToTextRecorder



class AudioRecorder() :
    def __init__(self) :
        self.recorder = AudioToTextRecorder(model="small.en", spinner=False, no_log_file=True, compute_type="float32",)

    def print_text(self, text) :
        print(text)

    def record_audio(self) :
        print("Start recording")
        output = self.recorder.text()
        self.recorder.shutdown()
        self.print_text(output)
        return output
    

if __name__ == '__main__':
    ia = AudioRecorder()
    output = ia.record_audio()

