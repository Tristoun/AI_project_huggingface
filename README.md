Project for IA Classes
Using python3.10 

Require Librairies:
- pip install RealtimeSTT (if you are on Ubuntu and it failed to install use sudo apt-get install portaudio19-dev and then retry the installation of this package)
- pip install -U transformers
- pip install torch 
- pip install opencv-python
- pip install ultralytics
- pip install supervision
- pip install accelerate
- pip install sentencepiece
- pip install sacremoses
- pip install elevenlabs
- pip install diffusers
- pip install keyboard

When launching the project it may take a while since it needs to download the AI
If you have warning during model installation, you can enable developper parameter in your settings.
You need to create an api key on https://elevenlabs.io/ to enable text to speech feature, and paste it to the file called api_key.txt

Then try the project with starting AI.py !

Utilisation :
- You talk into the mic when it's saying "Start recording" -> if you don't use specific command it'll use a chat ai to answer (it takes quite few times depends your computer)
- Then if you want to do some command you can see all the commands in the txt file "command.txt"
- For object detection you can see all possible detections with "yolov8class.txt"