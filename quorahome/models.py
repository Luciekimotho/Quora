from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField('question')
    date_posted = models.DateTimeField('date posted')

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.TextField('answer')
    date_answered = models.DateTimeField('date answered')

    def __str__(self):
        return self.answer
