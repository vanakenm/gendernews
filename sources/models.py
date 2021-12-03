from django.db import models

# Create your models here.

class Source(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    logoUrl = models.URLField(max_length=200, null=True)
    finder = models.CharField(max_length=20)

    def last_analysis(self):
        return self.analysis_set.latest('date')

    def __str__(self):
        return self.name


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

      return {"male": male, "malepc": (male * 100) / total, "femalepc": (female * 100) / total , "female": female, "total": total}

    def __str__(self):
        return self.source.name + " - " + self.date.strftime("%Y-%m-%d")