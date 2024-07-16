# MoodRSS

MoodRSS est une application web permettant d'analyser les flux RSS pour déterminer le sentiment des articles et les afficher sur un tableau de bord. L'analyse de sentiment est réalisée en utilisant l'analyseur de sentiment VADER.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Documentations](#documentations)
- [Citation](#citation)

## Fonctionnalités

- Recherche de flux RSS par URL
- Analyse des flux RSS pour déterminer le sentiment des articles (positif, négatif, neutre)
- Affichage des articles sur un tableau de bord
- Filtrage des articles par sentiment

## Prérequis

- Docker
- Docker Compose

## Installation

### 1. Cloner le dépôt

```
git clone https://github.com/votre-utilisateur/moodrss.git
cd moodrss
```

### 2. Configurer le fichier des variables d'environnement

Modifier la clé secrète dans le fichier des variables d'environnement, pour la version en production uniquement.

.env :
```
SECRET_KEY=clé_secrète
DEBUG=False
DJANGO_ALLOWED_HOSTS=moodrss.seizh.synology.me localhost
CSRF_TRUSTED_ORIGINS=https://moodrss.seizh.synology.me http://localhost:1009
```

### 3. Construire et démarrer les conteneurs Docker

```
make build # Version de production
make build ENV=dev # Version de développement
```

### 4. Suivre les logs

```
make logs # Version de production
make logs ENV=dev # Version de développement
```

### 5. Arrêter les services

```
make down # Version de production
make down ENV=dev # Version de développement
```


### 6. Supprime les conteneurs, images et volumes

```
make clean # Version de production
make clean ENV=dev # Version de développement
```

### 7. Accéder à l'application

#### Version de développement

```
localhost:8000
```

#### version de production

```
localhost:1009
```
ou
```
https://moodrss.seizh.synology.me
```

## Utilisation

Ouvrez votre navigateur et accédez à l'URL de développement ou de production.
Entrez l'URL d'un flux RSS dans la barre de recherche.
Cliquez sur "Search" pour analyser le flux RSS.
Utilisez le bouton "Filter by Mood" pour filtrer les articles par sentiment.

## Documentations

Une documentation complète est disponible dans le dossier "Documentations", comprenant les éléments suivants :
- Documentation utilisateur
- Documentation technique
- Cahier des charges & spécification
- Rapport de réalisation

## Citations

Ce projet utilise les bibliothèques tierces suivantes :

1. **feedparser**
   - Licence : Licence BSD
   - Auteurs : 2010-2023 Kurt McKee, 2004-2008 Mark Pilgrim

2. **dateutil**
   - Licence : Double Licence (Apache 2.0 ou BSD 3-Clause pour les contributions après le 1er décembre 2017)
   - Auteur original : Gustavo Niemeyer
   - Mainteneurs : Tomi Pieviläinen, Yaron de Leeuw & Paul Ganssle

3. **vader**
   - Licence : Licence Apache 2.0
   - Auteurs : Hutto, C.J. & Gilbert, E.E.

Pour les textes complets des licences, consultez le fichier LICENSE.