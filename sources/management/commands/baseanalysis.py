from django.core.management.base import BaseCommand
import spacy
from bs4 import BeautifulSoup
import requests
from sources.models import Source
from sources.models import Analysis
import gender_guesser.detector as gender
import datetime

class AnalysisCommand(BaseCommand):
    help = 'Run analysis for all sources'
    nl_model = spacy.load("nl_core_news_sm")
    fr_model = spacy.load("fr_core_news_sm")

    models = {
      "nl": {
        "model": nl_model,
        "tag": "PERSON"
      },
      "fr": {
        "model": fr_model,
        "tag": "PER"
      }
    }

    d = gender.Detector()

    def get_results(self, titles, name, language):
      nlp = self.models[language]["model"]
      results = {}
      names_found = []
      print("Analying: " + name + " in " + language)
      for(title) in titles:
          doc = nlp(title)
          for word in doc.ents:
              if(word.label_ == self.models[language]["tag"]):
                  gender = self.d.get_gender(word.text.split(" ")[0])
                  if(gender != "unknown"):
                      print(name + ":" + word.text + " - " + gender)
                      found = word.text
                      start = title.index(found)
                      end = start + len(found)
                      before = title[:start]
                      after = title[end:]
                      names_found.append({
                        "name": found, 
                        "gender": gender, 
                        "source": name, 
                        "sentence": title,
                        "before": before,
                        "after": after
                      })

      results["names"] = names_found
      results["titles"] = titles
      return results