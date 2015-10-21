from django.contrib import admin
from .models import Question, Answer
from .forms import QuestionForm
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm

admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer)
