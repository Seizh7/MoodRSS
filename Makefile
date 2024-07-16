# Variables
DOCKER_COMPOSE = docker-compose
COMPOSE_FILE ?= docker-compose.yml

# Défini le fichier docker-compose en fonction de l'environnement
ifeq ($(ENV),dev)
	COMPOSE_FILE = docker-compose.dev.yml
endif


build: # Construit les images Docker
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) up -d --build

down: # Arrête les services
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) down -v

logs: # Affiche les logs des services
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) logs -f

clean: # Supprime les conteneurs, images, volumes et réseaux
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) down --rmi all --volumes --remove-orphans
