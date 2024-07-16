''' Nom : parser.py
Rôle : Programme qui récupère et analyse les flux RSS et nettoie le contenu HTML.
Auteur : Ronan LOSSOUARN
Date : 03/04/2024
Licence : L3 Réalisation de programme

DESCRIPTION
Le programme récupère un flux RSS depuis une URL et nettoie le contenu HTML des résumés des entrées.
'''

import feedparser
import re
from html import unescape
from dateutil.parser import parse as dateparse
import unittest


# Nettoie le contenu HTML brut en supprimant les balises HTML et en convertissant les caractères spéciaux.
# @param raw_html -> le contenu HTML brut ;
# @return -> le texte nettoyé sans balises HTML.
def clean_html(html_text):
    # Suppression des balises HTML
    clean_text = re.sub('<.*?>', '', html_text)
    # Convertion des caractères spéciaux
    return unescape(clean_text)


# Récupère un flux RSS depuis une URL, nettoie le contenu HTML des résumés et récupère les dates de publication.
# @param url -> l'URL du flux RSS ;
# @return -> une liste d'entrées de flux nettoyées, ou "Not found" si aucune entrée n'est trouvée.
def prepare_rss_feed(url):
    # Parcourt le flux RSS
    feed = feedparser.parse(url)
    # Vérifie s'il y a des entrées dans le flux
    if feed.entries:
        for entry in feed.entries:
            # Nettoie le résumé
            entry.summary = clean_html(entry.summary)
            # Récupère la date de publication
            entry.published = dateparse(entry.published)
        return feed.entries
    else:
        return "Not found"


class TestParser(unittest.TestCase):
    # Test avec une entrée
    def test_with_entries(self):
        rss_content = """
        <rss version="2.0">
            <channel>
                <title>Example RSS Feed</title>
                <description>This is an example RSS feed</description>
                <item>
                    <title>Exemple</title>
                    <description><![CDATA[Test résumé avec du contenu <b>HTML</b>.]]></description>
                    <pubDate>Tue, 21 May 2024 16:36:44 +0000</pubDate>
                </item>
            </channel>
        </rss>
        """
        result = prepare_rss_feed(rss_content)
        # Vérifie que la fonction retourne une entrée
        self.assertEqual(len(result), 1)
        # Vérifie que le résumé de l'entrée est nettoyé correctement
        self.assertEqual(result[0].summary, "Test summary with HTML content.")

    # Test sans une entrée
    def test_without_entries(self):
        rss_content = """
        <rss version="2.0">
            <channel>
                <title>Exemple RSS</title>
                <description>RSS</description>
            </channel>
        </rss>
        """
        result = prepare_rss_feed(rss_content)
        # Vérifie que la fonction retourne "Not found" quand il n'y a pas d'entrées
        self.assertEqual(result, "Not found")

    # Test de la fonction clen_html()
    def test_clean_html(self):
        # HTML brut
        raw_html = "<p>Test summary with <b>HTML</b> content.</p>"
        # Résultat attendu après nettoyage du HTML
        expected_output = "Test summary with HTML content."
        # Vérifier que la fonction clean_html nettoie le HTML correctement
        self.assertEqual(clean_html(raw_html), expected_output)


if __name__ == "__main__":
    unittest.main()
