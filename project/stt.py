from RealtimeSTT import AudioToTextRecorder



class AudioRecorder() :

    def print_text(self, text) :
        print(text)

    def record_audio(self) :
        recorder =  AudioToTextRecorder(model="small.en", spinner=False, no_log_file=True, compute_type="float32",)
        print("Start recording")
        output = recorder.text()
        recorder.shutdown()
        self.print_text(output)
        return output
    

if __name__ == '__main__':
    ia = AudioRecorder()
    while True : 
        output = ia.record_audio()

