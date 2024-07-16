''' Nom : prediction.py
Rôle : Programme qui analyse le sentiment des titres et résumés d'articles en utilisant VADER.
Auteur : Ronan LOSSOUARN
Date : 03/04/2024
Licence : L3 Réalisation de programme

DESCRIPTION
Le programme combine un titre et un résumé d'article en un seul texte et utilise l'analyseur de sentiment VADER pour évaluer le sentiment global de ce texte. En fonction du score de sentiment global (score compound), le programme retourne une prédiction de sentiment sous forme de chaîne de caractères : 'Positive' si le score est positif, 'Negative' si le score est négatif, 'Neutral' si le score est neutre.
'''

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import unittest


# Analyse le sentiment d'un titre et d'un résumé pour évaluer le sentiment global.
# @param title -> le titre de l'article ;
# @param summary -> le résumé de l'article ;
# @return -> chaîne de caractères, 'Positive', 'Negative' ou 'Neutral'.
def get_prediction(title, summary):
    try:
        nltk.data.find('sentiment/vader_lexicon.zip')
    except LookupError:
        nltk.download('vader_lexicon')

    text = title + " " + summary

    # Analyse des scores de sentiment pour le texte
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    # Extraction du score compound (global) des sentiments
    compound_score = sentiment_scores['compound']

    # Sélection du sentiment
    if compound_score >= 0.1:
        return 'Positive'
    elif compound_score <= -0.1:
        return 'Negative'
    else:
        return 'Neutral'


class TestPrediction(unittest.TestCase):

    def test_positive(self):
        title = "Paddington In Peru Trailer Sends The Adorable Bear On A New Adventure, And I'm Ready To Follow Him Anywhere"
        summary = "The Paddington series of movies ranks as the most delightful, and Paddington in Peru looks to extend the winning streak."
        self.assertEqual(get_prediction(title, summary), 'Positive')

    def test_negative(self):
        title = "Someone Finally Asked Austin Butler About Those Pirates Of The Caribbean Rumors"
        summary = "Austin Butler responds to rumors he could star in the nextPirates of the Caribbean movie."
        self.assertEqual(get_prediction(title, summary), 'Negative')

    def test_neutral(self):
        title = "Late Night With Seth Meyers Staff Losing Jobs Amidst Budget Cuts: 'Nobody Wants To Pay"
        summary = "As part of budget cuts at NBC, Late Night with Seth Meyers is cutting a notable portion of its staff."
        self.assertEqual(get_prediction(title, summary), 'Neutral')


if __name__ == "__main__":
    unittest.main()
