from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField('question')
    date_posted = models.DateTimeField('date posted', auto_now = False, auto_now_add=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    thequestion = models.ForeignKey('Question', related_name='answer')
    answer = models.TextField()
    date_answered = models.DateTimeField('date answered', auto_now = False, auto_now_add=True)

    def __str__(self):
        return self.answer
