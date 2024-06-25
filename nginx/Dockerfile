# Image officielle
FROM nginx:1.25

# Supprime la configuration par défaut de NGINX
RUN rm /etc/nginx/conf.d/default.conf

# Copie le fichier de configuration personnalisé dans le répertoire de configuration
COPY nginx.conf /etc/nginx/conf.d
