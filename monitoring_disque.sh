#!/bin/bash

LOG_FILE="journal_monitoring_disk.log"

echo "Espace disque disponible :"

df -h | awk 'NR>1' | while read ligne; do # awk 'NR>1' saute l'entête
    utilisation=$(echo "$ligne" | awk '{print $5}' | tr -d '%') #utilisation (%) : colonne 5
    partition=$(echo "$ligne" | awk '{print $1}') #nom de la partition
    montage=$(echo "$ligne" | awk '{print $6}')

    echo "$partition ($montage) → ${utilisation}% utilisé"

# Si >80%
  if [ "$utilisation" -gt 80 ]; then
    message="[ALERTE] $(date) : $partition ($montage) a dépassé le seuil de 80% et a atteint ${utilisation}% d’utilisation."
    echo "$message" >> "$LOG_FILE"
  fi

done
