from django.contrib import admin
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm

class AnswerAdmin(admin.ModelAdmin):
    form = AnswerForm

admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer)
