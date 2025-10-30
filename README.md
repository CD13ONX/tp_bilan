# tp_bilan
TP bilan module Techniques de Scripting Système

Chaque tâche administrative (sauvegarde, monitoring) se trouve dans un sous-dossier dédié et comporte un fichier de logs. Les scripts sont commentés et ont été développés sur une branche develop avant d'être fusionnés à la branche main. L'historique de commits est disponible sur github.

1. Monitoring espace disque
Surveillance de l'espace disque utilisé et mise en place d'alertes au delà d'un seuil de 80% 

2. Sauvegardes
Sauvegarde des dossiers critiques vers un emplacement de sauvegarde avec horodatage, afin de les récupérer en cas de problème

Structure répertoire tp_bilan : 

tp_bilan/
├── backup/
│   ├── backup_dir/           #dossier de sauvegarde
│   ├── source_dir/           #dossier à sauvegarder
|   ├── backup.log            #logs
│   └── backup.py             #script sauvegarde
│
├── monitoring_disque/
│   └── monitoring_disque.sh  #script bash
|   └── journal_monitoring_disk.py    #logs 
│
├── README.md
