#!/bin/bash

# Démarrage du service cron
service cron start

# Exécution initiale du script
python scripts/update_seances.py

# Garder le conteneur en vie
tail -f /var/log/cron.log 