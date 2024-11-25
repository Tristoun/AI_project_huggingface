Project for IA Classes
Using python3.10    

Setup the environment :
1 - Create a virtual environment
python3 -m venv <name of the environment>
if venv is not installed : pip install virtualenv

2- Activate the environment :
Go to the bin (Scripts for Windows) folder of your virtual environment then
For Ubuntu user : source bin/activate
For Windows user (in Powershell) :
Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
.\activate

To desactivate it :
source deactivate (Ubuntu)
deactivate.bat (Windows)

Then you can clone the repo here (git clone...)

Install require Librairies:
pip install RealtimeSTT (if you are on Ubuntu and it failed to install use sudo apt-get install portaudio19-dev and then retry the installation of this package)
pip install -U transformers
pip install torch 
pip install opencv-python
pip install ultralytics
pip install supervision

When you launch the project it will take a while depending on your internet connection it needed to download the model you requests
So be patient.

If you don't want message from log studown of RealtimeSTT:
Open site-packages folder -> RealtimeSTT -> audio_recorder.py then put in comment line 1560
Sometimes a token is asket for using models from HuggingFace
To prevent this just connect into you account and create a token in you account page
Then go to the page of the model and accept the utilisation conditions.

If you have warning during model installation, you can enable developper parameter in your settings.

Then to try the project start AI.py !

Utilisation :
- You talk into the mic when it's saying "Start recording" -> if you don't use specific command it'll use for now a chat ai to answer (it takes quite few times depends your computer)
- Then if you want to do some command you can see all the commands in the txt file "command.txt"
- For object detection you can see all possible detections with "yolov8class.txt"