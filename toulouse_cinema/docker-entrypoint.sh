#!/bin/bash

# Exécuter le script une première fois au démarrage
cd /app && python scripts/update_seances.py >> /var/log/cron.log 2>&1

# Démarrer cron en premier plan
cron -f 