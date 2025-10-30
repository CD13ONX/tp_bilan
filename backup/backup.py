import subprocess
import datetime
import os
import sys

source = "backup/source_dir"
destination = "backup/backup_dir"

date = datetime.datetime.now().strftime("%Y-%m-%d-%Hh%M")
backup_path = os.path.join(destination, f"backup_{date}") #chemin sauvegarde
os.makedirs(backup_path, exist_ok=True) #création dossier sauvegarde

# Verification du dossier source
if not os.path.exists(source):
    print("Dossier source introuvable")

 # xcopy /E /I /Y : copie tout, crée dossier si nécessaire, pas de confirmation
cmd = f'xcopy "{source}" "{backup_path}" /E /I /Y'

try:
    # execution commande + capture erreurs si existantes
    result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Sauvegarde ok")

except subprocess.CalledProcessError as e:
    print("Erreur lors de la sauvegarde :")
    print(e.stderr) #Affichage errreur
