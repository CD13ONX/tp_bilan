import subprocess
import datetime
import os
import sys

source = "backup/source_dir"
destination = "backup/backup_dir"
timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%Hh%M")
backup_path = os.path.join(destination, f"backup_{timestamp}")
os.makedirs(backup_path, exist_ok=True)


# xcopy /E /I /Y : copie tout, crée dossier si nécessaire, pas de confirmation
cmd = f'xcopy "{source}" "{backup_path}" /E /I /Y'
subprocess.run(cmd, shell=True)

