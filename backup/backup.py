import subprocess
import datetime
import os
import sys


def simulation_mail(destinataire, message):
    mail = "----- Simulation envoi mail -----\n À : " + destinataire + "\n Message : " + message + " \n ---------------------------------"
    return mail

source = "backup/source_dir"
destination = "backup/backup_dir"
destinataire_email="admin@gmail.com"

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
    print(simulation_mail(destinataire_email, "Sauvegarde ok"))

except subprocess.CalledProcessError as e:
    erreur=e.stderr
    print(simulation_mail(destinataire_email, "Erreur lors de la sauvegarde : "+ erreur))
