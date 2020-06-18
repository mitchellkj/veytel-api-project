from django.db import models
from datetime import timedelta
from django.utils.timezone import now

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        timeNow = now()
        timeDelta = timedelta(days=1)
        pubDate = self.pub_date
        return timeNow - timeDelta <= pubDate <= timeNow

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text