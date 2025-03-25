#!/bin/bash

# Démarrage du service cron
/etc/init.d/cron start

# Exécuter le script une première fois au démarrage
cd /app && python scripts/update_seances.py >> /var/log/cron.log 2>&1

# Garder le conteneur en vie et le cron actif
cron -f &
tail -f /var/log/cron.log 