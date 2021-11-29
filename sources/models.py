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
      male = len([r for r in self.results if r["gender"] == "male" or r["gender"] == "mostly_male"])
      female = len(self.results) - male

      return {"male": male, "female": female, "total": len(self.results)}

    def __str__(self):
        return self.source.name + " - " + self.date