###########
# BUILDER #
###########

# Image de base du conteneur
FROM python:3.11.4-slim-buster as builder

# Définit le répertoire de travail
WORKDIR /usr/src/moodrss

# Variables d'environnement pour optimiser les performances de Python
ENV PYTHONUNBUFFERED 1 \
    PYTHONDONTWRITEBYTECODE 1

# Copie le code source de l'application
COPY . /usr/src/moodrss/

# Controle des conventions de code 
RUN pip install --upgrade pip
RUN pip install flake8==6.0.0
RUN flake8 --ignore=E501,F401 .

# Installe les dépendances
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/moodrss/wheels -r requirements.txt

#########
# FINAL #
#########

FROM python:3.11.4-slim-buster

# Crée l'utilisateur de l'application
RUN addgroup --system moodrss && adduser --system --ingroup moodrss moodrss

# Crée les répertoires appropriés
ENV APP_HOME=/home/moodrss/web
RUN mkdir -p $APP_HOME/staticfiles
WORKDIR $APP_HOME

# Copie des dépendances depuis l'étape de construction
COPY --from=builder /usr/src/moodrss/wheels /wheels
COPY --from=builder /usr/src/moodrss/requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache /wheels/*

# Copie le code source de l'application
COPY . $APP_HOME

# Change l'utilisateur
USER moodrss
