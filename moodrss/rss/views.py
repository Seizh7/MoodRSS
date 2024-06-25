''' Nom : views.py
Rôle : Vue Django pour analyser les flux RSS, déterminer le sentiment des articles et les afficher sur un tableau de bord.
Auteur : Ronan LOSSOUARN
Date : 04/04/2024
Licence : L3 Réalisation de programme

DESCRIPTION
Cette vue Django récupère un flux RSS depuis une URL fournie par l'utilisateur, nettoie le contenu HTML des résumés, analyse le sentiment des articles en utilisant VADER, et affiche les articles. Les articles peuvent être filtrés par sentiment. La vue gère les requêtes POST pour traiter les données soumises par l'utilisateur. '''

from django.shortcuts import render
from rss.parser import prepare_rss_feed
from rss.prediction import get_prediction


# Traite les requêtes pour afficher un tableau de bord des flux RSS avec analyse de sentiment.
# @param request -> l'objet de requête HTTP ;
# @return -> rend la page HTML du tableau de bord avec les flux RSS analysés et filtrés par sentiment.
def dashboard(request):
    if request.method == 'POST':
        # Récupère les données soumises par l'utilisateur
        data = request.POST
        url = data['url']  # URL du flux RSS entré par l'utilisateur
        feeds = prepare_rss_feed(url)  # Prépare le flux RSS

        # Vérifie si un filtre de sentiment a été sélectionné
        if data['sentiment']:
            selected = data['sentiment']

        # Vérifie si des flux ont été trouvés
        if feeds != "Not found":
            found = 'true'

            unique_feeds = []
            seen_titles = set()

            # Élimine les doublons
            for feed in feeds:
                if feed.title not in seen_titles:
                    unique_feeds.append(feed)
                    seen_titles.add(feed.title)

            for feed in unique_feeds:
                # Analyse le sentiment du titre et du résumé
                feed['sentiment'] = get_prediction(feed.title, feed.summary)
                # Ajoute du texte secondaire en fonction du sentiment analysé
                if feed['sentiment'] == 'Positive':
                    feed['secondary_text'] = 'This feed brings positive content.'
                elif feed['sentiment'] == 'Negative':
                    feed['secondary_text'] = 'The tone of this feed is more negative.'
                else:
                    feed['secondary_text'] = 'This feed provides articles with a neutral tone.'

                # Affecte le nom de l'auteur s'il est disponible
                if 'authors' in feed:
                    feed['author_name'] = feed.authors[0]['name']
                else:
                    feed['author_name'] = None

                # Affecte le lien du flux s'il est disponible
                if 'link' in feed:
                    feed['link'] = feed.link
                else:
                    feed['link'] = None

                # Affecte la date de publication si elle est disponible
                if 'published' in feed:
                    feed['published'] = feed.published
                else:
                    feed['published'] = None

            # Filtre les flux par sentiment sélectionné
            selected_sentiment = data.get('sentiment', 'All')  # Par défaut
            if selected_sentiment != 'All':
                unique_feeds = [feed for feed in unique_feeds if feed['sentiment'] == selected_sentiment]

            # Vérifie s'il y a des flux à afficher et rend la page avec les flux
            if len(unique_feeds) > 0:
                return render(request, "dashboard.html", {'feeds': unique_feeds, 'found': found, 'selected': selected, 'url': url, 'empty': 'no', 'feed': unique_feeds[0]})
            else:
                # Rend la page indiquant qu'il n'y a aucun flux à afficher
                return render(request, "dashboard.html", {'feeds': unique_feeds, 'found': found, 'selected': selected, 'url': url, 'empty': 'yes'})

        else:
            # Indique que le flux RSS n'a pas été trouvé
            found = 'false'
            return render(request, "dashboard.html", {'feeds': None, 'found': found, 'selected': selected})

    else:
        # Rend la page du tableau de bord vide pour une requête GET
        return render(request, "dashboard.html")
