import torch
import os
from diffusers import ShapEPipeline
from diffusers.utils import export_to_gif
from PIL import Image
import time

# Chargement du modèle Shap-E
ckpt_id = "openai/shap-e"
device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = ShapEPipeline.from_pretrained(ckpt_id).to(device)

# Paramètres de génération
guidance_scale = 15.0
prompt = "Pikachu"

# Générer les images sans spécifier la taille
images = pipe(
    prompt,
    guidance_scale=guidance_scale,
    num_inference_steps=64,
).images

# Aplatir la liste d'images si nécessaire
if isinstance(images, list) and isinstance(images[0], list):
    images = [img for sublist in images for img in sublist]

# Redimensionner les images après leur génération
target_size = (256, 256)  # Taille souhaitée pour les images (ex : 512x512 pixels)
images_resized = [img.resize(target_size, Image.Resampling.LANCZOS) for img in images]

# Vérification de la structure des données retournées par pipe()
if isinstance(images_resized, list) and isinstance(images_resized[0], list):
    # Si images est une liste contenant des listes d'images, on aplatit
    images_resized = [img for sublist in images_resized for img in sublist]

# Convertir chaque image en RGB si ce n'est pas déjà le cas
images_resized = [img.convert("RGB") if isinstance(img, Image.Image) else img for img in images_resized]

# Définir le dossier de sortie avec un chemin valide
output_folder = os.path.expanduser("~/AI_test_text_2_3D/3D_Models_Results")
os.makedirs(output_folder, exist_ok=True)

# Construire le nom du fichier basé sur le prompt
filename = f"{prompt.replace(' ', '_')}_3D_Models.gif"

# Vérifier si le fichier existe déjà et ajouter un suffixe si nécessaire
gif_path = os.path.join(output_folder, filename)
if os.path.exists(gif_path):
    timestamp = time.strftime("%Y%m%d_%H%M%S")  # Ajouter un horodatage unique
    filename = f"{prompt.replace(' ', '_')}_3D_Models_{timestamp}.gif"
    gif_path = os.path.join(output_folder, filename)

# Exportation du GIF - Assurer que l'on passe la liste d'images à export_to_gif
export_to_gif(images_resized, gif_path)

print(f"GIF exporté avec succès : {gif_path}")
