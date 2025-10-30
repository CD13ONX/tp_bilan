#!/bin/bash

echo "Espace disque disponible :"

df -h | awk 'NR>1' | while read ligne; do # awk 'NR>1' saute l'entête
  utilisation=$(echo "$ligne" | awk '{print $5}' | tr -d '%') #utilisation (%) : colonne 5
  partition=$(echo "$ligne" | awk '{print $1}') #nom de la partition

  echo "$partition ($montage) → ${utilisation}% utilisé"

# Si >80%
  if [ "$utilisation" -gt 80 ]; then
    message="La partition a dépassé 80% d'utilisation"
    echo $message
  fi

done


