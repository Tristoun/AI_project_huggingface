from elevenlabs import play
from elevenlabs.client import ElevenLabs

f = open("api_key.txt", "r")
API_KEY = f.read()


class TTS() :
  def __init__(self) -> None:
    self.client = ElevenLabs(
      api_key=API_KEY,
    )

  def text_to_speech(self, prompt) :
    audio = self.client.generate(
      text=prompt,
      voice="Brian",
      model="eleven_multilingual_v2"
    )

    play(audio)


if __name__ == "__main__":
  tts = TTS()
  tts.text_to_speech("Hello James")