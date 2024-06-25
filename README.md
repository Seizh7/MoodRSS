# MoodRSS

MoodRSS est une application web permettant d'analyser les flux RSS pour déterminer le sentiment des articles et les afficher sur un tableau de bord. L'analyse de sentiment est réalisée en utilisant l'analyseur de sentiment VADER.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Citation](#citation)
- [Auteur](#auteur)

## Fonctionnalités

- Recherche de flux RSS par URL
- Analyse des flux RSS pour déterminer le sentiment des articles (positif, négatif, neutre)
- Affichage des articles sur un tableau de bord
- Filtrage des articles par sentiment

## Prérequis

- Docker
- Docker Compose

## Installation et exécution 

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
DJANGO_ALLOWED_HOSTS=moodrss.seizh.synology.me
CSRF_TRUSTED_ORIGINS=https://moodrss.seizh.synology.me
```

### 3. Construire et démarrer les conteneurs Docker

#### Version développement

```
docker-compose -f docker-compose.dev.yml up --build -d
```

#### version production

```
docker-compose -f docker-compose.yml up --build -d
```

### 4. Accéder à l'application

#### Version développement

```
localhost:8000
```

#### version production

```
https://moodrss.seizh.synology.me
```

## Utilisation

Ouvrez votre navigateur et accédez à l'URL de développement ou de production.
Entrez l'URL d'un flux RSS dans la barre de recherche.
Cliquez sur "Search" pour analyser le flux RSS.
Utilisez le bouton "Filter by Mood" pour filtrer les articles par sentiment.

## Citation

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

## Auteur

Ronan Lossouarn
