from elevenlabs import play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="YOURAPIKEY", # Defaults to ELEVEN_API_KEY
)

audio = client.generate(
  text="Hello James",
  voice="Brian",
  model="eleven_multilingual_v2"
)
play(audio)
