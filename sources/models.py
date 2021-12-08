from django.db import models

# Create your models here.

class Source(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    logoUrl = models.URLField(max_length=200, null=True)
    finder = models.CharField(max_length=20)

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


      return {"male": male, "malepc": int((male * 100) / total), "femalepc": int((female * 100) / total) , "female": female, "total": total}

    def __str__(self):
        return self.source.name + " - " + self.date.strftime("%Y-%m-%d")