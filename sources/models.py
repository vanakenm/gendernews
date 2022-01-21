from django.db import models
from django.db.models import Count

# Create your models here.

class Source(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    logoUrl = models.URLField(max_length=200, null=True)
    finder = models.CharField(max_length=20)
    locale = models.CharField(max_length=10, default="fr-BE")

    def last_analysis(self, date=None):
        if(date):
          daily_records = self.analysis_set.filter(date__date=date)
          if(daily_records.count() > 0):
            return daily_records.latest('date')
          else:
            return None
        else:
          if(self.analysis_set.count() > 0):
            return self.analysis_set.latest('date')
          else:
            return None

    def __str__(self):
        return self.name

    def language(self):
        return self.locale.split("-")[0]

    def country_code(self):
        return self.locale.split("-")[1].lower()
        
    def names(self, days=7):
        anas = self.analysis_set.order_by('-date')[:days]
        names = {}
        for analysis in anas:
            a_names = analysis.results["names"]
            for name in a_names:
                if not name["name"] in names:
                    names[name["name"]] = 0
                names[name["name"]] += 1
        return names

class Analysis(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    html = models.TextField()
    results = models.JSONField()

    def stats(self):
      names = self.results["names"]
      male = len([r for r in names if r["gender"] == "male" or r["gender"] == "mostly_male"])
      female = len(names) - male
      total = len(names)

      if(total == 0):
        return {"male": male, "malepc": 0, "femalepc": 0 , "female": female, "total": total}


      femalepc = int((female * 100) / total)
      return {"male": male, "malepc": 100 - femalepc, "femalepc":  femalepc, "female": female, "total": total}

    def __str__(self):
        return self.source.name + " - " + self.date.strftime("%Y-%m-%d")

class ReportLine(models.Model):
    source_name = models.TextField()
    date = models.DateTimeField('date published')
    gender = models.TextField()
    name = models.TextField()

    @classmethod
    def top5(cls, gender):
      top5 = ReportLine.objects.filter(gender=gender).values('name').annotate(total=Count('name')).order_by('-total')[:5]
      return top5

