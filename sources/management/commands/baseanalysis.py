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
    nlp = spacy.load("fr_core_news_sm")
    d = gender.Detector()

    def get_results(self, titles, name):
      results = []
      for(title) in titles:
          doc = self.nlp(title)
          for word in doc.ents:
              if(word.label_ == "PER"):
                  gender = self.d.get_gender(word.text.split(" ")[0])
                  if(gender != "unknown"):
                      print(name + ":" + word.text + " - " + gender)
                      found = word.text
                      start = title.index(found)
                      end = start + len(found)
                      before = title[:start]
                      after = title[end:]
                      results.append({
                        "name": found, 
                        "gender": gender, 
                        "source": name, 
                        "sentence": title,
                        "before": before,
                        "after": after
                      })
                      # html = self.wrap(word.text, html)
      return results