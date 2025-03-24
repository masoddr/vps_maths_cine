FROM python:3.11-slim

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    cron \
    && rm -rf /var/lib/apt/lists/*

# Création du répertoire de travail
WORKDIR /app

# Copie des fichiers du projet
COPY . .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Configuration de cron
COPY crontab /etc/cron.d/update-seances
RUN chmod 0644 /etc/cron.d/update-seances && \
    crontab /etc/cron.d/update-seances && \
    touch /var/log/cron.log

# Script d'entrée
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"] 