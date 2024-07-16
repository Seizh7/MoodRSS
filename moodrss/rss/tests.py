from django.test import TestCase, Client
from django.urls import reverse


class MoodRSSTests(TestCase):

    # Prépare l'environnement de test
    def setUp(self):
        self.client = Client()
        self.url = reverse('dashboard')

    # Test de la requête GET pour vérifier que la page se charge correctement sans flux RSS
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
        self.assertContains(response, 'MoodRSS')

    # Test de la requête POST avec une URL de flux RSS valide
    def test_post_valid_rss(self):
        response = self.client.post(self.url, {'url': 'https://www.cinemablend.com/feeds.xml', 'sentiment': 'All'})
        self.assertEqual(response.status_code, 200)
        # Vérifie qu'il ne contient pas le message "Feed not found"
        self.assertNotContains(response, 'Feed not found')
        # Vérifie que des flux sont retournés
        self.assertGreater(len(response.context['feeds']), 0)

    # Test de la requête POST avec une URL de flux RSS invalide
    def test_post_invalid_rss(self):
        response = self.client.post(self.url, {'url': 'http://invalid-rss-feed.com/rss', 'sentiment': 'All'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Feed not found')

    # Test de la requête POST avec un filtre de sentiment
    def test_post_sentiment_filter(self):
        # Effectue une requête avec un filtre de sentiment
        response = self.client.post(self.url, {'url': 'https://www.cinemablend.com/feeds.xml', 'sentiment': 'Positive'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Feed not found')
        # Vérifie que tous les flux retournés ont un sentiment positif
        for feed in response.context['feeds']:
            self.assertEqual(feed['sentiment'], 'Positive')
